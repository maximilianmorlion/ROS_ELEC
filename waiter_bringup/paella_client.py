#! /usr/bin/env python
import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
import numpy as np
from action_tutorials_interfaces.action import Waiter


class WaiterActionClient(Node):

    def __init__(self):
        super().__init__('waiter_action_client')
        self._action_client = ActionClient(self, Waiter, 'waiter')

    def send_goal(self, goal):
        print("Sending Goal")
        goal_msg = Waiter.Goal()
        goal_msg.goal = goal

        self._action_client.wait_for_server()


        self._send_goal_future = self._action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
            goal_handle = future.result()
            if not goal_handle.accepted:
                self.get_logger().info('Goal rejected :(')
                return

            self.get_logger().info('Goal accepted :)')

            
            self._get_result_future = goal_handle.get_result_async()
            self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        if result.finished:
            print("Finished")
        else: 
            print("Blocked")
        self.get_logger().info('Result: {0}'.format(result.finished))
        rclpy.shutdown()

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info('Received feedback: {0}'.format(feedback.feedback_data))

def main(args=None):
    rclpy.init(args=args)

    action_client = WaiterActionClient()
    tables_pos =np.array([[1.1,0.0],[1.1,1.1],[1.1,-1.1],[-1.1,1.1],[-1.1,0.0],[0.0,1.1],[0.0,-1.1],[-1.1,-1.1],[0.0,0.0]])
    tables_number = np.arange(0,9)
    numpy.random.shuffle(tables_number)
    selected_tables = tables_pos[tables_number[:3]]
    future = action_client.send_goal(selected_tables)

    rclpy.spin(action_client)


if __name__ == '__main__':
    main()