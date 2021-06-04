import os
from base.log import logger
from base import config
import allure

log = logger()


def pytest_start():

    cmd_command = f"pytest --alluredir {config.REPORT_RESULT_PATH} --reruns 2 "
    os.system(cmd_command)


def report():
    log.info("生成报告……")
    #generate_report = f"allure generate {config.REPORT_RESULT_PATH} -o F:\Web端自动化\cms-automation-master\report\allure_result\html --clean"
    generate_report = f"allure serve {config.REPORT_RESULT_PATH} "
    os.system(generate_report)


# def generate_report():
#     log.info("生成报告……")
#     os.system(f"allure generate {config.REPORT_RESULT_PATH} -o {config.REPORT_END_PATH} --clean")
#     #         # 复制history文件夹，在本地生成趋势图
#     files = os.listdir(config.REPORT_HISTORY_PATH)
#     result_history_dir = os.path.join(config.REPORT_RESULT_PATH, "history")
#     # 如果不存在则先创建文件夹
#     if not os.path.exists(result_history_dir):
#         os.mkdir(result_history_dir)
    # for file in files:
    #     shutil.copy(os.path.join(config.REPORT_HISTORY_PATH, file), result_history_dir)

if __name__ == '__main__':
    log.info("开始执行测试")
    pytest_start()
    # generate_report()
    report()
    # run_allure_server()
    # email.send_default_email()

