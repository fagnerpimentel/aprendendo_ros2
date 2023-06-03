
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, SetEnvironmentVariable
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    robot_model = SetEnvironmentVariable(
        name='TURTLEBOT3_MODEL', value='waffle'
    )

    gazebo_model = SetEnvironmentVariable(
        name='GAZEBO_MODEL_PATH', value=['$GAZEBO_MODEL_PATH:/opt/ros/humble/share/turtlebot3_gazebo/models:',get_package_share_directory('pacote_de_exemplos'),'/simulation/models']
    )

    tb3 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([get_package_share_directory('nav2_bringup'), '/launch/tb3_simulation_launch.py']),
        launch_arguments={
            'headless': 'False',
            # 'slam': 'True',
            'map': [get_package_share_directory('pacote_de_exemplos'),'/config/map/map.yaml'],
            'world': [get_package_share_directory('pacote_de_exemplos'), '/simulation/worlds/simple_room_with_fixed_boxes.world']
        }.items()
    )


    ld = LaunchDescription()
    ld.add_action(robot_model)
    ld.add_action(gazebo_model)
    ld.add_action(tb3)
    
    return ld