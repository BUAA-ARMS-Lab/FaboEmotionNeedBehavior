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
To control robot arms to do designed actions:
```bash
roslaunch arm_control arm_control.launch
```

To test behavior_module only:
```bash
rosrun behavior_module behavior_node
```


To test behavior_module and perform_module together, controling fabo by bluetooth:
```bash
roslaunch behavior_module bluetooth_demo.launch
```

Use the following to **publish different topics more easily**:
```bash
rosrun behavior_module talker.py
```

Emotion Module
```bash
rosrun emotion_module main.py
```

Need Module
```bash
rosrun need_module need_model
```

## Topic publish
手动发布"机器人闲置状态"
+ 发送“无后续行为”的闲置状态,从而使机器人在闲置30秒后,生成“无聊”的情绪。
    
    rostopic pub -1 /idleState social_msg/idleState "{idleState: true, hehavior_name: '', person_name: '', IDtype: '', target_angle: 0.0,   target_distance: 0.0, person_emotion: '', satisfy_value: 0}" 

+ 发送“测温”行为结束的闲置状态,从而生成Pass放行的入校的需求,同时机器人会因为完成了”测温行为“而生成“高兴”的情绪。
    
    rostopic pub -1 /idleState social_msg/idleState "{idleState: false, hehavior_name: 'MeasureTempareture', person_name: 'xiaoming', IDtype: 'Student', target_angle: 0.0, target_distance: 0.0, person_emotion: 'happy', satisfy_value: 1}"