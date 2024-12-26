import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class MultiplyTwoIntsServerNode(Node):
    
    def __init__(self):
        super().__init__("multiply_two_ints_server")
        self.server_  = self.create_service(
            AddTwoInts, "multiply_two_ints", self.callback_multiply_two_ints
        )
        self.get_logger().info("Multiply two ints server has been started!")
        
    def callback_multiply_two_ints(self, request, response):
        response.sum = request.a * request.b
        self.get_logger().info(
            str(request.a) + " x " + str(request.b) + " = " + str(response.sum))
        return response
        
def main(args=None):
    rclpy.init(args=args)
    node = MultiplyTwoIntsServerNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
    
if __name__ == "__main__":
    main()