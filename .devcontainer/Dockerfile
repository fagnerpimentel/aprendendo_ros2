ARG ROS_DISTRO
ARG DEBIAN_FRONTEND=noninteractive 

FROM osrf/ros:${ROS_DISTRO}-desktop-full

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
RUN mkdir /home/robot/workspace
WORKDIR /home/robot/workspace


# instala dependências do projeto  
# RUN cp /etc/apt/trusted.gpg /etc/apt/trusted.gpg.d
RUN apt update --fix-missing
RUN apt install -y --no-install-recommends apt-utils
RUN apt install -y --no-install-recommends git
RUN apt install -y --no-install-recommends wget
RUN apt install -y --no-install-recommends gpg
RUN apt install -y --no-install-recommends tmux 
RUN apt install -y --no-install-recommends xterm 
RUN apt install -y --no-install-recommends xclip 
RUN apt install -y --no-install-recommends python3-pip 
RUN apt install -y --no-install-recommends python3-argcomplete 
RUN apt install -y --no-install-recommends python3-colcon-common-extensions 
RUN apt install -y --no-install-recommends libboost-system-dev 
RUN apt install -y --no-install-recommends build-essential
RUN apt install -y --no-install-recommends libudev-dev

RUN apt install -y --no-install-recommends ros-${ROS_DISTRO}-test-msgs
RUN apt install -y --no-install-recommends ros-${ROS_DISTRO}-gazebo-ros 
RUN apt install -y --no-install-recommends ros-${ROS_DISTRO}-gazebo-ros-pkgs 
RUN apt install -y --no-install-recommends ros-${ROS_DISTRO}-joint-state-publisher 
RUN apt install -y --no-install-recommends ros-${ROS_DISTRO}-joint-state-publisher-gui 
RUN apt install -y --no-install-recommends ros-${ROS_DISTRO}-robot-localization 
RUN apt install -y --no-install-recommends ros-${ROS_DISTRO}-slam-toolbox 
RUN apt install -y --no-install-recommends ros-${ROS_DISTRO}-cartographer
RUN apt install -y --no-install-recommends ros-${ROS_DISTRO}-cartographer-ros 
RUN apt install -y --no-install-recommends ros-${ROS_DISTRO}-navigation2 
RUN apt install -y --no-install-recommends ros-${ROS_DISTRO}-nav2-bringup 
RUN apt install -y --no-install-recommends ros-${ROS_DISTRO}-tf-transformations 

RUN apt install -y --no-install-recommends ros-${ROS_DISTRO}-turtlebot3
RUN apt install -y --no-install-recommends ros-${ROS_DISTRO}-turtlebot3-msgs
RUN apt install -y --no-install-recommends ros-${ROS_DISTRO}-turtlebot3-gazebo
RUN apt install -y --no-install-recommends ros-${ROS_DISTRO}-hls-lfcd-lds-driver
RUN apt install -y --no-install-recommends ros-${ROS_DISTRO}-dynamixel-sdk

# turtlebot update
# RUN wget https://raw.githubusercontent.com/ROBOTIS-GIT/turtlebot3/humble-devel/turtlebot3_navigation2/param/burger.yaml
RUN wget https://github.com/ROBOTIS-GIT/turtlebot3/blob/humble/turtlebot3_navigation2/param/burger.yaml
RUN mv burger.yaml /opt/ros/humble/share/turtlebot3_navigation2/param/

# vscode
RUN wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
RUN install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
RUN sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
RUN rm -f packages.microsoft.gpg
RUN apt update --fix-missing
RUN apt install apt-transport-https -y
RUN apt install -y code

RUN pip install setuptools==58.2.0
RUN pip install transforms3d
RUN pip install bresenham

# RUN apt install tigervnc-standalone-server
# RUN apt install xpra
# RUN pip install websockify
# RUN apt install novnc

# download modelos do gazebo 
# RUN git clone https://github.com/osrf/gazebo_models.git /home/robot/gazebo_models/

# USER robot


# ----------------------------------------------------------------
# docker build -t fagnerpimentel/aprendendo_ros2:latest .
# docker login -u "myusername" -p "mypassword" docker.io
# docker push fagnerpimentel/aprendendo_ros2:latest
