import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger

class EmergencyService(Node):
    def __init__(self):
        super().__init__('emergency_service')
        self.srv = self.create_service(Trigger, '/emergency_stop', self.emergency_callback)
        self.robot_running = True

    def emergency_callback(self, request, response):
        self.robot_running = False
        response.success = True
        response.message = "Emergency stop triggered, robot halted."
        return response

def main(args=None):
    rclpy.init(args=args)
    node = EmergencyService()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
