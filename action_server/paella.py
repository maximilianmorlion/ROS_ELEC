#! /usr/bin/env python

import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
import sys
import math
import numpy as np
import time
from rclpy.executors import MultiThreadedExecutor
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry

from action_tutorials_interfaces.action import Waiter

from rclpy.qos import qos_profile_system_default, qos_profile_sensor_data



class OdomSub(Node):

    def __init__(self):
        super().__init__('odom_values')
        self.subscription = self.create_subscription(
            Odometry,
            'odom',
            self.listener_callback,
            qos_profile_system_default)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.x = msg.pose.pose.position.x
        self.y = msg.pose.pose.position.y

class GoalPublisher(Node):

    def __init__(self):
        super().__init__('goal_publisher')
        self.publisher_ = self.create_publisher(PoseStamped, 'goal_pose', 2)


    def goal_callback(self):
        msg = PoseStamped()
        msg.pose.position.x = robot_goal[0]
        msg.pose.position.y = robot_goal[1]
        msg.pose.position.z = 0
        msg.pose.orientation.x = 0
        msg.pose.orientation.y = 0
        msg.pose.orientation.z = 0
        msg.pose.orientation.w = 0
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.pose.position.x)

class PaellalActionServer(Node):

    def __init__(self):
        super().__init__('paella_action_server')
        self._action_server = ActionServer(
            self,
            Waiter,
            'waiter',
            self.execute_callback)

    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')
        feedback_msg =Waiter.Feedback()
 

        tables_position = goal_handle.request.goal
        goal_publisher = GoalPublisher()
        scan_sub = ScanSub()
        odom_sub = OdomSub()
        rclpy.spin_once(odom_sub)
        
        robot_pos = (odom_sub.x,odom_sub.y)
        left_tables = 3.0
        tables_done = 0.0
        for i in range(3):
            robot_goal = tables_position[i]
            rclpy.spin_once(goal_publisher)

            while np.abs(robot_goal-robot_pos)>0.4:
                rclpy.spin_once(odom_sub)
                actual_position= (odom_sub.x,odom_sub.y)
                
                feedback_msg.feedback_data = [actual_position[0],actual_position[1],tables_done,tables_left]
                self.get_logger().info('Feedback: {}'.format(feedback_msg.feedback_data))
                goal_handle.publish_feedback(feedback_msg)

        goal_handle.succeed()
        result = Waiter.Result()
        return result


def main(args=None):
    rclpy.init(args=args)

    paella_action_server = PaellaActionServer()
    executor = MultiThreadedExecutor()
    rclpy.spin(paella_action_server, executor=executor)
    paella_action_server.destroy()
    rclpy.shutdown()


if __name__ == '__main__':
    main()