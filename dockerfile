FROM osrf/ros:humble-desktop-full
ARG ROS_DISTRO=humble
ARG DEBIAN_FRONTEND=noninteractive 

# User: robot (password: robot) with sudo power
ARG UID=1000
ARG GID=1000
RUN useradd -ms /bin/bash robot && echo "robot:robot" | chpasswd && adduser robot sudo
RUN usermod -u $UID robot && groupmod -g $GID robot
# USER robot
# USER root

# Muda o terminal shell para bash
SHELL [ "/bin/bash" , "-c"]

# cria e determina diretório da area de trabalho
RUN mkdir /home/robot/ws_aprendendo_ros2
COPY ./* /home/robot/ws_aprendendo_ros2/
WORKDIR /home/robot/ws_aprendendo_ros2

# instala dependências do projeto  
RUN cp /etc/apt/trusted.gpg /etc/apt/trusted.gpg.d
RUN apt-get update
RUN ./instalar_dependencias.sh

# comandos carregados na inicialização dos containers
RUN /home/robot/ws_aprendendo_ros2/entrypoint.sh
ENTRYPOINT [ "/home/robot/ws_aprendendo_ros2/entrypoint.sh" ]

USER robot
