import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class SubscriberNode(Node):
    
    def __init__(self):
        super().__init__("minimal_subscriber")
        self._subscriber_ = self.create_subscription(String, "topic", self.callback_topic, 10)
        self.get_logger().info("Python subscriber has been started!")
        
    def callback_topic(self, msg):
        self.get_logger().info("I heard: " + msg.data)
        
        
def main(args=None):
    rclpy.init(args=args)
    node = SubscriberNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()