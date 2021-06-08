import os
import datetime
import re

# ---------------- 项目根目录 --------------------
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------- 日志相关 --------------------
# 日志级别
LOG_LEVEL = 'debug'
LOG_STREAM_LEVEL = 'debug'  # 屏幕输出流
LOG_FILE_LEVEL = 'info'   # 文件输出流
# 日志命名
LOG_FOLDER = os.path.join(BASE_PATH, 'logs')
LOG_FILE_NAME = os.path.join(LOG_FOLDER, datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S') + '.log')

# ---------------yaml文件----------------
YMAL_FILE = os.path.join(BASE_PATH, "data")

# ---------------yaml文件----------------
SCREENSHOTS_FOLDER = os.path.join(BASE_PATH, "screenshots")
SCREENSHOTS_NAME = os.path.join(SCREENSHOTS_FOLDER, datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S') + '.png')

# ---------------- 邮件相关 --------------------
# 邮件文件列表
# FILE_LIST = [
#     os.path.join(BASE_PATH, "report", "zip", "report.zip")
# ]
# "C:\\Users\SKJ-05A14-0028\AppData\Local\Temp\\[0-9]"
#  ---------------- 测试报告 --------------------
REPORT_PATH = os.path.join(BASE_PATH, "report")
REPORT_RESULT_PATH = os.path.join(REPORT_PATH,  "allure_result")

REPORT_REPORT_PATH = os.path.join("F:\report\\[0-9]", "allure_report")
REPORT_HISTORY_PATH = os.path.join(REPORT_PATH, "allure_report", "history")

# ---------------- Email相关 --------------------EMAIL_FROMADDR = '1310063345@qq.com'  # 发件人邮箱
EMAIL_PASSWORD = '1qazxsw2'   # 发件人授权码
EMAIL_TOADDR = ['fuchaoxin@win-stock.com.cn']    # 收件人地址列表'1310063345@qq.com'
EMAIL_FROMADDR = 'fuchaoxin@win-stock.com.cn'

# # 邮件文件列表
# FILE_LIST = [
#     os.path.join(BASE_PATH, "report", "zip", "report.zip")
# ]
#
# # ---------------- 压缩文件相关 --------------------
# # 要压缩文件夹的根路径
# REPORT_DIR = os.path.join(BASE_PATH, "report", "allure_report")
