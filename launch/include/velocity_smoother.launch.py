import os
import sys

import launch
import launch_ros.actions
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory

import yaml


pkg_name = 'kobuki_velocity_smoother',
exe_name = 'velocity_smoother'
config_file = 'velocity_smoother_params.yaml'

def generate_launch_description():
    share_dir = get_package_share_directory(pkg_name)

    params_file = os.path.join(share_dir, 'config', config_file)
    with open(params_file, 'r') as f:
        params = yaml.safe_load(f)[pkg_name]

    ld = launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(
            name = 'input_cmd_vel_topic',
            default_value = 'raw_cmd_vel'
        ),
        launch.actions.DeclareLaunchArgument(
            name = 'feedback_cmd_vel_topic',
            default_value = 'robot_cmd_vel'
        ),
        launch.actions.DeclareLaunchArgument(
            name = 'output_cmd_vel_topic',
            default_value = 'smoothed_cmd_vel'
        ),
        launch.actions.DeclareLaunchArgument(
            name = 'feedback_odom_topic',
            default_value = 'odom'
        ),
       launch_ros.actions.Node(
            executable = exe_name,
            executable = pkg_name,
            name = pkg_name,
            output = "both",
            parameters = [params],
            remappings = [
                ( pkg_name + '/input', LaunchConfiguration('input_cmd_vel_topic') ),
                ( pkg_name + '/feedback/cmd_vel', LaunchConfiguration('feedback_cmd_vel_topic') ),
                ( pkg_name + '/smoothed', LaunchConfiguration('output_cmd_vel_topic') ),
                ( pkg_name + '/feedback/odometry', LaunchConfiguration('feedback_odom_topic') )
            ]
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
