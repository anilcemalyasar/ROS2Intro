#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

# inheriting from Node class
class RobotNewsStationNode(Node):

    def __init__(self):
        super().__init__("robot_news_station")

        self.robot_name_ = "TAC"
        self.publisher_ = self.create_publisher(String, "robot_news", 10)
        self.timer_ = self.create_timer(0.5, self.publish_new)
        self.get_logger().info("Robot News Station has been started")

    def publish_new(self):
        msg = String()
        msg.data = "Hi, this is " + str(self.robot_name_) + " from the robot news station." 
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)  # starts ROS2 communication and other features

    # node = Node("py_test")  # first node created
    # node.get_logger().info("Hello ROS2") 
    node = RobotNewsStationNode()

    rclpy.spin(node)  # node will be spinning and program wont stop
    rclpy.shutdown() # shutting down opened ros2 communication

if __name__ == "__main__":
    main()