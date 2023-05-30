from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            name='no_simples',
            package='pacote_de_exemplos',
            executable='no_simples',
            output='log',
        ),
    ])
