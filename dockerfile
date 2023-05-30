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
RUN apt-get install -y --no-install-recommends apt-utils git
# RUN git clone https://github.com/osrf/gazebo_models.git /home/robot/gazebo_models/


COPY instalar_dependencias.sh .
RUN sed -i -e 's/\r$//' instalar_dependencias.sh
RUN ./instalar_dependencias.sh


# COPY src/hera_description src/hera_description
RUN git clone -b ros2 https://github.com/Home-Environment-Robot-Assistant/hera_description.git src/hera_description
RUN ./src/hera_description/install_dependencies.sh

# comandos carregados na inicialização dos containers
COPY entrypoint.sh .
RUN sed -i -e 's/\r$//' entrypoint.sh
RUN /home/robot/ws_aprendendo_ros2/entrypoint.sh
ENTRYPOINT [ "/home/robot/ws_aprendendo_ros2/entrypoint.sh" ]

# USER robot
