import os
import datetime
import re


# ---------------- 项目根目录 --------------------
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Pre_Url ="https://rpdtssax-cms.caizidao.com.cn:9011"
#Pre_Url ="https://betassax-cms.caizidao.com.cn:9011"
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

#----------------token-------------------
TOKEN="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2MjU1NjMxMjEsImlhdCI6MTYyNTU2MTMyMSwianRpIjoiMWM5ZTY4N2I0YTQwNGMwNDlmN2FmYTFiOTY2OTM0ZTgiLCJzdWIiOiJtZW5neWluZzEifQ.FqA9HcQ6g3IqOBda0WAJ6pi6aalLUOkoPfecovMOwq0Vaylo9-DsjJ2q2aIe00LPh745WxuNW5mi_RxkGVLOmvOv2mYF577mWa00sCF57nZIiaH38-J1jCkl8vmyw0dVJOTJyKWZwse7zi9gHwk-JZd0brlkcVxOUBazH6yyHPMiPrF2--td2U_d_CAvBMBngIIglx9DbvLi7OH_i5fMFOEw_385ysea1NojWnZ31DMcJb-H6WqbtNsKAKhgtwV-_AlexJrlLnH0PAhuzWoQoDTKa_wCOyWjylgkxXLDVPe5SnjvtMY--zJBgfv5fgRB8gtFBYZk0rE1UaAPrn9reQ"


#  ---------------- 测试报告 --------------------
REPORT_PATH = os.path.join(BASE_PATH, "report")
REPORT_RESULT_PATH = os.path.join(REPORT_PATH,  "allure_result")

REPORT_REPORT_PATH = os.path.join("F:\report\\[0-9]", "allure_report")
REPORT_HISTORY_PATH = os.path.join(REPORT_PATH, "allure_report", "history")

# ---------------- Email相关 --------------------EMAIL_FROMADDR = '1310063345@qq.com'  # 发件人邮箱
EMAIL_PASSWORD = 'itwtjdwkjnvjbagg'   # POP3发件人授权码
#EMAIL_PASSWORD = 'fwljaevgllcybafa'     # IMAP发件人授权码
#EMAIL_PASSWORD = '1qazxsw2'
# EMAIL_TOADDR = ['1256573857@qq.com']    # 收件人地址列表'fuchaoxin@win-stock.com.cn'
EMAIL_FROMADDR = '1256573857@qq.com'
EMAIL_TOADDR = ['fuchaoxin@win-stock.com.cn']    # 收件人地址列表'fuchaoxin@win-stock.com.cn'
#EMAIL_FROMADDR = 'fuchaoxin@win-stock.com.cn'
# # 邮件文件列表
FILE_LIST = [
     os.path.join("F:\Web端自动化\cms-automation-master\\report\\", "allure_html.zip"),
     os.path.join("F:\Web端自动化\cms-automation-master\\", "logs.zip")
]

