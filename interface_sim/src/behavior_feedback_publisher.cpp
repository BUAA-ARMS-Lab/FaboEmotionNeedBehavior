#include "ros/ros.h"
#include <dynamic_reconfigure/server.h>
#include <interface_sim/behavior_feedback_publisherConfig.h>
#include "social_msg/behavior_feedback_msg.h"
ros::Publisher pub_behavior_feedback;

void callback(behavior_feedback_publisher::behavior_feedback_publisherConfig &config, uint32_t level)
{
    if(config.publish == true)
    {
        social_msg::behavior_feedback_msg msg;
        msg.header.seq = config.header_seq;
        msg.header.stamp.sec = config.header_time_sec;
        msg.header.stamp.nsec = config.header_time_nsec;
        msg.header.frame_id = config.header_frame_id;
        msg.hehavior_name = config.hehavior_name;
        msg.total_phase = config.total_phase;
        msg.current_phase = config.current_phase;

        pub_behavior_feedback.publish(msg);
    }
}

int main(int argc, char **argv)
{
        ros::init(argc, argv, "need_model_dynamic_reconfigure");
        ros::NodeHandle n;
        // 感知信息
        pub_behavior_feedback  = n.advertise<social_msg::behavior_feedback_msg>("/BehaviorFeedback", 10);

        dynamic_reconfigure::Server<behavior_feedback_publisher::behavior_feedback_publisherConfig> server;
        dynamic_reconfigure::Server<behavior_feedback_publisher::behavior_feedback_publisherConfig>::CallbackType f;
        sleep(2);
        f = boost::bind(&callback, _1, _2);
        server.setCallback(f);
        ros::spin();
        return 0;
}