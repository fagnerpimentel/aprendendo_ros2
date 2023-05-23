from ament_index_python.packages import get_package_share_path

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import Command, LaunchConfiguration

from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from ament_index_python.packages import get_package_share_directory

world_path = ''

def generate_launch_description():
    urdf_tutorial_path = get_package_share_path('robot_description')
    default_model_path = urdf_tutorial_path / 'urdf/myfirstrobot.urdf.xacro'
    # default_model_path = urdf_tutorial_path / 'urdf/sam_bot_description.urdf'
    default_rviz_config_path = urdf_tutorial_path / 'rviz/robot.rviz'

    gui_arg = DeclareLaunchArgument(name='gui', default_value='false', choices=['true', 'false'],
                                    description='Flag to enable joint_state_publisher_gui')
    model_arg = DeclareLaunchArgument(name='model', default_value=str(default_model_path),
                                      description='Absolute path to robot urdf file')
    rviz_arg = DeclareLaunchArgument(name='rvizconfig', default_value=str(default_rviz_config_path),
                                     description='Absolute path to rviz config file')
    use_sim_time_arg = DeclareLaunchArgument(name='use_sim_time', default_value='true',
                                            description='Flag to enable use_sim_time')

    gazebo = ExecuteProcess(cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so', world_path], output='screen')

    robot_description = ParameterValue(Command(['xacro ', LaunchConfiguration('model')]),
                                       value_type=str)

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{
            'use_sim_time': LaunchConfiguration('use_sim_time'), 
            'robot_description': robot_description
        }]
    )

    # Depending on gui parameter, either launch joint_state_publisher or joint_state_publisher_gui
    joint_state_publisher_node = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        condition=UnlessCondition(LaunchConfiguration('gui')),
        parameters=[{
            'use_sim_time': LaunchConfiguration('use_sim_time')
        }]
    )

    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        condition=IfCondition(LaunchConfiguration('gui')),
        parameters=[{
            'use_sim_time': LaunchConfiguration('use_sim_time')
        }]
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='own_log',
        arguments=['-d', LaunchConfiguration('rvizconfig')],
    )

    teleop = Node(
        name='teleop_twist_keyboard',
        package='teleop_twist_keyboard',
        executable='teleop_twist_keyboard',
        output='screen',
        prefix=["xterm -hold -e"],
        remappings=[
            # ('/cmd_vel', '/demo/cmd_vel'),
        ]
    )

    spawn_entity = Node(
    	package='gazebo_ros', 
    	executable='spawn_entity.py',
        arguments=['-entity', 'sam_bot', '-topic', 'robot_description'],
        output='screen',
    )

    robot_localization_node = Node(
         package='robot_localization',
         executable='ekf_node',
         name='ekf_filter_node',
         output='screen',
         parameters=[
             [get_package_share_directory('robot_nav'), '/config/ekf.yaml'], 
             {'use_sim_time': LaunchConfiguration('use_sim_time')}
        ]
    )
    
    return LaunchDescription([
        gui_arg,
        model_arg,
        rviz_arg,
        use_sim_time_arg,
        gazebo,
        joint_state_publisher_node,
        joint_state_publisher_gui_node,
        robot_state_publisher_node,
        spawn_entity,
        # robot_localization_node,
        rviz_node,
        teleop
    ])
