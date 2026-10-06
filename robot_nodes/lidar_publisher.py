import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import time

class LidarPublisher(Node):
    def __init__(self):
        super().__init__('lidar_publisher')
        self.publisher_ = self.create_publisher(LaserScan, '/scan', 10)
        self.timer_period = 0.5
        self.timer = self.create_timer(self.timer_period, self.timer_callback)

    def timer_callback(self):
        msg = LaserScan()
        msg.ranges = [1.2, 2.3, 3.1, 0.8, 2.0]
        msg.range_min = 0.1
        msg.range_max = 10.0
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = LidarPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
