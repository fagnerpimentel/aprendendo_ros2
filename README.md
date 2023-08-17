# aprendendo_ros2
## Os próximos comandos são executados fora do Docker

Rodando o ambiente ROS
```bash
docker compose up ros-master
```
---
## Os próximos comandos são executados dentro do Docker


Compilando o workspace:<br>
```bash
colcon build
source install/setup.bash
```

Criando um Pacote:<br>
ex:
```bash
cd src
ros2 pkg create <nome_do_pacote> --build-type ament_python
# ex: ros2 pkg create meu_primeiro_pacote --build-type ament_python
cd ..

```

Executando um nó:<br>
ex:
```bash
ros2 run <nome_do_pacote> <nome_do_nó>
# ex: ros2 run meu_primeiro_pacote meu_primeiro_no

```

Executando um launch:<br>
ex:
```bash
ros2 launch <nome_do_pacote> <nome_do_nó>
# ex: ros2 launch meu_primeiro_pacote meu_primeiro_launch.py

```