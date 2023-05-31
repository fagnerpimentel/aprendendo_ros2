from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

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
                'rvizconfig': [get_package_share_directory('pacote_de_exemplos'), '/config/rviz/mapping_slam_toolbox.rviz'],
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

    ld = LaunchDescription()
    ld.add_action(log_level)
    ld.add_action(simulation)
    ld.add_action(robot)
    ld.add_action(slam_toobox)

    return ld
