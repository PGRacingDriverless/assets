#!/usr/bin/env python3
#
# Copyright 2019 ROBOTIS CO., LTD.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Authors: Darby Lim

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    TURTLEBOT3_MODEL = os.environ['TURTLEBOT3_MODEL']

    use_sim_time = LaunchConfiguration('use_sim_time', default='false')
    # urdf_file_name = 'turtlebot3_' + TURTLEBOT3_MODEL + '.urdf'
    
    # print('urdf_file_name : {}'.format(urdf_file_name))

    # urdf_path = os.path.join(
    #     get_package_share_directory('turtlebot3_gazebo'),
    #     'urdf',
    #     urdf_file_name)

    # with open(urdf_path, 'r') as infp:
    #     robot_desc = infp.read()  

    gpu = LaunchConfiguration('gpu', default='False')
    organize_cloud = LaunchConfiguration('organize_cloud', default='False')
    xacro_urdf_file_name = 'turtlebot3_' + TURTLEBOT3_MODEL + '.urdf.xacro'
    
    xacro_path = os.path.join(
        get_package_share_directory('turtlebot3_gazebo'),
        'urdf',
        xacro_urdf_file_name)

    robot_description = Command(['xacro',' ', xacro_path, ' gpu:=', gpu, ' organize_cloud:=', organize_cloud])

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'),

        DeclareLaunchArgument(
            'gpu',
            default_value='False',
            description='Whether to use Gazebo gpu_ray or ray'),

        DeclareLaunchArgument(
            'organize_cloud',
            default_value='False',
            description='Organize PointCloud2 into 2D array with NaN placeholders, otherwise 1D array and leave out invlaid points'),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{
                'use_sim_time': use_sim_time,
                'robot_description': robot_description
            }],
        ),
    ])
