from ament_index_python.packages import get_package_share_path

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import Command, LaunchConfiguration

from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from ament_index_python.packages import get_package_share_directory
import os
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import DeclareLaunchArgument, ExecuteProcess, SetEnvironmentVariable


def generate_launch_description():

    robot_model = SetEnvironmentVariable(
        name='TURTLEBOT3_MODEL', value='waffle'
    )

    declare_namespace_cmd = DeclareLaunchArgument(
        'namespace',
        default_value='',
        description='Top-level namespace')
    
    declare_robot_name_cmd = DeclareLaunchArgument(
        'robot_name',
        default_value='turtlebot3_waffle',
        description='name of the robot')

    declare_robot_sdf_cmd = DeclareLaunchArgument(
        'robot_sdf',
        default_value=[get_package_share_directory('nav2_bringup'),'/worlds/waffle.model'],
        description='Full path to robot sdf file to spawn the robot in gazebo')


    urdf = os.path.join(get_package_share_directory('nav2_bringup'), 'urdf', 'turtlebot3_waffle.urdf')
    with open(urdf, 'r') as infp:
        robot_description = infp.read()

    start_robot_state_publisher_cmd = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        namespace=LaunchConfiguration('namespace'),
        output='screen',
        parameters=[{
            'use_sim_time': True,
            'robot_description': robot_description
        }],
        remappings=[
            ('/tf', 'tf'),
            ('/tf_static', 'tf_static')
        ]
    )

    start_gazebo_spawner_cmd = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        output='screen',
        arguments=[
            '-entity', LaunchConfiguration('robot_name'),
            '-file', LaunchConfiguration('robot_sdf'),
            '-robot_namespace', LaunchConfiguration('namespace')
        ]
    )

    rviz_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([get_package_share_directory('nav2_bringup'),'/launch/rviz_launch.py']),
        launch_arguments={
            'namespace': LaunchConfiguration('namespace'),
            'use_namespace': 'false',
            'rviz_config': [get_package_share_directory('nav2_bringup'),'/rviz/nav2_default_view.rviz']
        }.items()
    )


    ld = LaunchDescription()
    ld.add_action(robot_model)
    ld.add_action(declare_namespace_cmd)
    ld.add_action(declare_robot_name_cmd)
    ld.add_action(declare_robot_sdf_cmd)
    ld.add_action(start_robot_state_publisher_cmd)
    ld.add_action(start_gazebo_spawner_cmd)
    ld.add_action(rviz_cmd)

    return ld
