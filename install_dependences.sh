ros_version=$1

valid_ros_version=("kinetic" "melodic" "noetic")

# pip2 install pathlib jieba

pip install rospkg
# pip install PyQt5==5.10.1

if [[ "${valid_ros_version[@]}"  =~ $ros_version ]]; then
    echo "ros version \"$ros_version\" is valid"
    sudo apt-get install ros-$ros_version-moveit-core
    sudo apt-get install ros-$ros_version-moveit-visual-tools
    sudo apt-get install ros-$ros_version-moveit-ros-planning-interface
else
    echo "Error: ros version \"$ros_version\" is not valid"
    exit 1
fi


