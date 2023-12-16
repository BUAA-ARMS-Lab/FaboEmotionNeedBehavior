# FaboEmotionNeedBehavior
The emotion/need/behavior module of  Social Interaction Project, with a perform module for Research Group 3's internal testing

# Build
Build for the first time:
```bash
cd ~
mkdir -p social_interaction_ws/src
cd social_interaction_ws/src
git clone https://github.com/BUAA-ARMS-Lab/FaboEmotionNeedBehavior.git
catkin_init_workspace
cd ..
bash src/FaboEmotionNeedBehavior/build.sh
echo "source ~/social_interaction_ws/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

Build after building once:
```bash
catkin_make
```

# Usage
+ To control robot arms to do designed actions:
```bash
roslaunch arm_control arm_control.launch
```

+ To test behavior_module only:
```bash
rosrun behavior_module behavior_node
```


+ To test behavior_module and perform_module together, controling fabo by bluetooth:
```bash
roslaunch behavior_module bluetooth_demo.launch
```

+ Use the following to **publish different topics more easily**:
```bash
rosrun behavior_module talker.py
```

+ Emotion Module
```bash
rosrun emotion_module main.py
```

+ Need Module
```bash
rosrun need_module need_model
```
如果要开启需求模块的调试界面，可以输入参数 1
```bash
rosrun need_module need_model 1
```

+ 仿真接口: 
```bash
roslaunch interface_sim interface_sim_cfg.launch
```
1.   可以发送感知信息、社交态度、idleState等topic
2.   修改各topic的内容： 从“O_____”开头的选项向下代表一个topic，第一个“O_____”选项，用于开关是否发送此topic，之后的选项用于修改topic的内容。
3.   发送topic： 先通过点击“O_____”开关，选择要发送的topic；再点击第一行的“publish”，发送topic。

## Topic publish
手动发布"机器人闲置状态"
+ 发送“无后续行为”的闲置状态,从而使机器人在闲置30秒后,生成“无聊”的情绪。
    
    rostopic pub -1 /idleState social_msg/idleState "{idleState: true, hehavior_name: '', person_name: '', IDtype: '', target_angle: 0.0,   target_distance: 0.0, person_emotion: '', satisfy_value: 0}" 

+ 发送“测温”行为结束的闲置状态,从而生成Pass放行的入校的需求,同时机器人会因为完成了”测温行为“而生成“高兴”的情绪。
    
    rostopic pub -1 /idleState social_msg/idleState "{idleState: false, hehavior_name: 'MeasureTemperature', person_name: 'xiaoming', IDtype: 'Student', target_angle: 0.0, target_distance: 0.0, person_emotion: 'happy', satisfy_value: 1}"





    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
    git branch -m new_main_for_project2 main
    git fetch origin
    git branch -u origin/main main
    git remote set-head origin -a

rostopic pub /BehaviorInstruction social_msg/behavior_msg "header:
  seq: 0
  stamp: {secs: 0, nsecs: 0}
  frame_id: ''
name: 'Stop_All_Actions_Now'
scene: 'school'
type: ''
total_phase: 0
current_phase: 0
occupancy: [1, 1, 1, 1, 1]
target: ''
target_angle: 0.0
target_distance: 0.0
speech: ''
rob_emotion: ''
rob_emotion_intensity: 0
attitude: ''
move_speed: 0.0
distance: 0.0
voice_speed: 0.0" 



一、学校
（1）问好
rostopic pub /perception_msg social_msg/perception_msg "{time: 0.0, person_name: '王老师', IDtype: '老师', scene: 'school', target_angle: 20.0, target_distance: 1000.0,  intention: '人机交互', p: 1.0, intention_2: '', p_2: 0.0, person_speech: '', speech: '王老师早上好啊',  person_emotion: 'Happy'}" 



rostopic pub /perception_msg social_msg/perception_msg "{time: 0.0, person_name: '小明', IDtype: '学生', scene: 'school', target_angle: 20.0, target_distance: 1000.0,  intention: '人机交互', p: 1.0, intention_2: '', p_2: 0.0, person_speech: '', speech: '',  person_emotion: 'Happy'}" 


rostopic pub /perception_msg social_msg/perception_msg "{time: 0.0, person_name: '小明他爸', IDtype: '家长', scene: 'school', target_angle: 20.0, target_distance: 1000.0,  intention: '人机交互', p: 1.0, intention_2: '', p_2: 0.0, person_speech: '', speech: '',  person_emotion: 'Happy'}" 



rostopic pub /perception_msg social_msg/perception_msg "{time: 0.0, person_name: '路人甲', IDtype: '陌生人', scene: 'school', target_angle: 90.0, target_distance: 1000.0,  intention: '人机交互', p: 1.0, intention_2: '', p_2: 0.0, person_speech: '', speech: '你好啊，非校内人员进校要先登记和测量体温哦',  person_emotion: 'Happy'}" 



（2）问询
rostopic pub /perception_msg social_msg/perception_msg "{time: 0.0, person_name: '王老师', IDtype: '老师', scene: 'school', target_angle: 90.0, target_distance: 1000.0,  intention: '问询', p: 1.0, intention_2: '', p_2: 0.0, person_speech: '', speech: '抱歉，我也不知道呢',  person_emotion: 'Happy'}" 



rostopic pub /perception_msg social_msg/perception_msg "{time: 0.0, person_name: '小明', IDtype: '学生', scene: 'school', target_angle: -30.0, target_distance: 1000.0,  intention: '问询', p: 1.0, intention_2: '', p_2: 0.0, person_speech: '', speech: '抱歉，我也不知道呢',  person_emotion: 'Happy'}" 


rostopic pub /perception_msg social_msg/perception_msg "{time: 0.0, person_name: '小明他爸', IDtype: '家长', scene: 'school', target_angle: 0.0, target_distance: 1000.0,  intention: '问询', p: 1.0, intention_2: '', p_2: 0.0, person_speech: '', speech: '',  person_emotion: 'Happy'}" 



rostopic pub /perception_msg social_msg/perception_msg "{time: 0.0, person_name: '路人甲', IDtype: '陌生人', scene: 'school', target_angle: -40.0, target_distance: 1000.0,  intention: '问询', p: 1.0, intention_2: '', p_2: 0.0, person_speech: '', speech: '你好啊，非校内人员进校要先登记和测量体温哦',  person_emotion: 'Happy'}" 





（3）测体温
rostopic pub /perception_msg social_msg/perception_msg "{time: 0.0, person_name: '王老师', IDtype: '老师', scene: 'school', target_angle: 20.0, target_distance: 1000.0,  intention: '体温测量', p: 1.0, intention_2: '', p_2: 0.0, person_speech: '', speech: '',  person_emotion: 'Happy'}" 



rostopic pub /perception_msg social_msg/perception_msg "{time: 0.0, person_name: '小明', IDtype: '学生', scene: 'school', target_angle: -20.0, target_distance: 1000.0,  intention: '体温测量', p: 1.0, intention_2: '', p_2: 0.0, person_speech: '', speech: '',  person_emotion: 'Happy'}" 


rostopic pub /perception_msg social_msg/perception_msg "{time: 0.0, person_name: '小明他爸', IDtype: '家长', scene: 'school', target_angle: 0.0, target_distance: 1000.0,  intention: '体温测量', p: 1.0, intention_2: '', p_2: 0.0, person_speech: '', speech: '',  person_emotion: 'Happy'}" 



rostopic pub /perception_msg social_msg/perception_msg "{time: 0.0, person_name: '路人甲', IDtype: '陌生人', scene: 'school', target_angle: 90.0, target_distance: 1000.0,  intention: '体温测量', p: 1.0, intention_2: '', p_2: 0.0, person_speech: '', speech: '你好啊，非校内人员进校要先登记和测量体温哦',  person_emotion: 'Happy'}" 





（4）日常闲聊
rostopic pub /perception_msg social_msg/perception_msg "{time: 0.0, person_name: '王老师', IDtype: '老师', scene: 'school', target_angle: 0.0, target_distance: 0.0,  intention: '日常闲聊', p: 1.0, intention_2: '', p_2: 0.0, person_speech: '', speech: '工作期间不能跟你聊天哦',  person_emotion: 'Happy'}" 



rostopic pub /perception_msg social_msg/perception_msg "{time: 0.0, person_name: '小明', IDtype: '学生', scene: 'school', target_angle: 0.0, target_distance: 1000.0,  intention: '日常闲聊', p: 1.0, intention_2: '', p_2: 0.0, person_speech: '', speech: '工作期间不能跟你聊天哦',  person_emotion: 'Happy'}" 


rostopic pub /perception_msg social_msg/perception_msg "{time: 0.0, person_name: '小明他爸', IDtype: '家长', scene: 'school', target_angle: 0.0, target_distance: 1000.0,  intention: '日常闲聊', p: 1.0, intention_2: '', p_2: 0.0, person_speech: '', speech: '工作期间不能跟你聊天哦',  person_emotion: 'Happy'}" 



rostopic pub /perception_msg social_msg/perception_msg "{time: 0.0, person_name: '路人甲', IDtype: '陌生人', scene: 'school', target_angle: 0.0, target_distance: 1000.0,  intention: '日常闲聊', p: 1.0, intention_2: '', p_2: 0.0, person_speech: '', speech: '工作期间不能跟你聊天哦',  person_emotion: 'Happy'}" 






二、家庭
（1）人机交互


rostopic pub /perception_msg social_msg/perception_msg "{time: 0.0, person_name: '小明', IDtype: '孩子', scene: 'family', target_angle: 20.0, target_distance: 1000.0,  intention: '人机交互', p: 1.0, intention_2: '', p_2: 0.0, person_speech: '', speech: '',  person_emotion: 'Happy'}" 


rostopic pub /perception_msg social_msg/perception_msg "{time: 0.0, person_name: '小明他爸', IDtype: '家长', scene: 'family', target_angle: 20.0, target_distance: 1000.0,  intention: '人机交互', p: 1.0, intention_2: '', p_2: 0.0, person_speech: '', speech: '',  person_emotion: 'Happy'}" 





（2）问询
rostopic pub /perception_msg social_msg/perception_msg "{time: 0.0, person_name: '王老师', IDtype: '老师', scene: 'family', target_angle: 90.0, target_distance: 1000.0,  intention: '问询', p: 1.0, intention_2: '', p_2: 0.0, person_speech: '', speech: '抱歉，我也不知道呢',  person_emotion: 'Happy'}" 




rostopic pub /perception_msg social_msg/perception_msg "{time: 0.0, person_name: '小明他爸', IDtype: '家长', scene: 'family', target_angle: 0.0, target_distance: 1000.0,  intention: '问询', p: 1.0, intention_2: '', p_2: 0.0, person_speech: '', speech: '',  person_emotion: 'Happy'}" 





三、医院
（2）问询
rostopic pub /perception_msg social_msg/perception_msg "{time: 0.0, person_name: '王老师', IDtype: '病人', scene: 'hospital', target_angle: 0.0, target_distance: 1000.0,  intention: '问询', p: 1.0, intention_2: '', p_2: 0.0, person_speech: '', speech: '抱歉，我也不知道呢',  person_emotion: 'Happy'}" 



# hospital answer

rostopic pub /BehaviorInstruction social_msg/behavior_msg "header:
  seq: 0
  stamp: {secs: 10101010, nsecs: 0}
  frame_id: ''
name: 'Answer'
scene: 'hospital'
type: ''
total_phase: 2
current_phase: 0
occupancy: [1, 1, 1, 1, 1]
target: '小明'
target_angle: 0.0
target_distance: 1000.0
speech: '你好啊，你是生病了吗？'
rob_emotion: 'Calm'
rob_emotion_intensity: 1
attitude: '热情'
move_speed: 200.0
distance: 1000.0
voice_speed: 0.0"  -1



# Wander

rostopic pub /BehaviorInstruction social_msg/behavior_msg "header:
  seq: 0
  stamp: {secs: 0, nsecs: 0}
  frame_id: ''
name: 'Wander'
scene: 'school'
type: ''
total_phase: 8
current_phase:   0 
occupancy: [1, 1, 1, 1, 1]
target: ''
target_angle: 0.0
target_distance: 0.0
speech: '123456'
rob_emotion: ''
rob_emotion_intensity: 0
attitude: ''
move_speed: 200.0
distance: 1000.0
voice_speed: 0.0"  -1


# Stop_All_Actions_Now
rostopic pub /BehaviorInstruction social_msg/behavior_msg "header:
  seq: 0
  stamp: {secs: 0, nsecs: 0}
  frame_id: ''
name: 'Stop_All_Actions_Now'
scene: 'school'
type: ''
total_phase: 0
current_phase: 0
occupancy: [1, 1, 1, 1, 1]
target: ''
target_angle: 0.0
target_distance: 0.0
speech: ''
rob_emotion: ''
rob_emotion_intensity: 0
attitude: ''
move_speed: 0.0
distance: 0.0
voice_speed: 0.0"  -1


# WarmGreet

rostopic pub /BehaviorInstruction social_msg/behavior_msg "header:
  seq: 0
  stamp: {secs: 0, nsecs: 0}
  frame_id: ''
name: 'WarmGreet'
scene: 'school'
type: ''
total_phase: 3
current_phase:   0 
occupancy: [1, 1, 1, 1, 1]
target: ''
target_angle: 15.0
target_distance: 1000.0
speech: '小明你好阿'
rob_emotion: ''
rob_emotion_intensity: 0
attitude: ''
move_speed: 200.0
distance: 1000.0
voice_speed: 0.0"  -1

# Other Order
rosrun need_module need_model 1
rosrun behavior_module behavior_node
rostopic echo /BehaviorInstruction
rosrun behavior_module sub_beh_feedback.py
