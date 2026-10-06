import logging
import os
from datetime import datetime

# 日志文件夹
LOG_PATH = "./logs"
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)

# 日志文件名
log_file = os.path.join(LOG_PATH, f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

logger = logging.getLogger("robot_test")
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 文件输出
file_handler = logging.FileHandler(log_file, encoding="utf-8")
file_handler.setFormatter(formatter)
# 控制台输出
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)
