#include "ros/ros.h"
#include "social_msg/need_msg.h"

ros::Publisher need_pub;



int main(int argc, char **argv)
{
        ros::init(argc, argv, "need_model_dynamic_reconfigure");
        ros::NodeHandle n;
        // 感知信息
        need_pub  = n.advertise<social_msg::need_msg>("/need_lists", 10);

        sleep(1);
        social_msg::need_msg msg;
        msg.need_name   = config.need_name;          // 需求类型
        msg.scene   = config.need_scene;                // 场景名称 (school, hospital, family)
        msg.person_name   = config.need_person_name;          // 用户姓名
        msg.IDtype   = config.need_IDtype;               // 用户身份
        msg.target_angle   = config.need_target_angle;        // 交互对象角度
        msg.target_distance   = config.need_target_distance;     // 交互对象距离
        msg.rob_emotion   = config.need_rob_emotion;         // 机器人情绪类型
        msg.rob_emotion_intensity   = config.need_rob_emotion_intensity;  // 机器人情绪强度
        msg.person_emotion   = config.need_person_emotion;       // 用户的心情
        msg.weight   = config.need_weight;              // 需求权重
        msg.speech   = config.need_speech;               // 回答文本[机器人回复的话]
        msg.qt_order   = config.need_qt_order ;             // qt显示界面中的索引
        msg.satisfy_value   = config.need_satisfy_value;          // 需求自我满足值[用于情感模块中的自我评价]
        msg.attitude   = config.need_attitude;             // (机器人对用户的)社交态度
        msg.move_speed   = config.need_move_speed;          // 移速
        msg.distance   = config.need_distance;            // 社交距离
        msg.voice_speed   = config.need_voice_speed;         // 语速

        need_pub.publish(msg);



        ros::spin();
        return 0;
}