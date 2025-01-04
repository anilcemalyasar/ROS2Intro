import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class WebcamImageSubscriberNode(Node):
    
    def __init__(self):
        super().__init__("image_subscriber")
        
        self.subscriber_ = self.create_subscription(Image, "image_raw", self.listener_callback, 10)
        self.bridge_ = CvBridge()
        self.get_logger().info("Receiving video frame has been started!")
        
    def listener_callback(self, data):
        current_frame = self.bridge_.imgmsg_to_cv2(data)
        cv2.imshow("Webcam", current_frame)
        
        # ESC tuşunu basıldığında zorunlu olarak durduruyoruz
        if cv2.waitKey(1) & 0xFF == 27:
            super().destroy_node()
            cv2.destroyAllWindows()
        
        
        
def main(args=None):
    rclpy.init(args=args)
    node = WebcamImageSubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
    
if __name__ == "__main__":
    main()