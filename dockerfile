FROM osrf/ros:humble-desktop-full
ARG ROS_DISTRO=humble
ARG DEBIAN_FRONTEND=noninteractive 

# # User: robot (password: robot) with sudo power
# ARG UID=1000
# ARG GID=1000
# RUN useradd -ms /bin/bash robot && echo "robot:robot" | chpasswd && adduser robot sudo
# RUN usermod -u $UID robot && groupmod -g $GID robot
# # USER robot
# # USER root
RUN mkdir /home/robot

# Muda o terminal shell para bash
SHELL [ "/bin/bash" , "-c"]

# cria e determina diretório da area de trabalho
RUN mkdir /home/robot/ws_aprendendo_ros2
WORKDIR /home/robot/ws_aprendendo_ros2


# instala dependências do projeto  
RUN cp /etc/apt/trusted.gpg /etc/apt/trusted.gpg.d
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    apt-utils \
    git \
    tmux \
    xterm \
    xclip \
    python3-pip \
    ros-$ROS_DISTRO-xacro \
    ros-$ROS_DISTRO-gazebo-ros \
    ros-$ROS_DISTRO-gazebo-ros-pkgs \
    ros-$ROS_DISTRO-joint-state-publisher \
    ros-$ROS_DISTRO-joint-state-publisher-gui \
    ros-$ROS_DISTRO-robot-localization \
    ros-$ROS_DISTRO-slam-toolbox \
    ros-$ROS_DISTRO-cartographer-ros \
    ros-$ROS_DISTRO-navigation2 \
    ros-$ROS_DISTRO-nav2-bringup \
    ros-$ROS_DISTRO-tf-transformations 
    # ros-$ROS_DISTRO-turtlebot3*

RUN pip install setuptools==58.2.0
RUN pip install transforms3d

# config tmux
RUN echo "unbind -n Tab"                                                                    >> ~/.tmux.conf
RUN echo "set -g window-style        'fg=#ffffff,bg=#8445ca'"                               >> ~/.tmux.conf
RUN echo "set -g window-active-style 'fg=#ffffff,bg=#5e2b97'"                               >> ~/.tmux.conf
RUN echo "set-option -g default-shell '/bin/bash'"                                          >> ~/.tmux.conf
RUN echo "run-shell '. /opt/ros/humble/setup.bash'"                                         >> ~/.tmux.conf
RUN echo "set -g mouse on"                                                                  >> ~/.tmux.conf 
RUN echo "bind-key -n C-Left select-pane -L"                                                >> ~/.tmux.conf
RUN echo "bind-key -n C-Right select-pane -R"                                               >> ~/.tmux.conf
RUN echo "bind-key -n C-Up select-pane -U"                                                  >> ~/.tmux.conf
RUN echo "bind-key -n C-Down select-pane -D"                                                >> ~/.tmux.conf
RUN echo "bind -n M-Right split-window -h"                                                  >> ~/.tmux.conf
RUN echo "bind -n M-Down split-window -v"                                                   >> ~/.tmux.conf
# RUN echo "bind C-c run 'tmux save-buffer - | xclip -i -sel clipboard'"                      >> ~/.tmux.conf
# RUN echo "bind C-v run 'tmux set-buffer '\$(xclip -o -sel clipboard)'; tmux paste-buffer'"   >> ~/.tmux.conf

# download modelos do gazebo 
# RUN git clone https://github.com/osrf/gazebo_models.git /home/robot/gazebo_models/

# comandos carregados na inicialização dos containers
# RUN touch entrypoint.sh
# RUN echo "#!/bin/bash"                                  >> entrypoint.sh
# RUN echo "source /opt/ros/\${ROS_DISTRO}/setup.bash"    >> entrypoint.sh
# RUN echo "colcon build --symlink-install"               >> entrypoint.sh
# RUN echo "source install/setup.bash"                    >> entrypoint.sh
# RUN echo "exec \"\$@\""                                   >> entrypoint.sh
# RUN chmod +x entrypoint.sh
# ENTRYPOINT [ "/home/robot/ws_aprendendo_ros2/entrypoint.sh" ]

# USER robot




# ----------------------------------------------------------------
# docker build -t fagnerpimentel/aprendendo_ros2:latest .
# docker login -u "myusername" -p "mypassword" docker.io
# docker push fagnerpimentel/aprendendo_ros2:latest