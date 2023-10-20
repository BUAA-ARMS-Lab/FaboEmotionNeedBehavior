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
    
    rostopic pub -1 /idleState social_msg/idleState "{idleState: false, hehavior_name: 'MeasureTempareture', person_name: 'xiaoming', IDtype: 'Student', target_angle: 0.0, target_distance: 0.0, person_emotion: 'happy', satisfy_value: 1}"





    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