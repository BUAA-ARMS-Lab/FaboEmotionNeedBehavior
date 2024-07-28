#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import rospy
import os
from std_msgs.msg import Header
from sensor_msgs.msg import CompressedImage
import cv2
import numpy as np
import time
from cv_bridge import CvBridge
IMAGE_WIDTH=1280
IMAGE_HEIGHT=720

rospy.init_node('Image_talker', anonymous=True)
pub = rospy.Publisher('emotion_img', CompressedImage, queue_size=1)
rate = rospy.Rate(3) # 1hz

def publish_image(imgdata):
    while not rospy.is_shutdown():
        image_temp=CompressedImage()
        header = Header(stamp=rospy.Time.now())
        header.frame_id = 'map'
        image_temp.height=IMAGE_HEIGHT
        image_temp.width=IMAGE_WIDTH
        image_temp.encoding='rgb8'
        image_temp.data=np.array(imgdata).tostring()
        #print(imgdata)
        #image_temp.is_bigendian=True
        image_temp.header=header
        image_temp.step=1241*3
        pub.publish(image_temp)
        rospy.loginfo("图片成功发布")
        rate.sleep()

def publish_image2(imgdata):
    while not rospy.is_shutdown():
        current_folder = os.path.dirname(os.path.abspath(__file__))
        print("Current folder:", current_folder)
        imgdata=cv2.imread('/home/peng/codes/project3_ws/src/FaboEmotionNeedBehavior/emotion_module/image/emotion_img.png')  
        # print("width:%d",imgdata.shape[1])
        # print("height:%d",imgdata.shape[0])
        if imgdata is not None:
            imgdata = imgdata[0:720,280:1000]    
            # print("width2:%d",imgdata.shape[1])
            # print("height2:%d",imgdata.shape[0])
            image_temp=CvBridge().cv2_to_compressed_imgmsg(imgdata,'jpg')
            pub.publish(image_temp)
            rospy.loginfo("图片成功发布")
        rate.sleep()

if __name__ == '__main__':
    try:
         # img=cv2.imread('/home/zhjd/ws_social_project/src/FaboEmotionNeedBehavior/emotion_module/image/emotion_img.png')
        current_folder = os.path.dirname(os.path.abspath(__file__))
        print("Current folder:", current_folder)
        img=cv2.imread('/home/peng/codes/project3_ws/src/FaboEmotionNeedBehavior/emotion_module/image/emotion_img.png')
        publish_image2(img)
    except rospy.ROSInterruptException:
        pass




