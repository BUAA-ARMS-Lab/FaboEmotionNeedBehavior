#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import rospy
import time
import random
from social_msg.msg import perception_msg, feedback_msg, behavior_msg

# float64 time            # 时间戳
# string person_name      # 用户的名字
# string IDtype           # 用户的身份
# string scene            # 场景名称 (school, hospital, family)
# float64 target_angle    # 交互对象角度
# float64 target_distance # 交互对象距离
# string intention        # 用户的top1意图
# float64 p               # 用户的top1意图识别概率
# string intention_2      # 用户的top2意图[可以赋空值]
# float64 p_2             # 用户的top2意图识别概率[可以赋空值]
# # string intention_3      # 用户的top2意图[可以赋空值]
# # float64 p_3             # 用户的top2意图识别概率[可以赋空值]
# string person_speech    # 用户问题文本说的话说的话[用户说的话]
# string speech           # 回答文本[机器人回复的话]
# string person_emotion   # 用户的心情
# string person_name
# string IDtype
# string motivation
# int8 emotional_feedback
# int8 language_feedback

distance = 800

def perception_talker(n):
  global distance

  if n==1:
    # time.sleep(2)
    feedback = feedback_msg()
    feedback.person_name = "小明"
    feedback.IDtype = "孩子"
    feedback.motivation = "WarmGreet"
    feedback.emotional_feedback = 1
    feedback.language_feedback = 0
    pub_fb.publish(feedback)
    perc = perception_msg()
    perc.time = rospy.get_time()
    perc.person_name ="小明"
    perc.IDtype = "孩子"
    perc.scene = "family"
    random_angle = random.randint(-1,1)
    perc.target_angle = 12
    random_distance = random.randint(-100,100)
    perc.target_distance = 1600 + random_distance
    perc.intention = "人机交互"
    perc.p = 0.9
    perc.intention_2 = ""
    perc.p_2 = 0
    perc.person_speech = "你好小胖!"
    perc.speech = "你好啊。小明"
    perc.person_emotion = "happy"
    pub_per.publish(perc)
    rospy.loginfo("  发布的消息%d: %f,%s,%s,%s",n,perc.time,perc.person_name,perc.speech,perc.person_emotion)

    # rospy.spin()
   

  elif n==2:
    # time.sleep(10)
    perc = perception_msg()
    perc.time = rospy.get_time()
    perc.person_name ="小明"
    perc.IDtype = "孩子"
    perc.scene = "family"
    random_angle = random.randint(-5,5)
    perc.target_angle = 0 + random_angle
    random_distance = random.randint(-20,30)
    distance = 800 + random_distance
    perc.target_distance = distance
    perc.intention = "问询"
    perc.p = 0.88
    perc.intention_2 = ""
    perc.p_2 = 0
    perc.person_speech = "小胖我想和你玩算数游戏!"
    perc.speech = "请先选择您想要进行的游戏难度，分为难度一到难度五。"
    perc.person_emotion = "happy"
    pub_per.publish(perc)
    rospy.loginfo("  发布的消息%d: %f,%s,%s,%s",n,perc.time,perc.person_name,perc.speech,perc.person_emotion)
    feedback = feedback_msg()
    feedback.person_name = "小明"
    feedback.IDtype = "孩子"
    feedback.motivation = "Answer"
    feedback.emotional_feedback = 1
    feedback.language_feedback = 0
    pub_fb.publish(feedback)


  elif n==3:
    # time.sleep(16)
    perc = perception_msg()
    perc.time = rospy.get_time()
    perc.person_name ="小明"
    perc.IDtype = "孩子"  
    perc.scene = "family"
    random_angle = random.randint(-7,7)
    random_distance = random.randint(-50,50)
    perc.target_angle = 0 + random_angle
    perc.target_distance = 800 + random_distance
    perc.intention = "问询"
    perc.p = 0.91
    perc.intention_2 = ""
    perc.p_2 = 0
    perc.person_speech = "难度三"
    perc.speech = "您好！本次的题目是,10加7减3,请您在十秒钟内做出回答："
    perc.person_emotion = "normal"
    pub_per.publish(perc)
    rospy.loginfo("  发布的消息%d: %f,%s,%s,%s",n,perc.time,perc.person_name,perc.speech,perc.person_emotion)
    feedback = feedback_msg()
    feedback.person_name = "小明"
    feedback.IDtype = "孩子"
    feedback.motivation = "Answer"
    feedback.emotional_feedback = 2
    feedback.language_feedback = 0
    pub_fb.publish(feedback)

  elif n==4:
    # time.sleep(16)
    perc = perception_msg()
    perc.time = rospy.get_time()
    perc.person_name ="小明"
    perc.IDtype = "孩子"
    perc.scene = "family"
    random_angle = random.randint(-7,7)
    random_distance = random.randint(-50,50)
    perc.target_angle = 0 + random_angle
    perc.target_distance = 800 + random_distance
    perc.intention = "问询"
    perc.p = 0.88
    perc.intention_2 = ""
    perc.p_2 = 0
    perc.person_speech = "答案是5"
    perc.speech = "很遗憾，您没有回答正确，需要降低难度吗"
    perc.person_emotion = "normal"
    pub_per.publish(perc)
    rospy.loginfo("  发布的消息%d: %f,%s,%s,%s",n,perc.time,perc.person_name,perc.speech,perc.person_emotion)
    feedback = feedback_msg()
    feedback.person_name = "小明"
    feedback.IDtype = "孩子"
    feedback.motivation = "Answer"
    feedback.emotional_feedback = 2
    feedback.language_feedback = 0
    pub_fb.publish(feedback)
    
  elif n==5:
    # time.sleep(16)
    perc = perception_msg()
    perc.time = rospy.get_time()
    perc.person_name ="小明"
    perc.IDtype = "孩子"
    perc.scene = "family"
    random_angle = random.randint(-7,7)
    random_distance = random.randint(-50,50)
    perc.target_angle = 0 + random_angle
    perc.target_distance = 820 + random_distance
    perc.intention = "问询"
    perc.p = 0.88
    perc.intention_2 = ""
    perc.p_2 = 0
    perc.person_speech = "太难了，降低难度"
    perc.speech = "好的，已经为您降低了难度，目前是难度二，您准备好开始了吗"
    perc.person_emotion = "normal"
    pub_per.publish(perc)
    rospy.loginfo("  发布的消息%d: %f,%s,%s,%s",n,perc.time,perc.person_name,perc.speech,perc.person_emotion)
    feedback = feedback_msg()
    feedback.person_name = "小明"
    feedback.IDtype = "孩子"
    feedback.motivation = "Answer"
    feedback.emotional_feedback = 2
    feedback.language_feedback = 0
    pub_fb.publish(feedback)

  elif n==6:
    # time.sleep(16)
    perc = perception_msg()
    perc.time = rospy.get_time()
    perc.person_name ="小明"
    perc.IDtype = "孩子"
    perc.scene = "family"
    random_angle = random.randint(-7,7)
    random_distance = random.randint(-50,50)
    perc.target_angle = 0 + random_angle
    perc.target_distance = 820 + random_distance
    perc.intention = "问询"
    perc.p = 0.88
    perc.intention_2 = ""
    perc.p_2 = 0
    perc.person_speech = "准备好了"
    perc.speech = "您好！本次的题目是,4减2加1,请您在十秒钟内做出回答："
    perc.person_emotion = "normal"
    pub_per.publish(perc)
    rospy.loginfo("  发布的消息%d: %f,%s,%s,%s",n,perc.time,perc.person_name,perc.speech,perc.person_emotion)
    feedback = feedback_msg()
    feedback.person_name = "小明"
    feedback.IDtype = "孩子"
    feedback.motivation = "Answer"
    feedback.emotional_feedback = 2
    feedback.language_feedback = 0
    pub_fb.publish(feedback)

  elif n==7:
    # time.sleep(16)
    perc = perception_msg()
    perc.time = rospy.get_time()
    perc.person_name ="小明"
    perc.IDtype = "孩子"
    perc.scene = "family"
    random_angle = random.randint(-7,7)
    random_distance = random.randint(-50,50)
    perc.target_angle = 0 + random_angle
    perc.target_distance = 820 + random_distance
    perc.intention = "问询"
    perc.p = 0.88
    perc.intention_2 = ""
    perc.p_2 = 0
    perc.person_speech = "等于3"
    perc.speech = "恭喜您回答正确"
    perc.person_emotion = "normal"
    pub_per.publish(perc)
    rospy.loginfo("  发布的消息%d: %f,%s,%s,%s",n,perc.time,perc.person_name,perc.speech,perc.person_emotion)
    feedback = feedback_msg()
    feedback.person_name = "小明"
    feedback.IDtype = "孩子"
    feedback.motivation = "Answer"
    feedback.emotional_feedback = 2
    feedback.language_feedback = 0
    pub_fb.publish(feedback)

  elif n==8:
    # time.sleep(16)
    perc = perception_msg()
    perc.time = rospy.get_time()
    perc.person_name ="小明"
    perc.IDtype = "孩子"
    perc.scene = "family"
    random_angle = random.randint(-7,7)
    random_distance = random.randint(-50,50)
    perc.target_angle = 0 + random_angle
    perc.target_distance = 820 + random_distance
    perc.intention = "问询"
    perc.p = 0.88
    perc.intention_2 = ""
    perc.p_2 = 0
    perc.person_speech = "小胖，我不想玩了"
    perc.speech = "好的，再见，有什么问题你都可以随时问我哦"
    perc.person_emotion = "normal"
    pub_per.publish(perc)
    rospy.loginfo("  发布的消息%d: %f,%s,%s,%s",n,perc.time,perc.person_name,perc.speech,perc.person_emotion)
    feedback = feedback_msg()
    feedback.person_name = "小明"
    feedback.IDtype = "孩子"
    feedback.motivation = "Answer"
    feedback.emotional_feedback = 2
    feedback.language_feedback = 0
    pub_fb.publish(feedback)

  elif n==9:
    # time.sleep(16)
    perc = perception_msg()
    perc.time = rospy.get_time()
    perc.person_name ="陌生人"
    perc.IDtype = "陌生人"
    perc.scene = "family"
    random_angle = random.randint(-2,2)
    random_distance = random.randint(1,100)
    distance = 800 + random_distance
    perc.target_angle = -15
    perc.target_distance = distance
    perc.intention = "人机交互"
    perc.p = 0.88
    perc.intention_2 = ""
    perc.p_2 = 0
    perc.person_speech = "你好呀"
    perc.speech = "您好，我是智能机器人小胖！不好意思，我现在还不认识您，您需要先进行登记哦!请问您是现在进行登记吗？"
    perc.person_emotion = "normal"
    pub_per.publish(perc)
    rospy.loginfo("  发布的消息%d: %f,%s,%s,%s",n,perc.time,perc.person_name,perc.speech,perc.person_emotion)
    feedback = feedback_msg()
    feedback.person_name = "陌生人"
    feedback.IDtype = "陌生人"
    feedback.motivation = "RespectGreet"
    feedback.emotional_feedback = 2
    feedback.language_feedback = 0
    pub_fb.publish(feedback)

  elif n==10:
    distance += 400
    # time.sleep(20)
    perc = perception_msg()
    perc.time = rospy.get_time()
    perc.person_name ="陌生人"
    perc.IDtype = "陌生人"
    perc.scene = "family"
    random_angle = random.randint(-7,7)
    random_distance = random.randint(-50,50)
    perc.target_angle = 0 + random_angle
    perc.target_distance = 1250 + random_distance
    perc.intention = "问询"
    perc.p = 0.88
    perc.intention_2 = ""
    perc.p_2 = 0
    perc.person_speech = "是的，请帮我登记一下"
    perc.speech = "好的，请问您的名字是？"
    perc.person_emotion = "normal"
    pub_per.publish(perc)
    rospy.loginfo("  发布的消息%d: %f,%s,%s,%s",n,perc.time,perc.person_name,perc.speech,perc.person_emotion)
    feedback = feedback_msg()
    feedback.person_name = "陌生人"
    feedback.IDtype = "陌生人"
    feedback.motivation = "Answer"
    feedback.emotional_feedback = 2
    feedback.language_feedback = 0
    pub_fb.publish(feedback)

  elif n==11:
    # time.sleep(16)
    perc = perception_msg()
    perc.time = rospy.get_time()
    perc.person_name ="陈睿"
    perc.IDtype = "陌生人"
    perc.scene = "family"
    random_angle = random.randint(-7,7)
    random_distance = random.randint(-50,50)
    perc.target_angle = 0 + random_angle
    perc.target_distance = 1250 + random_distance
    perc.intention = "问询"
    perc.p = 0.88
    perc.intention_2 = ""
    perc.p_2 = 0
    perc.person_speech = "陈睿"
    perc.speech = "请问您的身份是？"
    perc.person_emotion = "normal"
    pub_per.publish(perc)
    rospy.loginfo("  发布的消息%d: %f,%s,%s,%s",n,perc.time,perc.person_name,perc.speech,perc.person_emotion)
    feedback = feedback_msg()
    feedback.person_name = "陈睿"
    feedback.IDtype = "陌生人"
    feedback.motivation = "Answer"
    feedback.emotional_feedback = 2
    feedback.language_feedback = 0
    pub_fb.publish(feedback)

  elif n==12:
    # time.sleep(16)
    perc = perception_msg()
    perc.time = rospy.get_time()
    perc.person_name ="陈睿"
    perc.IDtype = "小明的舅舅"
    perc.scene = "family"
    random_angle = random.randint(-7,7)
    random_distance = random.randint(-50,50)
    perc.target_angle = 0 + random_angle
    perc.target_distance = 1250 + random_distance
    perc.intention = "问询"
    perc.p = 0.88
    perc.intention_2 = ""
    perc.p_2 = 0
    perc.person_speech = "小明的舅舅"
    perc.speech = "好的，已经为您登记成功！您好，陈睿，请您先坐下休息一下吧"
    perc.person_emotion = "normal"
    pub_per.publish(perc)
    rospy.loginfo("  发布的消息%d: %f,%s,%s,%s",n,perc.time,perc.person_name,perc.speech,perc.person_emotion)
    feedback = feedback_msg()
    feedback.person_name = "陈睿"
    feedback.IDtype = "小明的舅舅"
    feedback.motivation = "Answer"
    feedback.emotional_feedback = 2
    feedback.language_feedback = 0
    pub_fb.publish(feedback)

  elif n==13:
    # time.sleep(16)
    perc = perception_msg()
    perc.time = rospy.get_time()
    perc.person_name ="陈睿"
    perc.IDtype = "小明的舅舅"
    perc.scene = "family"
    random_angle = random.randint(-7,7)
    random_distance = random.randint(-50,50)
    perc.target_angle = 0 + random_angle
    perc.target_distance = 1250 + random_distance
    perc.intention = "问询"
    perc.p = 0.88
    perc.intention_2 = ""
    perc.p_2 = 0
    perc.person_speech = "好的，谢谢"
    # perc.speech = "好的，再见，有什么问题你都可以随时问我哦"
    perc.speech = "好的，有什么问题你都可以随时问我哦。如果你要进家里，你还需要测下体温。"
    perc.person_emotion = "normal"
    pub_per.publish(perc)
    rospy.loginfo("  发布的消息%d: %f,%s,%s,%s",n,perc.time,perc.person_name,perc.speech,perc.person_emotion)
    feedback = feedback_msg()
    feedback.person_name = "陈睿"
    feedback.IDtype = "小明的舅舅"
    feedback.motivation = "Answer"
    feedback.emotional_feedback = 2
    feedback.language_feedback = 0
    pub_fb.publish(feedback)

  elif n==14:
    # time.sleep(16)
    perc = perception_msg()
    perc.time = rospy.get_time()
    perc.person_name ="陈睿"
    perc.IDtype = "小明的舅舅"
    perc.scene = "family"
    random_angle = random.randint(-7,7)
    random_distance = random.randint(-50,50)
    perc.target_angle = 0 + random_angle
    perc.target_distance = 1250 + random_distance
    perc.intention = "体温测量"
    perc.p = 0.88
    perc.intention_2 = ""
    perc.p_2 = 0
    perc.person_speech = "好的，那你帮我测下体温"
    perc.speech = ""
    perc.person_emotion = "normal"
    pub_per.publish(perc)
    rospy.loginfo("  发布的消息%d: %f,%s,%s,%s",n,perc.time,perc.person_name,perc.speech,perc.person_emotion)
    feedback = feedback_msg()
    feedback.person_name = "陈睿"
    feedback.IDtype = "小明的舅舅"
    feedback.motivation = "MeasureTemperature"
    feedback.emotional_feedback = 2
    feedback.language_feedback = 0
    pub_fb.publish(feedback)

  else:
    rospy.loginfo("  不存在或已结束，可以退出")


