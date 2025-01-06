import rclpy
from rclpy.node import Node

class YoloObjectDetectionNode(Node):
    
    def __init__(self):
        super().__init__("yolo_detection_model")
        
        
def main(args=None):
    rclpy.init(args=args)
    node = YoloObjectDetectionNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
    
if __name__ == "__main__":
    main()