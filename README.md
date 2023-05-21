# aprendendo_ros2

Compilando o ambiente ROS
```bash
docker-compose build # use esse comando se você estiver rodando no linux
docker compose build # use esse comando se você estiver rodando no windows
```

Rodando o ambiente ROS
```bash
docker-compose up terminal # use esse comando se você estiver rodando no linux
docker compose up terminal # use esse comando se você estiver rodando no windows
```
---
Os próximos comandos são executados dentro do Docker

Compilando o workspace:
```bash
colcon build
```

Criando um Pacote:<br>
ex:
```bash
cd src
ros2 pkg create meu_primeiro_pacote --build-type ament_python
cd ..

```

Executando um nó:<br>
ex:
```bash
ros2 run meu_primeiro_pacote meu_primeiro_no

```

Executando um launch:<br>
ex:
```bash
ros2 launch meu_primeiro_pacote meu_primeiro_launch.py

```

Inicializando o Gazebo
```bash
ros2 launch gazebo_ros gazebo.launch.py
```
