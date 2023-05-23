#!/bin/bash
# rode o comando 'apt-get update' antes de chamar esse script


apt-get install -y --no-install-recommends \
    apt-utils \
    xterm \
    tmux \
    xclip \
    python3-pip \
    ros-$ROS_DISTRO-xacro \
    ros-$ROS_DISTRO-gazebo-ros \
    ros-$ROS_DISTRO-gazebo-ros-pkgs \
    ros-$ROS_DISTRO-robot-localization \
    ros-$ROS_DISTRO-slam-toolbox \
    ros-$ROS_DISTRO-navigation2 \
    ros-$ROS_DISTRO-nav2-bringup

pip install setuptools==58.2.0

# config tmux
echo "unbind -n Tab"  >> ~/.tmux.conf
echo "set -g window-style        'fg=#ffffff,bg=#8445ca'"  >> ~/.tmux.conf
echo "set -g window-active-style 'fg=#ffffff,bg=#5e2b97'"  >> ~/.tmux.conf
echo "set-option -g default-shell '/bin/bash'"   >> ~/.tmux.conf
echo "run-shell '. /opt/ros/humble/setup.bash'"         >> ~/.tmux.conf
echo "set -g mouse on"                              >> ~/.tmux.conf 
echo "bind-key -n C-Left select-pane -L"            >> ~/.tmux.conf
echo "bind-key -n C-Right select-pane -R"           >> ~/.tmux.conf
echo "bind-key -n C-Up select-pane -U"              >> ~/.tmux.conf
echo "bind-key -n C-Down select-pane -D"            >> ~/.tmux.conf
echo "bind -n M-Right split-window -h"              >> ~/.tmux.conf
echo "bind -n M-Down split-window -v"               >> ~/.tmux.conf
echo "bind C-c run 'tmux save-buffer - | xclip -i -sel clipboard'"                      >> ~/.tmux.conf
echo "bind C-v run 'tmux set-buffer '$(xclip -o -sel clipboard)'; tmux paste-buffer'"   >> ~/.tmux.conf

