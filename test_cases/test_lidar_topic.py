import pytest
from sensor_msgs.msg import LaserScan
from utils.log import logger

def test_lidar_topic_msg(test_node):
    # 订阅/scan激光雷达话题，等待消息
    msg_received = None
    def callback(msg):
        nonlocal msg_received
        msg_received = msg

    sub = test_node.create_subscription(LaserScan, "/scan", callback, 10)
    
    # 循环等待消息，最多等待3秒
    timeout = 3.0
    start_time = test_node.get_clock().now().nanoseconds / 1e9
    while msg_received is None:
        rclpy.spin_once(test_node, timeout_sec=0.1)
        current = test_node.get_clock().now().nanoseconds / 1e9
        if current - start_time > timeout:
            break
    
    # 断言校验
    assert msg_received is not None, "未收到激光雷达话题消息"
    assert msg_received.range_min == 0.1
    assert msg_received.range_max == 10.0
    logger.info("激光雷达话题测试通过，消息字段校验成功")
