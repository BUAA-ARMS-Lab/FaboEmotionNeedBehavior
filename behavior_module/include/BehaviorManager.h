#include <iostream>
#include "ros/ros.h"
#include <jsoncpp/json/json.h>
#include <string>
#include <vector>
#include <mutex>
#include <thread>
#include <unistd.h>
#include <fstream>
#include <std_msgs/Header.h>
// #include <behavior_module/need_msg.h>
// #include <behavior_module/behavior_msg.h>
// #include <behavior_module/behavior_list.h>
// #include <behavior_module/behavior_feedback_msg.h>
// #include <behavior_module/idleState.h>

#include <social_msg/need_msg.h>
#include <social_msg/behavior_msg.h>
#include <social_msg/behavior_list.h>
#include <social_msg/behavior_feedback_msg.h>
#include <social_msg/idleState.h>

#include "utils.h"
// #include <bits/stdc++.h>

using namespace std;
using namespace FABO_ROBOT;

// 子行为表达
class SubBehaviorExpression{
public:
    SubBehaviorExpression(){};
    bool is_necessary;  // 动作对行为是否必要
    double weight;   // 动作权重
};

// 视线
class Gaze : public SubBehaviorExpression{
public:
    string target;  // 目标对象
    double rate;  // 速率
};

// 情绪
class Emotion : public SubBehaviorExpression{
public:
    string type;  // 情绪类型
};

// 语音
class Voice : public SubBehaviorExpression{
public:
    string content;  // 语音内容
    int tone;// 语调（低沉、一般、高昂）
    double rate;  // 速率
};

// 操作
class Manipulator : public SubBehaviorExpression{
public:
    string action;  // 动作
    string target;  // 对象
    double rate;  // 速率
    double range; // 幅度
};

// 移动
class Mover : public SubBehaviorExpression{
public:
    string target;  // 目标（object/around）
    double rate;  // 速率
    double distance;  // 距离
    double range;  // 范围
};

// 子行为
class SubBehavior{
public:
    SubBehavior(){
        mActuators = vector<SubBehaviorExpression*>(5);
        mActuators[0] = new Gaze();
        mActuators[1] = new Emotion();
        mActuators[2] = new Voice();
        mActuators[3] = new Manipulator();
        mActuators[4] = new Mover();
    };
    string discription;
    vector<SubBehaviorExpression*> mActuators;
};

class Behavior{
public:
    Behavior(){
    };

    Behavior(const Behavior& beh, bool reserveStamp=true) : 
            name(beh.name), type(beh.type), current_phase(beh.current_phase), total_phase(beh.total_phase),
            target(beh.target), target_angle(beh.target_angle), target_distance(beh.target_distance),
            speech(beh.speech), rob_emotion(beh.rob_emotion), rob_emotion_intensity(beh.rob_emotion_intensity),
            weight(beh.weight), is_light(beh.is_light), necessary_count(beh.necessary_count),
            subBehaviorSeries(beh.subBehaviorSeries), scene(beh.scene),
            IDtype(beh.IDtype), person_emotion(beh.person_emotion), 
            satisfy_value(beh.satisfy_value), attitude(beh.attitude), 
            move_speed(beh.move_speed), distance(beh.distance), voice_speed(beh.voice_speed)
    {
        if (reserveStamp)
        {
            header.stamp = beh.header.stamp;
        }   
        else{
            header.stamp = ros::Time::now();
        }
    }

    // void configureByNeedMsg(const behavior_module::need_msg &msg)
    void configureByNeedMsg(const social_msg::need_msg &msg)
    {
        name = msg.need_name;
        scene = msg.scene;
        target = msg.person_name;
        IDtype = msg.IDtype;
        target_angle = msg.target_angle;
        target_distance = msg.target_distance;
        person_emotion = msg.person_emotion;
        rob_emotion_intensity = msg.rob_emotion_intensity;
        weight = msg.weight; // TODO：是否由需求给出权重
        speech = msg.speech;
        rob_emotion = msg.rob_emotion;
        satisfy_value = msg.satisfy_value;
        attitude = msg.attitude;
        move_speed = msg.move_speed;
        distance = msg.distance;
        voice_speed = msg.voice_speed;
        cout << "beh.move_speed = " << move_speed << endl;
        cout << "beh.distance = " << distance << endl;
        cout << "beh.voice_speed = " << voice_speed << endl;
    }

public:
    // params to pass to perform_module
    std_msgs::Header header;
    string name;
    string type;
    string scene;
    int current_phase = 0;
    int total_phase;
    string target;
    string IDtype;
    float target_angle;
    float target_distance;
    string speech;
    string rob_emotion;
    string person_emotion;
    int rob_emotion_intensity;
    int satisfy_value;
    string attitude;
    float move_speed;
    float distance;
    float voice_speed;
    
