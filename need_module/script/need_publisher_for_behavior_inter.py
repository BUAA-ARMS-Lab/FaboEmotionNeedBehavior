#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from re import I
import numpy as np
import math
from bisect import bisect_left
import pandas as pd
import csv
import rospy
import time
import threading
from social_msg.msg import attitude_msg
from social_msg.msg import perception_msg
from social_msg.msg import robot_emotion
from social_msg.msg import need_msg
import sys
import os

# "/home/zhjd/ws/src/social_system/emotion_module/scripts/"+'emotion_param.csv'
# /home/zhjd/ws/src/social_system/emotion_module/scripts/"+'emotion_param.csv

# csv_name = "/home/zhjd/ws/src/social_system/need_module/script/"+'test(school).csv'
# csv_name = "/home/zhjd/ws/src/social_system/need_module/script/"+'test(school).csv'
sys.stdout.write( '选择刺激输入源,【1】行为打断,【2】行为并行:  ' )
str = input();
current_folder_path = os.path.dirname(os.path.abspath(__file__))




def talker():
        rospy.init_node('need_publisher_for_behavior_inter', anonymous=True)
        pub_need = rospy.Publisher('/need_lists', need_msg, queue_size=10)
        # rate = rospy.Rate(5)
        rate = rospy.Rate(0.08) # 10s发一次
        
        print(" ")
        print(" ")

        if str == 1 :
                time.sleep(1)     
                need = need_msg()

                print("发送对小明的测温需求")
                need.need_name = "MeasureTemperature"  
                need.scene = "school"
                need.person_name = "小明"
                need.IDtype = "学生"
                need.target_angle = 0
                need.target_distance = 1000
                need.rob_emotion = "Joy"
                need.rob_emotion_intensity = 1
                need.person_emotion = "Happy"   
                need.weight = 0.75
                need.speech = ""
                need.qt_order = 0
                need.satisfy_value = 2
                need.attitude = "热情"
                need.move_speed = 200
                need.distance = 700
                need.voice_speed = 50
                pub_need.publish(need)


                time.sleep(15)     #TODO:   具体间隔时间待定

                
                print("发送对小明的维持秩序需求")
                need.need_name = "KeepOrder"
                need.scene = "school"
                need.person_name = "小明"
                need.IDtype = "学生"
                need.target_angle = 0
                need.target_distance = 700
                need.rob_emotion = "Anger"
                need.rob_emotion_intensity = 1
                need.person_emotion = "Happy"   
                need.weight = 0.85 
                need.speech = "请站在原地不要动，小明。我没法测体温了"
                need.qt_order = 0
                need.satisfy_value = 2
                need.attitude = "热情"
                need.move_speed = 200
                need.distance = 1000
                need.voice_speed = 50
                pub_need.publish(need)


        

        if str == 2 :
                time.sleep(1)     
                need = need_msg()


                print("发送对小明的测温需求")
                need.need_name = "MeasureTemperature"  
                need.scene = "school"
                need.person_name = "小明"
                need.IDtype = "学生"
                need.target_angle = 0
                need.target_distance = 1000
                need.rob_emotion = "Joy"
                need.rob_emotion_intensity = 1
                need.person_emotion = "Happy"   
                need.weight = 0.75
                need.speech = ""
                need.qt_order = 0
                need.satisfy_value = 2
                need.attitude = "热情"
                need.move_speed = 200
                need.distance = 700
                need.voice_speed = 50
                pub_need.publish(need)


                time.sleep(15)     #TODO:   具体间隔时间待定

                
                print("发送对李老师的问好需求")
                need.need_name = "RespectGreet"
                need.scene = "school"
                need.person_name = "李老师"
                need.IDtype = "老师"
                need.target_angle = 30
                need.target_distance = 500
                need.rob_emotion = "Trust"
                need.rob_emotion_intensity = 1
                need.person_emotion = "Happy"   
                need.weight = 0.85 
                need.speech = "李老师早上好啊"
                need.qt_order = 0
                need.satisfy_value = 2
                need.attitude = "热情"
                need.move_speed = 200
                need.distance = 500
                need.voice_speed = 50
                pub_need.publish(need)

                        
                        
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass




