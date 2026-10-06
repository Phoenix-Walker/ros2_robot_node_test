# ros2_robot_node_test
ROS2机器人节点自动化测试项目，基于 pytest + rclpy，模拟机器人传感器话题、急停服务，实现机器人软件节点自动化回归测试。

## 技术栈
Python3, ROS2 Humble, rclpy, pytest, PyYAML, Git/GitHub

## 项目目录
ros2_robot_node_test/
├── robot_nodes/                   # 被测模拟机器人节点
│   ├── init.py
│   ├── lidar_publisher.py        # 模拟激光雷达话题发布节点
│   └── emergency_service.py      # 机器人急停服务节点
├── test_cases/                    # pytest测试用例
│   ├── init.py
│   ├── test_lidar_topic.py       # 激光雷达话题消息测试
│   └── test_emergency_service.py # 急停服务接口测试
├── test_data/                     # YAML测试数据
│   ├── init.py
│   └── cases.yaml
├── utils/
│   └── log.py                    # 日志工具封装
├── conftest.py                    # pytest全局fixture，ROS2初始化与销毁
└── requirements.txt


## 项目功能
1. 模拟机器人激光雷达节点，持续发布 `/scan` 话题数据
2. 模拟机器人急停服务 `/emergency_stop`，支持远程调用触发急停
3. 自动化测试：校验话题消息接收、消息字段合法性、ROS服务调用结果
4. YAML管理测试数据，实现测试数据和代码分离
5. 完整日志记录，方便定位节点通信异常

## 环境搭建（WSL2 Ubuntu22.04）
```bash
# 1. 安装ROS2 Humble
# 2. 克隆项目
git clone https://github.com/phoenix-walker/ros2_robot_node_test.git
cd ros2_robot_node_test
# 3. 安装python依赖
pip install -r requirements.txt
```

## 运行步骤
 1. 新开终端，启动激光雷达节点
 python robot_nodes/lidar_publisher.py 
 2. 新开终端，启动急停服务节点
 python robot_nodes/emergency_service.py 
 3. 新开终端，执行自动化测试
 pytest test_cases/ -v
 
## 测试范围
  话题通信测试：验证传感器消息正常发布，消息参数符合预期
  ROS服务测试：调用急停服务，校验返回状态与提示信息
  超时异常校验：服务不可达、话题无消息时用例断言失败

## 项目亮点
 使用 rclpy + pytest 搭建ROS2机器人节点自动化测试框架
​ 覆盖机器人传感器话题、机器人服务接口两类典型ROS通信场景
​ 采用数据驱动，YAML存放预期值，便于后续维护新增测试场景
​ 项目代码托管GitHub，文档齐全，可复现整套机器人节点回归流程
