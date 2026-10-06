import rclpy
import pytest
from rclpy.node import Node

@pytest.fixture(scope="session", autouse=True)
def ros_init_shutdown():
    # 测试会话启动前初始化ROS2
    rclpy.init()
    yield
    # 全部用例跑完后关闭ROS2
    rclpy.shutdown()

@pytest.fixture(scope="function")
def test_node():
    # 测试用例单独的测试节点，用于订阅/调用服务
    node = Node("test_client_node")
    yield node
    node.destroy_node()
