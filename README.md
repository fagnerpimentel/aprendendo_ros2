# aprendendo_ros2

Compilando o workspace:
```bash
colcon build
```

Criando um Pacote:
```bash
cd src
ros2 pkg create meu_primeiro_pacote --build-type ament_python
cd ..

```

Executando um nó:
```bash
ros2 run meu_primeiro_pacote meu_primeiro_no

```

Executando um launch:
```bash
ros2 launch meu_primeiro_pacote meu_primeiro_launch.py

```
