import os
from base.log import logger
from base import config
from base import email
import zipfile

log = logger()

def pytest_start():

    cmd_command = f"pytest -s -q --alluredir F:\Web端自动化\cms-automation-master\\report\\allure  "
    #--reruns 2
    os.system(cmd_command)


def report():
    generate_report1 = f"allure generate F:\Web端自动化\cms-automation-master\\report\\allure -o F:\Web端自动化\cms-automation-master\\report\\allure_html --clean"
    generate_report2 = f"allure serve F:\Web端自动化\cms-automation-master\\report\\allure "
    os.system(generate_report1)
    os.system(generate_report2)

def zip_ya(startdir,file_news):
    z = zipfile.ZipFile(file_news,'w',zipfile.ZIP_DEFLATED) #文件夹名
    for dirpath, dirnames, filenames in os.walk(startdir):
        fpath = dirpath.replace(startdir,'') #不replace的话，就从根目录开始复制
        fpath = fpath and fpath + os.sep or ''#实现当前文件夹以及包含的所有文件的压缩
        for filename in filenames:
            z.write(os.path.join(dirpath, filename),fpath+filename)
            print("success")
    z.close()

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
    pytest_start()
    # generate_report()
    report()

    # startdir1 = "F:\Web端自动化\cms-automation-master\\report\\allure_html"  # 要压缩的文件夹路径
    # startdir2 = "F:\Web端自动化\cms-automation-master\\logs"  # 要压缩的文件夹路径
    # file_news2 = startdir2+'.zip'  # 压缩后文件夹的名字
    # file_news1 = startdir1 + '.zip'
    # zip_ya(startdir1,file_news1)
    # zip_ya(startdir2, file_news2)
    #email.send_default_email()

