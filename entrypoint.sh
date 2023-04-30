#!/bin/bash

# source no ROS2 do sistema e no Gazebo
source /opt/ros/${ROS_DISTRO}/setup.bash 
# source /usr/share/gazebo-11/setup.sh

# constroi a area de trabalho do ROS2
colcon build

# Source no ROS2 da area de trabalho
source install/setup.bash 

# gera a URDF do robô a partir do arquivo XACRO
# xacro install/myfirstrobot_description/share/myfirstrobot_description/config/robots/r2d2.urdf.xacro -o install/myfirstrobot_description/share/myfirstrobot_description/config/robots/r2d2.urdf

exec "$@"