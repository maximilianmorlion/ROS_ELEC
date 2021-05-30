# from launch import LaunchDescription
# from launch_ros.actions import Node
# 
# def generate_launch_description():
#     return LaunchDescription([
#         Node(
#             package='turtlesim',
#             namespace='turtlesim1',
#             executable='turtlesim_node',
#             name='sim'
#         )
#     ])

import os

# trop cheeater donc à potentiellement changer pas la méthode demandée
os.popen("export TURTLEBOT3_MODEL=waffle")
os.popen("export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/opt/ros/foxy/share/turtlebot3_gazebo/models")
os.popen("ros2 launch nav2_bringup tb3_simulation_launch.py")

# 
