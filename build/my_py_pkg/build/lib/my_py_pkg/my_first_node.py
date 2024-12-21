#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

# Node is not an executable object byself

# inheriting from Node class
class MyNode(Node):

    def __init__(self):
        super().__init__("py_test")
        self.counter_ = 0
        self.get_logger().info("Hello ROS2!!!!")
        self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        self.counter_ += 1
        self.get_logger().info("Hello " + str(self.counter_))

def main(args=None):
    rclpy.init(args=args)  # starts ROS2 communication and other features

    # node = Node("py_test")  # first node created
    # node.get_logger().info("Hello ROS2") 
    node = MyNode()

    rclpy.spin(node)  # node will be spinning and program wont stop
    rclpy.shutdown() # shutting down opened ros2 communication

if __name__ == "__main__":
    main()