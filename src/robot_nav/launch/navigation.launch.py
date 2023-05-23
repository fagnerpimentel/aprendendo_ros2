from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():

    robot = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([get_package_share_directory('robot_nav'), '/launch/load.launch.py']),
           launch_arguments={
                'rvizconfig': [get_package_share_directory('robot_nav'), '/config/navigation.rviz'],
            }.items(),
    )

    slam_toobox = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([get_package_share_directory('slam_toolbox'), '/launch/online_async_launch.py']),
           launch_arguments={
                'use_sim_time': 'true',
            }.items(),
    )

    nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([get_package_share_directory('nav2_bringup'), '/launch/navigation_launch.py']),
           launch_arguments={
                'use_sim_time': 'true',
            }.items(),
    )

    return LaunchDescription([
        robot,
        slam_toobox,
        nav2
    ])
