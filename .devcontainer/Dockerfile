ARG ROS_DISTRO=humble
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
RUN mkdir /home/robot/ws_aprendendo_ros2
WORKDIR /home/robot/ws_aprendendo_ros2


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

RUN apt install -y --no-install-recommends ros-${ROS_DISTRO}-xacro 
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
RUN wget https://raw.githubusercontent.com/ROBOTIS-GIT/turtlebot3/humble-devel/turtlebot3_navigation2/param/burger.yaml
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

# download modelos do gazebo 
# RUN git clone https://github.com/osrf/gazebo_models.git /home/robot/gazebo_models/

# comandos carregados na inicialização dos containers
RUN cd / && touch entrypoint.sh
RUN echo "#!/bin/bash"                                  >> /entrypoint.sh
# RUN echo "source /opt/ros/\${ROS_DISTRO}/setup.bash"    >> /entrypoint.sh
# RUN echo "colcon build --symlink-install"               >> /entrypoint.sh
# RUN echo "source install/setup.bash"                    >> /entrypoint.sh
# RUN echo "exec \"\$@\""                                 >> /entrypoint.sh
RUN echo "code serve-web --host 0.0.0.0 --port 80 --without-connection-token --accept-server-license-terms" >> /entrypoint.sh
# RUN echo "vncserver -geometry 1280x1024 -depth 24" >> /entrypoint.sh
# RUN echo "xpra start :100 --start-child=xterm" >> /entrypoint.sh

# RUN echo "websockify --web=/usr/share/novnc 6080 localhost:5901" >> /entrypoint.sh
# RUN echo "novnc --vnc localhost:5901" >> /entrypoint.sh


RUN chmod +x /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]



# USER robot


# ----------------------------------------------------------------
# docker build -t fagnerpimentel/aprendendo_ros2:latest .
# docker login -u "myusername" -p "mypassword" docker.io
# docker push fagnerpimentel/aprendendo_ros2:latest