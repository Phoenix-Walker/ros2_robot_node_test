import pytest
from std_srvs.srv import Trigger
from utils.log import logger

def test_emergency_stop_service(test_node):
    # 创建急停服务客户端
    client = test_node.create_client(Trigger, "/emergency_stop")
    # 等待服务上线
    ready = client.wait_for_service(timeout_sec=3.0)
    assert ready is True, "急停服务不可用"

    req = Trigger.Request()
    future = client.call_async(req)
    rclpy.spin_until_future_complete(test_node, future)
    resp = future.result()

    assert resp.success is True
    assert resp.message == "Emergency stop triggered, robot halted."
    logger.info("机器人急停服务调用测试通过")
