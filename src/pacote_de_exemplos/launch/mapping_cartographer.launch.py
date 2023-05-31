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
                'rvizconfig': [get_package_share_directory('pacote_de_exemplos'), '/config/rviz/mapping_cartographer.rviz'],
            }.items(),
    )

    cartographer = Node(
        package='cartographer_ros',
        executable='cartographer_node',
        name='cartographer_node',
        output='log',
        remappings=[
            ('scan', 'scan'),
            ('imu', 'imu'),
        ],
        parameters=[{
            'use_sim_time': True
        }],
        arguments=[
            '-configuration_directory', [get_package_share_directory('pacote_de_exemplos'), '/config/nav/'],
            '-configuration_basename', 'cartographer.lua',
            '--ros-args', '--log-level', LaunchConfiguration('log_level')
        ]
    )

    occupacy_grid = Node(
        package='cartographer_ros',
        executable='cartographer_occupancy_grid_node',
        name='occupancy_grid_node',
        output='log',
        parameters=[{
            'use_sim_time': True
        }],
        arguments=[
            '-resolution', '0.05', 
            '-publish_period_sec', '1.0',
            '--ros-args', '--log-level', LaunchConfiguration('log_level')
        ]
    )

    ld = LaunchDescription()
    ld.add_action(log_level)
    ld.add_action(simulation)
    ld.add_action(robot)
    ld.add_action(cartographer)
    ld.add_action(occupacy_grid)

    return ld
