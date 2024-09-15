from launch import LaunchDescription
from launch_ros.actions import Node # type: ignore
from launch.actions import DeclareLaunchArgument # type: ignore
from launch.substitutions import LaunchConfiguration # type: ignore

def generate_launch_description():
    return LaunchDescription([

        DeclareLaunchArgument(
            name='log_level', 
            default_value='INFO', 
            choices=['DEBUG','INFO','WARN','ERROR','FATAL'],
            description='Flag to set log level'
        ),

        Node(
            name='meu_no',
            package='meu_pacote',
            executable='meu_no',
            arguments=['--ros-args', '--log-level', LaunchConfiguration('log_level')]
        ),

        Node(
            name='meu_segundo_no',
            package='meu_pacote',
            executable='meu_segundo_no',
            arguments=['--ros-args', '--log-level', LaunchConfiguration('log_level')]
        ),
    ])
