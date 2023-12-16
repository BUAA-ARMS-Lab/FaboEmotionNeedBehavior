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
from social_msg.msg import behavior_msg
import sys
import os

# "/home/zhjd/ws/src/social_system/emotion_module/scripts/"+'emotion_param.csv'
# /home/zhjd/ws/src/social_system/emotion_module/scripts/"+'emotion_param.csv

# csv_name = "/home/zhjd/ws/src/social_system/need_module/script/"+'test(school).csv'
# csv_name = "/home/zhjd/ws/src/social_system/need_module/script/"+'test(school).csv'
# sys.stdout.write( '选择刺激输入源,【1】行为打断,【2】行为并行:  ' )
# str = input()
current_folder_path = os.path.dirname(os.path.abspath(__file__))
str = 1



def talker():
        rospy.init_node('need_publisher_for_behavior_inter', anonymous=True)
        pub_beh = rospy.Publisher('/BehaviorInstruction', behavior_msg, queue_size=10)
        # rate = rospy.Rate(5)
        # rate = rospy.Rate(0.08) # 10s发一次
        
        print(" ")
        print(" ")
        
        while not rospy.is_shutdown():
            beh = behavior_msg()

            print("测试煽动翅膀")
            beh.name = "Wing"  
            beh.scene = "hospital"               # 场景名称 (school, hospital, family)
            beh.total_phase = 1           # 行为总共包含的子行为数量
            beh.current_phase = 0        # 开始执行的子行为位置，如0表示从头开始执行
            beh.occupancy = [1,1,1,1,1]          # 执行器分配
            beh.target = "小明"             # 交互对象
            beh.target_angle = 30       # 交互对象角度
            beh.target_distance = 1000    # 交互对象距离
            # string speech              # 语音内容文本
            # string rob_emotion         # 机器人心情（与表情关联）
            # int8 rob_emotion_intensity # 机器人情绪强度
            # string attitude            # (机器人对用户的)社交态度
            # float64 move_speed         # 移速
            # float64 distance           # 社交距离
            # float64 voice_speed        # 语速

            pub_beh.publish(beh)
            time.sleep(15)     #TODO:   具体间隔时间待定
                        
                        
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass




