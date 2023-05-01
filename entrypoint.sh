#!/bin/bash

# source no ROS2 do sistema
source /opt/ros/${ROS_DISTRO}/setup.bash 

# constroi a area de trabalho do ROS2
colcon build --symlink-install

# Source no ROS2 da area de trabalho
source install/setup.bash 

exec "$@"