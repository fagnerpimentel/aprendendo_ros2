# aprendendo_ros2
## Os próximos comandos são executados fora do Docker


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

---
## Usando o ambiente

Inicializando o simulador
```bash
ros2 launch gazebo_ros gazebo.launch.py
```

---
## Para rodar a Hera:

```bash
source install/setup.bash
ros2 launch gazebo_ros gazebo.launch.py
ros2 launch hera_description load_description.launch.py
```
