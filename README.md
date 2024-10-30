# aprendendo_ros2
## Os próximos comandos são executados fora do Docker

Rodando o ambiente ROS
```bash
cd .devcontainer
docker compose up
```
---
## Commandos úteis

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

Abrindo um terminal dentro do docker:<br>
ex:
```bash
docker exec -it ros_env bash

```