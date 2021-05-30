#! /usr/bin/env python

import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
import sys
import math
import numpy as np
import time
from rclpy.executors import MultiThreadedExecutor
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

from action_tutorials_interfaces.action import Waiter

from rclpy.qos import qos_profile_system_default, qos_profile_sensor_data



class ScanSub(Node):

    def __init__(self):
        super().__init__('scan_values')
        self.subscription = self.create_subscription(
            LaserScan,
            'scan',
            self.listener_callback,
            qos_profile_system_default)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.robot_width = msg.range_min
        self.max_dist = msg.range_max
        self.laser_scan = msg.ranges

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
            
        scan_sub = ScanSub()
        odom_sub = OdomSub()
        rclpy.spin_once(odom_sub)
        
        robot_pos = (odom_sub.x,odom_sub.y)
        left_tables = 3.0
        tables_done = 0.0
        for i in range(3):
            robot_goal = tables_position[i]
            
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

    movetogoal_action_server = MovetoGoalActionServer()
    executor = MultiThreadedExecutor()
    rclpy.spin(movetogoal_action_server, executor=executor)
    movetogoal_action_server.destroy()
    rclpy.shutdown()


if __name__ == '__main__':
    main()