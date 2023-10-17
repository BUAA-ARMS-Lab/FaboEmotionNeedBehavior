//
// Created by zhjd on 2021/5/11.
//
//ros头文件
#include "common_include.h"

//内部头文件
// #include "need_satisfied.h"
#include "prior_need.h"
#include "perception_filter.h"

using namespace  std;
// time_t inner_need::time_for_wandor  =  0;
perception_filter *Filter = new perception_filter(20);   //TODO: 确定合适的per过滤时长阈值。

// ros node
ros::Subscriber sub_perception;
ros::Subscriber sub_robot_emotion;
ros::Subscriber sub_robot_status;
ros::Publisher pub;  //need
ros::Publisher query_attitude;
ros::Subscriber sub_idleState;
//全局变量: 
bool single_attitude = false;  //是否实时输出需求模块的状态，默认不输出
int period_cur = 0;   //每个period的周期时长,由 sleep函数 决定。




void single_need_test(ros::NodeHandle*  n_ptr){
            if(print_status)  printf( GREEN "Run %dth PriorNeed（运行先验模型） !!\n"NONE, period_cur);            
            vector<need> need_lists = PriorNeed.need_compute_all();
            if( need_lists.size() != 0 )
                for(int j =0 ; j< need_lists.size(); j++){
                    
                    //接受社交态度及相关参数
                    social_msg::attitude_query query;
                    query.IDtype = need_lists[j].IDtype;
                    query.motivation = need_lists[j].need_name;
                    query.person_name = need_lists[j].person_name;
                    query_attitude.publish(query);
                    double t = 1.0;
                    ros::Duration timeout(t);
                    ROS_INFO("Need waiting for social attitude");
                    social_msg::attitude_msg::ConstPtr result = ros::topic::waitForMessage<social_msg::attitude_msg>("attitude", *n_ptr, timeout);
                    
                    // 将need发布给行为模块
                    social_msg::need_msg need_output;
                    need_output.person_name =  need_lists[j].person_name;
                    need_output.IDtype = need_lists[j].IDtype;
                    need_output.scene = need_lists[j].scene;
                    need_output.need_name = need_lists[j].need_name;  
                    need_output.target_angle = need_lists[j].target_angle;
                    need_output.target_distance = need_lists[j].target_distance;
                    need_output.rob_emotion = need_lists[j].robot_emotion_str;//TODO: need_lists[i].rob_emotion;
                    need_output.rob_emotion_intensity = need_lists[j].robot_emotion_intensity;
                    need_output.person_emotion = need_lists[j].person_emotion;//need_lists[i].person_emotion
                    need_output.weight = need_lists[j].weight;
                    need_output.speech = need_lists[j].speech;
                    need_output.qt_order = period_cur;
                    need_output.satisfy_value = need_lists[j].satisfy_value;
                    if (result != NULL)
                    {
                        if( need_output.person_name ==  result->person_name &&
                            need_output.IDtype      ==  result->IDtype &&
                            need_output.need_name   ==  result->motivation
                         ){
                            ROS_INFO("Received right social attitude");
                            need_output.attitude    = result->attitude;
                            need_output.move_speed  = result->move_speed;
                            need_output.distance   = result->distance;
                            need_output.voice_speed = result->voice_speed;
                        }
                        else{
                            ROS_INFO("Received wrong social attitude");
                            need_output.attitude    = "enthusiastic";   //enthusiastic,respectful,serious,disgust
                            need_output.move_speed  = 1.0;
                            need_output.distance    = 1.0;
                            need_output.voice_speed = 1.0;
                        }
                    }
                    else
                    {
                        ROS_WARN("Timeout: Failed to receive social attitude within %f seconds", t);
                        need_output.attitude    = "enthusiastic";   //enthusiastic,respectful,serious,disgust
                        need_output.move_speed  = 1.0;
                        need_output.distance    = 1.0;
                        need_output.voice_speed = 1.0;
                    }   
                    pub.publish(need_output);
                    // printf( GREEN "    QT_order: %d:\n"NONE, need_output.qt_order); 
                    // sleep(0.1); // TODO: 重要。

                    std::cout <<  "[Output Need] " << j+1 << ": " << need_output.need_name << " ,Weight: " <<need_output.weight;
                    if (  need_output.person_name != "")
                        std::cout <<" ,for " <<need_output.person_name<<" as " <<need_output.IDtype;
                    std::cout<<std::endl;
                }
        
            period_cur++;     
    // cout<< "End PriorNeed !!\n";
}




int main(int argc, char** argv){
    // 是否实时输出需求模块的状态，默认不输出
    if(argc == 2){
        single_attitude = argv[1];
    }
        

    // ROS
    ros::init(argc, argv, "need_module");
    ros::NodeHandle n;
    cout<< "Need Module Start to Subscribe（接收ROS信息） !!\n";
    
    
    ros::spinOnce();
    
    if(single_attitude)
    {
        // 社交态度查询
        query_attitude = n.advertise<social_msg::attitude_query>("attitude_query", 1);  

        // 控制需求先验模型的运行周期
        ros::Rate loop_rate(0.35);  //5s一次

        // 为需求模型的运行  创建单独的线程 。  
        cout<< "Wait to run PriorNeed !!\n";
        while(ros::ok){
            if( ros::isShuttingDown() )
                break;
            single_need_test(&n);
            ros::spinOnce();
            loop_rate.sleep();
        }
    }
    else{
        
    }
    
    return 0;
}


