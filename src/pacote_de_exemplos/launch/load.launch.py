from ament_index_python.packages import get_package_share_path

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import Command, LaunchConfiguration

from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    declare_namespace_cmd = DeclareLaunchArgument(
        'namespace',
        default_value='',
        description='Top-level namespace')

    urdf_tutorial_path = get_package_share_path('pacote_de_exemplos')
    default_model_path = urdf_tutorial_path / 'urdf/myfirstrobot.urdf.xacro'
    # default_model_path = urdf_tutorial_path / 'urdf/sam_bot_description.urdf'
    default_rviz_config_path = urdf_tutorial_path / 'config/rviz/robot.rviz'

    gui_arg = DeclareLaunchArgument(name='gui', default_value='false', choices=['true', 'false'],
                                    description='Flag to enable joint_state_publisher_gui')
    model_arg = DeclareLaunchArgument(name='model', default_value=str(default_model_path),
                                      description='Absolute path to robot urdf file')
    rviz_arg = DeclareLaunchArgument(name='rvizconfig', default_value=str(default_rviz_config_path),
                                     description='Absolute path to rviz config file')
    use_sim_time_arg = DeclareLaunchArgument(name='use_sim_time', default_value='true',
                                            description='Flag to enable use_sim_time')

    robot_description = ParameterValue(Command(['xacro ', LaunchConfiguration('model')]),
                                       value_type=str)

    log_level = DeclareLaunchArgument(
        name='log_level', 
        default_value='INFO', 
        choices=['DEBUG','INFO','WARN','ERROR','FATAL'],
        description='Flag to set log level'
    )

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='log',
        parameters=[{
            'use_sim_time': LaunchConfiguration('use_sim_time'), 
            'robot_description': robot_description
        }],
        remappings=[
            ('/tf', 'tf'),
            ('/tf_static', 'tf_static')
        ],
        arguments=['--ros-args', '--log-level', LaunchConfiguration('log_level')]
    )

    # # Depending on gui parameter, either launch joint_state_publisher or joint_state_publisher_gui
    # joint_state_publisher_node = Node(
    #     package='joint_state_publisher',
    #     executable='joint_state_publisher',
    #     condition=UnlessCondition(LaunchConfiguration('gui')),
    #     output='log',
    #     parameters=[{
    #         'use_sim_time': LaunchConfiguration('use_sim_time')
    #     }],
    #     arguments=['--ros-args', '--log-level', LaunchConfiguration('log_level')]
    # )

    # joint_state_publisher_gui_node = Node(
    #     package='joint_state_publisher_gui',
    #     executable='joint_state_publisher_gui',
    #     output='log',
    #     condition=IfCondition(LaunchConfiguration('gui')),
    #     parameters=[{
    #         'use_sim_time': LaunchConfiguration('use_sim_time')
    #     }],
    #     arguments=['--ros-args', '--log-level', LaunchConfiguration('log_level')]
    # )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='own_log',
        parameters=[{
            'use_sim_time': LaunchConfiguration('use_sim_time')
        }],
        arguments=['-d', LaunchConfiguration('rvizconfig'), '--ros-args', '--log-level', LaunchConfiguration('log_level')]

    )

    teleop = Node(
        name='teleop_twist_keyboard',
        package='teleop_twist_keyboard',
        executable='teleop_twist_keyboard',
        output='log',
        prefix=["xterm -hold -e"],
        remappings=[
            # ('/cmd_vel', '/demo/cmd_vel'),
        ],
        arguments=['--ros-args', '--log-level', LaunchConfiguration('log_level')]
    )

    spawn_entity = Node(
    	package='gazebo_ros', 
    	executable='spawn_entity.py',
        arguments=[
            '-entity', 'sam_bot', 
            '-topic', 'robot_description', 
            '--ros-args', '--log-level', LaunchConfiguration('log_level')]
    )

    # robot_localization_node = Node(
    #      package='robot_localization',
    #      executable='ekf_node',
    #      name='ekf_filter_node',
    #      parameters=[
    #          [get_package_share_directory('pacote_de_exemplos'), '/config/nav/ekf.yaml'], 
    #          {'use_sim_time': LaunchConfiguration('use_sim_time')}
    #     ],
    #     arguments=['--ros-args', '--log-level', LaunchConfiguration('log_level')]
    # )
    
    return LaunchDescription([
        declare_namespace_cmd,
        log_level,
        gui_arg,
        model_arg,
        rviz_arg,
        use_sim_time_arg,
        # joint_state_publisher_node,
        # joint_state_publisher_gui_node,
        robot_state_publisher_node,
        spawn_entity,
        # robot_localization_node,
        rviz_node,
        teleop
    ])
