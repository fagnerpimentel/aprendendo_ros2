#!/bin/bash

# rode o comando 'apt-get update' antes de chamar esse script
apt-get install -y --no-install-recommends \
    xterm \
    tmux \
    ros-$ROS_DISTRO-xacro

