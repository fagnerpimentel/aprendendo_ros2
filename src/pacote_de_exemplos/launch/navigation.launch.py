from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

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
                'rvizconfig': [get_package_share_directory('pacote_de_exemplos'), '/config/rviz/navigation.rviz'],
            }.items(),
    )

    slam_toobox = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([get_package_share_directory('slam_toolbox'), '/launch/online_async_launch.py']),
           launch_arguments={
                'use_sim_time': 'true',
            }.items(),
    )

    nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([get_package_share_directory('nav2_bringup'), '/launch/bringup_launch.py']),
           launch_arguments={
                'use_sim_time': 'true',
                'map': [get_package_share_directory('pacote_de_exemplos'),'/config/map/map.yaml'],
                'params_file': [get_package_share_directory('pacote_de_exemplos'),'/config/nav/nav2_params.yaml']
             }.items(),
    )

    return LaunchDescription([
        simulation,
        robot,
        # slam_toobox,
        nav2
    ])
