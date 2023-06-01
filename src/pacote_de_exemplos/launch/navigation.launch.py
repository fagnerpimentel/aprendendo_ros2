from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node

def generate_launch_description():

    log_level = DeclareLaunchArgument(
        name='log_level', 
        default_value='INFO', 
        choices=['DEBUG','INFO','WARN','ERROR','FATAL'],
        description='Flag to set log level')


    simulation = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([get_package_share_directory('pacote_de_exemplos'), '/launch/simulation.launch.py']),
           launch_arguments={
                'world_path': [get_package_share_directory('pacote_de_exemplos'), '/simulation/worlds/simple_room_with_fixed_boxes.world'],
            }.items(),
    )

    robot = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([get_package_share_directory('pacote_de_exemplos'), '/launch/load.launch.py']),
           launch_arguments={
                'rvizconfig': [get_package_share_directory('pacote_de_exemplos'), '/config/rviz/navigation.rviz'],
            }.items(),
    )

    slam_toobox = Node(
        parameters=[
          [get_package_share_directory('pacote_de_exemplos'), '/config/slam_toolbox.yaml'],
          {'use_sim_time': True}
        ],
        package='slam_toolbox',
        executable='async_slam_toolbox_node',
        name='slam_toolbox',
        arguments=['--ros-args', '--log-level', LaunchConfiguration('log_level')],
    )

    nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([get_package_share_directory('nav2_bringup'), '/launch/bringup_launch.py']),
           launch_arguments={
                'use_sim_time': 'true',
                'log_level': LaunchConfiguration('log_level'),
                'map': [get_package_share_directory('pacote_de_exemplos'),'/config/map/map.yaml'],
                'params_file': [get_package_share_directory('pacote_de_exemplos'),'/config/nav/nav2_params.yaml']
             }.items(),
    )


    ld = LaunchDescription()
    ld.add_action(log_level)
    ld.add_action(simulation)
    ld.add_action(robot)
    # ld.add_action(slam_toobox)
    ld.add_action(nav2)

    return ld