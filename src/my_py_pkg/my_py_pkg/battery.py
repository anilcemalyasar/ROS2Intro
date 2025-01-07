import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import SetLed

class BatteryNode(Node):
    
    def __init__(self):
        super().__init__("battery")
        # self.client_ = self.create_client(SetLed, "set_led")
        # while not self.client_
        
        
def main(args=None):
    rclpy.init(args=args)
    node = BatteryNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
    
if __name__ == "__main__":
    main()