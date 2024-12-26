import rclpy
from rclpy.node import Node
from functools import partial
from example_interfaces.srv import AddTwoInts

class MultiplyTwoIntsClientNode(Node):
    
    def __init__(self):
        super().__init__("multiply_two_ints_client")
        self.call_multiply_two_ints_server(5, 9)
        self.call_multiply_two_ints_server(12, 13)
        
    def call_multiply_two_ints_server(self, a, b):
        client = self.create_client(
            AddTwoInts, "multiply_two_ints"
        )
        while not client.wait_for_service(1.0):
            self.get_logger().info("Waiting for Server Multiply Two ints")
        
        request = AddTwoInts.Request()
        request.a = a
        request.b = b
        
        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_call_multiply_two_ints, a=a, b=b)) 
        
    def callback_call_multiply_two_ints(self, future, a, b):
        try:
            response = future.result()
            self.get_logger().info(str(a) + " x " +
                               str(b) + " = " + 
                               str(response.sum))
        except Exception as e:
            self.get_logger().error("Service call failed %r" % (e,))

                 
def main(args=None):
    rclpy.init(args=args)
    node = MultiplyTwoIntsClientNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
    
if __name__ == "__main__":
    main()