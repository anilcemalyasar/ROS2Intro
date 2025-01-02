import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import HardwareStatus

class HardwareStatusSubscriberNode(Node):
    
    def __init__(self):
        super().__init__("hardware_status_subscriber")
        self.hw_status_subscriber_ = self.create_subscription(HardwareStatus, "hardware_status", self.callback_hardware, 10)
        self.get_logger().info("Hardware status subscriber has been started!")
        
    def callback_hardware(self, msg):
        self.get_logger().info("Hardware Temperature:\t" + str(msg.temperature) + "\n" + 
                                "Are Motors Ready:\t" + str(msg.are_motors_ready) + "\n" + 
                                "Debug Message:\t" + str(msg.debug_message))
        
        
def main(args=None):
    rclpy.init(args=args)
    node = HardwareStatusSubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
    
if __name__ == "__main__":
    main()