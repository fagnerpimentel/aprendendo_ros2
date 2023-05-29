from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():

    simulation = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([get_package_share_directory('pacote_de_exemplos'), '/launch/simulation.launch.py']),
           launch_arguments={
                'world_path': [get_package_share_directory('pacote_de_exemplos'), '/simulation/worlds/simple_room_with_fixed_boxes.world'],
            }.items(),
    )

    robot = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([get_package_share_directory('pacote_de_exemplos'), '/launch/load.launch.py']),
           launch_arguments={
                'rvizconfig': [get_package_share_directory('pacote_de_exemplos'), '/config/rviz/mapping_slam_toolbox.rviz'],
            }.items(),
    )

    slam_toobox = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([get_package_share_directory('slam_toolbox'), '/launch/online_async_launch.py']),
           launch_arguments={
                'use_sim_time': 'true',
                'slam_params_file': [get_package_share_directory('pacote_de_exemplos'), '/config/nav/slam_toobox.yaml']
            }.items(),
    )

    ld = LaunchDescription()
    ld.add_action(simulation)
    ld.add_action(robot)
    ld.add_action(slam_toobox)

    return ld
