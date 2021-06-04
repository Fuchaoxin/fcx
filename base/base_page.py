import datetime
import pymysql
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import os
import yaml
from base import config
from base.log import logger
import re


class BasePage:

    log = logger()

    def __init__(self, driver):    # 初始化
        self.driver = driver

    # def setup(self):
    #     StartAPP().run_app(devices_name=self._device_name)
    #
    # def teardown(self):
    #     StartAPP().end(devices_name=self._device_name)

    def find_element(self, type, locator):    # 查找元素
        try:
            WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((type, locator)))
            return self.driver.find_element(type, locator)
        except:
            self.get_screenshots()
            self.log.info("%s 页面中未能找到 %s 元素" % (self, locator))
            raise

    def find_elements(self, type, locator):   # 查找一类元素
        try:
            WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_all_elements_located((type, locator)))
            elements = self.driver.find_elements(type, locator)
            return elements
        except:
            self.get_screenshots()
            self.log.info("%s 页面中未能找到 %s 元素" % (self, locator))
            raise

    def find_element_and_click(self, type, locator):   # 查找元素并点击
        try:
            element = self.find_element(type, locator)
            element.click()
        except:
            self.get_screenshots()
            self.log.info("点击无效！！！")
            raise

    def send_keys(self, type, locator, value):   # 查找元素并输入
        try:
            self.find_element(type, locator).clear()
            return self.find_element(type, locator).send_keys(value)
        except:
            self.get_screenshots()
            self.log.info("无法输入！！！")
            raise

    def is_element_exist(self, element):   # 查看页面元素是否存在
        source = self.driver.page_source
        if element in source:
            return True
        else:
            return False

    def get_toast(self):  # 获取toast提示
        try:
            WebDriverWait(self.driver, 20, 0.1).until(expected_conditions.presence_of_element_located(
                (By.XPATH, "//*[@class='android.widget.Toast']")))
            toast_text = self.find_element(By.XPATH, "//*[@class='android.widget.Toast']").text
            return toast_text
        except:
            self.log.info("未发现toast提示！！！")
            return

    def get_screenshots(self):   # 截图并存放在指定路径
        return self.driver.get_screenshot_as_file(config.SCREENSHOTS_NAME)

    def get_file_from_yaml(self):   # 读取页面定位的yaml文件
        yaml_path = os.path.join(config.YMAL_FILE, 'locators.yaml')
        file = open(yaml_path, mode='r', encoding='utf-8')
        data = yaml.safe_load(file)
        return data

    def get_numbers_from_str(self, text):   # 从字符串中读取整数或小数
        numbers = re.search(r'\d+\.?\d+', text)
        return numbers

    def get_data(self):  # 获取测试用例测试数据的yaml文件
        yaml_path = os.path.join(config.YMAL_FILE, 'data.yaml')
        file = open(yaml_path, mode='r', encoding='utf-8')
        data = yaml.safe_load(file)
        return data

    def get_current_time(self):   # 获取当前时间
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        return current_time

    def connect_database(self, sql):  # 连接数据库并获取通过SQL获取数据
        connect = pymysql.Connect(
            host='172.27.252.41',
            port=3306,
            user='root',
            password='#FDIS#2018@',
            db='fund2',
            charset='utf8'
        )
        cursor = connect.cursor()
        if "DELETE" in sql:
            try:
                cursor.execute(sql)
                connect.commit()
            except:
                connect.rollback()
        elif "UPDATE" in sql:
            try:
                cursor.execute(sql)
                connect.commit()
            except:
                connect.rollback()
        else:
            cursor.execute(sql)
            all_data = cursor.fetchall()
            for data in all_data:
                return data

    def switch_to_context(self):   # 切换到WebView页面
        self.log.info(self.driver.contexts)
        try:
            self.driver.switch_to.context('WEBVIEW_com.linlong.fund.debug')
        except:
            self.get_screenshots()
            self.log.info(self.driver.current_context + " 无法切换到WebView")
        return

    def switch_to_native(self):  # 切换到原生页面
        try:
            self.driver.switch_to.context('NATIVE_APP')
        except:
            self.get_screenshots()
            self.log.info(self.driver.current_context + " 无法切换到native")
        return

    def get_page_size(self):  # 获取页面尺寸
        x = self.driver.get_window_size()['width']   # 宽
        y = self.driver.get_window_size()['height']  # 高
        return x, y

    def slip_up(self):   # 向上滑
        s = BasePage.get_page_size(self)
        self.driver.swipe(int(s[0]*0.5), int(s[1]*0.96), int(s[0]*0.5), int(s[1]*0.125))

    def slip_down(self):   # 向下滑动
        s = BasePage.get_page_size(self)
        self.driver.swipe(int(s[0] * 0.5), int(s[1] * 0.2), int(s[0]* 0.5), int(s[1] * 0.9))

    def slip_left(self):   # 向左滑动
        s = BasePage.get_page_size(self)
        self.driver.swipe(int(s[0] * 9), int(s[1] * 0.5), int(s[0] * 0.1), int(s[1] * 0.5))

    def slip_right(self):   # 向右滑动
        s = BasePage.get_page_size(self)
        self.driver.swipe(int(s[0] * 0.1), int(s[1] * 0.5), int(s[0] * 0.9), int(s[1] * 0.5))

    def long_press(self, x, y, ti):   # 长按
        TouchAction(self.driver).press(x=x, y=y).wait(ti).release().perform()

    def tap(self, x, y):   # 点击
        TouchAction(self.driver).tap(x=x, y=y).release().perform()

    def short_press(self, x, y):
        TouchAction(self.driver).press(x=x, y=y).release().perform()

    def slip_move_2(self, ti):   # 页面滑动
        # 移动
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        try:
            WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located((By.ID, "view_pager")))
            TouchAction(self.driver).press(x=x*0.99, y=y*0.5).wait(ti).move_to(x=x*0.01, y=y*0.5).wait(ti).release().perform()
        except:
            self.log.info("未进入引导页")

    def move(self, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, ti):    # 移动
        TouchAction(self.driver).press(x=x1, y=y1).wait(ti)\
            .move_to(x=x2, y=y2).wait(ti).move_to(x=x3, y=y3).wait(ti).move_to(x=x4, y=y4)\
            .wait(ti).move_to(x=x5, y=y5).release().perform()

    def slip_move(self, x1, y1, x2, y2, ti):   # 页面滑动
        try:
            TouchAction(self.driver).press(x=x1, y=y1).wait(ti).move_to(x=x2, y=y2).wait(ti).release().perform()
        except:
            self.log.info("无法滑动")

    def slip_control_btn_up(self, type, locator):   # 向上滑动
        control_btn = self.find_element(type, locator)
        btn_height = control_btn.size['height']
        btn_width = control_btn.size['width']
        start_x = control_btn.location['x']
        start_y = control_btn.location['y']
        self.slip_move(x1=start_x + btn_width/2, y1=start_y + btn_height*7/10,
                       x2=start_x + btn_width/2, y2=start_y + btn_height/2, ti=100)

    def slip_control_btn_down(self, type, locator):   # 向下滑动
        control_btn = self.find_element(type, locator)
        btn_height = control_btn.size['height']
        btn_width = control_btn.size['width']
        start_x = control_btn.location['x']
        start_y = control_btn.location['y']
        self.slip_move(x1=start_x + btn_width / 2, y1=start_y + btn_height*3 / 10,
                       x2=start_x + btn_width / 2, y2=start_y + btn_height/2, ti=100)

    def click_physical_keys(self, num):  # 模拟物理键
        self.driver.press_keycode(num)
        # 电话键
        # KEYCODE_CALL
        # 拨号键
        # 5
        # KEYCODE_ENDCALL
        # 挂机键
        # 6
        # KEYCODE_HOME
        # 按键Home
        # 3
        # KEYCODE_MENU
        # 菜单键
        # 82
        # KEYCODE_BACK
        # 返回键
        # 4
        # KEYCODE_SEARCH
        # 搜索键
        # 84
        # KEYCODE_CAMERA
        # 拍照键
        # 27
        # KEYCODE_FOCUS
        # 拍照对焦键
        # 80
        # KEYCODE_POWER
        # 电源键
        # 26
        # KEYCODE_NOTIFICATION
        # 通知键
        # 83
        # KEYCODE_MUTE
        # 话筒静音键
        # 91
        # KEYCODE_VOLUME_MUTE
        # 扬声器静音键
        # 164
        # KEYCODE_VOLUME_UP
        # 音量增加键
        # 24
        # KEYCODE_VOLUME_DOWN
        # 音量减小键
        # 25
        #
        # 控制键
        #
        # KEYCODE_ENTER
        # 回车键
        # 66
        # KEYCODE_ESCAPE
        # ESC键
        # 111
        # KEYCODE_DPAD_CENTER
        # 导航键
        # 确定键
        # 23
        # KEYCODE_DPAD_UP
        # 导航键
        # 向上
        # 19
        # KEYCODE_DPAD_DOWN
        # 导航键
        # 向下
        # 20
        # KEYCODE_DPAD_LEFT
        # 导航键
        # 向左
        # 21
        # KEYCODE_DPAD_RIGHT
        # 导航键
        # 向右
        # 22
        # KEYCODE_MOVE_HOME
        # 光标移动到开始键
        # 122
        # KEYCODE_MOVE_END
        # 光标移动到末尾键
        # 123
        # KEYCODE_PAGE_UP
        # 向上翻页键
        # 92
        # KEYCODE_PAGE_DOWN
        # 向下翻页键
        # 93
        # KEYCODE_DEL
        # 退格键
        # 67
        # KEYCODE_FORWARD_DEL
        # 删除键
        # 112
        # KEYCODE_INSERT
        # 插入键
        # 124
        # KEYCODE_TAB
        # Tab键
        # 61
        # KEYCODE_NUM_LOCK
        # 小键盘锁
        # 143
        # KEYCODE_CAPS_LOCK
        # 大写锁定键
        # 115
        # KEYCODE_BREAK
        # Break / Pause键
        # 121
        # KEYCODE_SCROLL_LOCK
        # 滚动锁定键
        # 116
        # KEYCODE_ZOOM_IN
        # 放大键
        # 168
        # KEYCODE_ZOOM_OUT
        # 缩小键
        # 169
        # 组合键
        # KEYCODE_ALT_LEFT
        # Alt + Left
        # KEYCODE_ALT_RIGHT
        # Alt + Right
        # KEYCODE_CTRL_LEFT
        # Control + Left
        # KEYCODE_CTRL_RIGHT
        # Control + Right
        # KEYCODE_SHIFT_LEFT
        # Shift + Left
        # KEYCODE_SHIFT_RIGHT
        # Shift + Right
        # 基本
        # KEYCODE_0
        # 按键’0’ 7
        # KEYCODE_1
        # 按键’1’ 8
        # KEYCODE_2
        # 按键’2’ 9
        # KEYCODE_3
        # 按键’3’ 10
        # KEYCODE_4
        # 按键’4’ 11
        # KEYCODE_5
        # 按键’5’ 12
        # KEYCODE_6
        # 按键’6’ 13
        # KEYCODE_7
        # 按键’7’ 14
        # KEYCODE_8
        # 按键’8’ 15
        # KEYCODE_9
        # 按键’9’ 16
        # KEYCODE_A
        # 按键’A’ 29
        # KEYCODE_B
        # 按键’B’ 30
        # KEYCODE_C
        # 按键’C’ 31
        # KEYCODE_D
        # 按键’D’ 32
        # KEYCODE_E
        # 按键’E’ 33
        # KEYCODE_F
        # 按键’F’ 34
        # KEYCODE_G
        # 按键’G’ 35
        # KEYCODE_H
        # 按键’H’ 36
        # KEYCODE_I
        # 按键’I’ 37
        # KEYCODE_J
        # 按键’J’ 38
        # KEYCODE_K
        # 按键’K’ 39
        # KEYCODE_L
        # 按键’L’ 40
        # KEYCODE_M
        # 按键’M’ 41
        # KEYCODE_N
        # 按键’N’ 42
        # KEYCODE_O
        # 按键’O’ 43
        # KEYCODE_P
        # 按键’P’ 44
        # KEYCODE_Q
        # 按键’Q’ 45
        # KEYCODE_R
        # 按键’R’ 46
        # KEYCODE_S
        # 按键’S’ 47
        # KEYCODE_T
        # 按键’T’ 48
        # KEYCODE_U
        # 按键’U’ 49
        # KEYCODE_V
        # 按键’V’ 50
        # KEYCODE_W
        # 按键’W’ 51
        # KEYCODE_X
        # 按键’X’ 52
        # KEYCODE_Y
        # 按键’Y’ 53
        # KEYCODE_Z
        # 按键’Z’ 54