if __name__ == '__main__':
    try:
        rospy.init_node('perception_talker', anonymous=True)
        pub_per = rospy.Publisher('perception_msg', perception_msg, queue_size=10)
        pub_fb = rospy.Publisher('feedback_msg', feedback_msg, queue_size=10)
        pub_bi = rospy.Publisher('BehaviorInstruction', behavior_msg, queue_size=10)

        n = 0
        while not rospy.is_shutdown():
            key = input("请输入选项：")
            # key_num = int(key)
            if key.isdigit():
                msg = behavior_msg()
                msg.name = 'Stop_All_Actions_Now'
                msg.scene = 'family'
                msg.total_phase=0
                msg.current_phase=0
                msg.occupancy=[0,0,0,0,0]
                pub_bi.publish(msg)
                n=int(key)
                perception_talker(n)
            elif key=='y' or key=='Y' or key=='yy' or key=='YY':
                n=n+1
                perception_talker(n)
            elif key == 'q':
               break
            elif key == 'n' or key == 'N' or key == 'NN' or key == 'nn':
                msg = behavior_msg()
                msg.name = 'Stop_All_Actions_Now'
                msg.scene = 'family'
                msg.total_phase=0
                msg.current_phase=0
                msg.occupancy=[0,0,0,0,0]
                pub_bi.publish(msg)
                # time.sleep(0.5)
                perception_talker(n)
            # elif key == 'c':
            #     for i in range(1, 14):
            #         time.sleep(10)
            #         perception_talker(i)

            else:
               continue
               

    except rospy.ROSInterruptException:
        pass