
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, SetEnvironmentVariable
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    gz_model_path = SetEnvironmentVariable(
        name='GAZEBO_MODEL_PATH',
        value=['/home/robot/gazebo_models:',get_package_share_directory('pacote_de_exemplos'),'/simulation/models'])

    gz_model_uri = SetEnvironmentVariable(name='GAZEBO_MODEL_DATABASE_URI', value='')

    world_path = DeclareLaunchArgument(
        name='world_path', 
        default_value='', 
        description=''
    )

    gazebo = ExecuteProcess(
        cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so', LaunchConfiguration('world_path')], 
        output='screen'
    )
    
    return LaunchDescription([
        gz_model_path,
        # gz_model_uri,
        world_path,
        gazebo,
    ])
