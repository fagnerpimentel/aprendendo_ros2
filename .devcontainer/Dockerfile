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
RUN apt install -y --no-install-recommends ros-${ROS_DISTRO}-ros-gz
RUN apt install -y --no-install-recommends ros-${ROS_DISTRO}-gz-ros2-control
RUN apt install -y --no-install-recommends ros-${ROS_DISTRO}-ros2-controllers
RUN apt install -y --no-install-recommends ros-${ROS_DISTRO}-ros2controlcli
RUN apt install -y --no-install-recommends ros-${ROS_DISTRO}-joint-state-publisher 
RUN apt install -y --no-install-recommends ros-${ROS_DISTRO}-joint-state-publisher-gui 
RUN apt install -y --no-install-recommends ros-${ROS_DISTRO}-robot-localization 
RUN apt install -y --no-install-recommends ros-${ROS_DISTRO}-slam-toolbox 
RUN apt install -y --no-install-recommends ros-${ROS_DISTRO}-cartographer
RUN apt install -y --no-install-recommends ros-${ROS_DISTRO}-cartographer-ros 
RUN apt install -y --no-install-recommends ros-${ROS_DISTRO}-navigation2 
RUN apt install -y --no-install-recommends ros-${ROS_DISTRO}-nav2-bringup 
RUN apt install -y --no-install-recommends ros-${ROS_DISTRO}-tf-transformations
RUN apt install -y --no-install-recommends ros-${ROS_DISTRO}-realsense2-description

# RUN pip install setuptools==58.2.0
# RUN pip install transforms3d
# RUN pip install bresenham

# download modelos do gazebo 
# RUN git clone https://github.com/osrf/gazebo_models.git /home/robot/gazebo_models/

# USER robot


# ----------------------------------------------------------------
# docker build -t fagnerpimentel/aprendendo_ros2:latest .
# docker login -u "myusername" -p "mypassword" docker.io
# docker push fagnerpimentel/aprendendo_ros2:latest
