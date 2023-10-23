cmake_minimum_required(VERSION 3.0.2)
project(interface_sim)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  dynamic_reconfigure
  roscpp
  rospy
  std_msgs
  geometry_msgs
  message_generation
)

## DEPENDS: system dependencies of this project that dependent projects also need


include_directories(
 include
  ${catkin_INCLUDE_DIRS}
  ${CATKIN_DEVEL_PREFIX}/include/
)

#ros massage自定义
# add_message_files( FILES perception_msg.msg  need_msg.msg  robot_emotion.msg  robot_status.msg )
# generate_messages( DEPENDENCIES    roscpp  std_msgs geometry_msgs )


generate_dynamic_reconfigure_options(
    include/cfg.cfg
    include/behavior_feedback.cfg
    include/need.cfg
)
 
add_executable(robot_emotion_publisher src/robot_emotion_publisher.cpp)
add_dependencies(robot_emotion_publisher ${PROJECT_NAME}_gencfg)
target_link_libraries(robot_emotion_publisher ${catkin_LIBRARIES})

add_executable(behavior_feedback_publisher src/behavior_feedback_publisher.cpp)
add_dependencies(behavior_feedback_publisher ${PROJECT_NAME}_gencfg)
target_link_libraries(behavior_feedback_publisher ${catkin_LIBRARIES})

add_executable(need_publisher src/need_publisher.cpp)
add_dependencies(need_publisher ${PROJECT_NAME}_gencfg)
target_link_libraries(need_publisher ${catkin_LIBRARIES})