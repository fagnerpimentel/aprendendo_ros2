#!/bin/bash
# rode o comando 'apt-get update' antes de chamar esse script


apt-get install -y --no-install-recommends \
    apt-utils \
    xterm \
    tmux \
    python3-pip \
    ros-$ROS_DISTRO-xacro \
    ros-$ROS_DISTRO-gazebo-ros \
    ros-$ROS_DISTRO-gazebo-ros-pkgs 

pip install setuptools==58.2.0

# config tmux
echo "set -g window-style 'fg=#ffffff,bg=#5e2b97'"  >> ~/.tmux.conf
echo "set -g mouse on"                              >> ~/.tmux.conf 
echo "bind-key -n C-Left select-pane -L"            >> ~/.tmux.conf
echo "bind-key -n C-Right select-pane -R"           >> ~/.tmux.conf
echo "bind-key -n C-Up select-pane -U"              >> ~/.tmux.conf
echo "bind-key -n C-Down select-pane -D"            >> ~/.tmux.conf
echo "bind -n M-Right split-window -h"              >> ~/.tmux.conf
echo "bind -n M-Down split-window -v"               >> ~/.tmux.conf