    // other params
    double weight;
    bool is_light;
    vector<int> necessary_count = {0,0,0,0,0};
    vector<SubBehavior> subBehaviorSeries;  // 子行为序列
};

/**
 * @brief 行为管理器
 * 
 */
class BehaviorManager
{
public:
    BehaviorManager();

    /**
     * @brief Construct a new Behavior Manager object
     * 
     * @param n 行为管理器所关联的节点句柄，用于接受和发送话题。
     * @param data_path 存储行为数据的json文件目录。
     */
    BehaviorManager(ros::NodeHandle& n, string data_path);
    // :n_(n)
    // {

    //     printInColor("==================================\n", BLUE);
    //     printInColor(" Welcome to use behavior_module! \n", BLUE);
    //     printInColor("==================================\n", BLUE);
    //     publisher_behavior_ = n_.advertise<behavior_module::behavior_msg>("/BehaviorInstruction", 1000);
    //     publisher_idlestate_ = n_.advertise<behavior_module::idleState>("/idleState",1000);
    //     subscriber_need_ = n_.subscribe("/need_lists", 1000, &BehaviorManager::need_msg_callback, this);
    //     subscriber_behavior_feedback_ = n_.subscribe("/BehaviorFeedback", 1000, &BehaviorManager::behavior_feedback_callback, this);
    //     ReadInBehaviorLibrary(data_path);
    //     sleep(1.2);
    //     TellIdleState(true, nullptr);
    // };

private:
    ros::NodeHandle n_;
    ros::Publisher publisher_behavior_;
    ros::Publisher publisher_behavior_list_;
    ros::Publisher publisher_idlestate_;
    ros::Subscriber subscriber_behavior_feedback_;
    ros::Subscriber subscriber_need_;

    mutex mutexBehaviorsTotal;
    mutex mutexCheckNewBeh;

    bool mbNewBehFlag;
    thread *mtWaitToUpdate;

    void ReadInBehaviorLibrary(const string &config_file);
    int AddNewBehavior(Behavior &new_behavior);

public:  //zhjd
    void TellIdleState(bool state, Behavior *completedBehavior);

private:
    Behavior* GetBehaviorByName(string name);
    // bool ReadInNewNeed(const behavior_module::need_msg &msg);
    bool ReadInNewNeed(const social_msg::need_msg &msg);
    void PrintBehaviorLibraryInfo();

    social_msg::behavior_msg GenerateBehaviorMsg(const Behavior& beh);

    void WaitToUpdate(float wait_seconds);

    void UpdateBehaviorPub();
    // void need_msg_callback(const behavior_module::need_msg &msg);
    void need_msg_callback(const social_msg::need_msg &msg);
    // {
    //     cout << "\n---------------------------------------------------" << endl;
    //     printInColor("【Received need_msg】", BLUE);
    //     cout << msg.need_name << endl << endl;
    //     ReadInNewNeed(msg);
    // }

    void behavior_feedback_callback(const social_msg::behavior_feedback_msg &msg);

    int InsertBehavior(Behavior &new_behavior);

    int ComputeParallel();

    void PrintBehaviorseries();

    void PrintBehaviors(vector<Behavior> &behaviors);

    void PrintBehaviorMsgInfo(social_msg::behavior_msg);

    void visualize_behavior_list();

    // 数据库所有行为名称的集合，用于在响应需求时判断是否有对应的行为
    set<std::string> msbehaviorsCatalog;

    // 行为数据库
    map<string,Behavior> mmbehaviorsLibrary;

    // 需要执行的总的行为序列，按权重从大到小排列
    vector<Behavior> mvbehaviorsTotal;

    // 当前正在并行执行的行为序列
    vector<Behavior> mvbehaviorsCurrent;

    // 存放占用各动作表现形式的行为序号
    vector<int> mviOccupancy = {1,1,1,1,1};

    // 标记当前是否处于等待停顿状态
    bool mbPauseFlag = false;

    // 存储最新算得的可并行行为数量
    int mParallelNum = 1;
};
