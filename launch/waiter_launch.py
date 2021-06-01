from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld= LaunchDescription()
        paella_servnode = Node(
            package='waiter_bringup',
            executable='paella',
            name='paella_server'
        )
        paella_clientnode = Node(
            package='waiter_bringup',
            executable='paella_client',
            name='paella_server'
        )
    ld.add_action(paella_servnode)
    ld.add_action(paella_clientnode)
    return ld

import os

# trop cheeater donc à potentiellement changer pas la méthode demandée
os.popen("export TURTLEBOT3_MODEL=waffle")
os.popen("export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/opt/ros/foxy/share/turtlebot3_gazebo/models")
os.popen("ros2 launch nav2_bringup tb3_simulation_launch.py")

# Spaun du robot dans l'environement
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseWithCovarianceStamped


publisher = Node.create_publisher(PoseWithCovarianceStamped, 'initialpose', 10)
msgPose = PoseWithCovarianceStamped()
msgPose.pose.pose.position.x = 2
msgPose.pose.pose.position.y = 0

publisher.publish(msgPose)


