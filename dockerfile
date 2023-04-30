FROM osrf/ros:humble-desktop-full
ARG ROS_DISTRO=humble

ARG DEBIAN_FRONTEND=noninteractive 

# Muda o terminal shell para bash
SHELL [ "/bin/bash" , "-c"]

# cria e determina diretório da area de trabalho
RUN mkdir /ws_aprendendo_ros2
COPY ./* /ws_aprendendo_ros2/
WORKDIR /ws_aprendendo_ros2

# instala dependências do projeto  
RUN apt-get update
RUN ./instalar_dependencias.sh

# comandos carregados na inicialização dos containers
RUN ./entrypoint.sh
ENTRYPOINT [ "./entrypoint.sh" ]