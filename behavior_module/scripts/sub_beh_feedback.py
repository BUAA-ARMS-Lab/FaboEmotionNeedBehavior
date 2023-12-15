#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#!/usr/bin/env python

import rospy
from std_msgs.msg import String 
from social_msg.msg import behavior_feedback_msg

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s' ,data)
    print(233)
    
def listener():
    rospy.init_node('listener', anonymous = True)
    rospy.Subscriber('/BehaviorFeedback', behavior_feedback_msg, callback)
    rospy.spin()
    
if __name__ == '__main__':
    listener()


