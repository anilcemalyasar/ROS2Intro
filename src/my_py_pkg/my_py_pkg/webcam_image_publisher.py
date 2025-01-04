import rclpy
from rclpy.node import Node
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class WebcamImageNode(Node):
    
    def __init__(self):
        super().__init__("image_publisher")
        self.get_logger().info("Starting webcam node...")
        self.publisher_ = self.create_publisher(Image, "image_raw", 10)

        
        # Her 0.1 saniyede frame okuyacağız
        self.timer_ = self.create_timer(
            0.1, self.timer_callback
        )
        
        self.bridge_ = CvBridge()
        self.cap_ = cv2.VideoCapture(0) # source=0 webcam den görüntüyü alması demek
        
        if not self.cap_.isOpened():
            self.get_logger().error("Webcam could not be opened!")
            return 
        
    def timer_callback(self):
        
        ret, frame = self.cap_.read()
        
        if not ret:
            self.get_logger().error("Failed to read frame from webcam!")
            return
        else:
            self.publisher_.publish(self.bridge_.cv2_to_imgmsg(frame))
        
        self.get_logger().info("Publishing video frame")
        
    def read_frame(self):
        
        ret, frame = self.cap_.read()
        
        if not ret:
            self.get_logger().error("Failed to read frame from webcam!")
            return
        
        # Alınan görüntüyü gösterme
        cv2.imshow("Webcam", frame)
        
        # ESC tuşunu basıldığında zorunlu olarak durduruyoruz
        if cv2.waitKey(1) & 0xFF == 27:
            self.destroy_node()
            cv2.destroyAllWindows()
            
    def destroy_node(self):
        self.get_logger().info("Shutting down webcam node!")
        self.cap_.release()
        super().destroy_node()
            
        
def main(args=None):
    rclpy.init(args=args)
    node = WebcamImageNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
    
if __name__ == "__main__":
    main()