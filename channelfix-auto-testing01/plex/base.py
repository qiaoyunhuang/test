from plex.element import Element, ClassElement, IdElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from plex.utils import handle_screenshot
from selenium.common.exceptions import TimeoutException
import settings
import logging
import traceback
import time


class BasePage:
    """
        基础页面类
    """
    popup_close = None

    def __init__(self, driver):
        self.driver = driver

    def __getattribute__(self, item):
        obj = super().__getattribute__(item)
        if isinstance(obj, Element):
            return self.find_element(obj)
        return obj

    def find_element(self, path):
        if path.type:
            try:
                WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located(
                        (path.type, path.value))
                )
            except TimeoutException as e:
                logging.error(traceback.format_exc())
                handle_screenshot(self.driver, settings.EXCEPTION_IMAGE_PATH)
        _fun = getattr(self.driver, path.func)
        element = _fun(path.value)
        # need auto screenshot
        if not path.need_shot:
            return element
        for action in ['click', 'send_keys']:
            fun = getattr(element, action)

            def wrap(args=None, _fun=fun, _action=action):
                if args:
                    _fun(args)
                else:
                    _fun()
                handle_screenshot(self.driver, settings.NORMAL_IMAGE_PATH)
            setattr(element, action, wrap)
        return element

    def close(self):
        self.driver.quit()

    def click_event(self, element):
        element.click()

    def close_popup(self):
        if self.popup_close:
            self.popup_close.click()


class WebBasePage(BasePage):
    """web页面基类"""
    url = None
    popup_close = ClassElement('popup__close')

    def __init__(self, driver):
        super().__init__(driver)
        if self.url:
            self.driver.get(self.url)


class AppBasePage(BasePage):
    """App页面基类"""
    popup_close = IdElement('com.vs.vipsai:id/img_home_popu_close')

# class clean:
#     def clean_text(self,text)  # 清除文本框方法的安装
#       self.keyevent(123)    # 123代表光标移动到末尾键
#       for i in range(0,len(text)):
#           self.keyevent(67)   #  67代表退格键
#
#     def find_ele(self,id):  # 获取到要删除的文本框内容
#         find_ele = driver.find_element_by_id(id)
#         find_ele.click()
#         ruturn find_ale.get_attribute('text')
#

# FileName : Tmall_App.py
# Author   : Adil
# DateTime : 2018/3/25 17:22
# SoftWare : PyCharm


# import time
# from appium import  webdriver

# caps = {}
#
# caps['platformName'] = 'Android'
# caps['platformVersion'] = '6.0'
# caps['deviceName'] = 'N79SIV5PVCSODAQC'
# caps['appPackage'] = 'com.tmall.wireless'
# caps['appActivity'] = 'com.tmall.wireless.splash.TMSplashActivity'
# #隐藏键盘
# caps['unicodeKeyboard'] = True
# caps['resetKeyboard'] = True
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)

# # 获取屏幕的size
# size = driver.get_window_size()
# print(size)
# # 获取屏幕宽度 width
# width = size['width']
# print(width)
# # 获取屏幕高度 height
# height = size['height']
# print(height)
#
# # 执行滑屏操作,向下（下拉）滑动
# x1 = width*0.5
# y1 = height*0.25
# y2 = height*0.8
# time.sleep(3)
# print("滑动前")
# driver.swipe(x1,y1,x1,y2)
# print("滑动后")
# # 增加滑动次数，滑动效果不明显，增加滑动次数
#
# for i in range(5):
#     print("第%d次滑屏"%i)
#     time.sleep(3)
#     driver.swipe(x1,y1,x1,y2)
# time.sleep(3)

    # """
    #      封装滑动方法
    #  """
    # size = self.driver.get_window_size() # 获取屏幕的size
    # print(size)
    # width = size['width']  # 获取屏幕宽度 width
    # print(width)
    # height = size['height']  # 获取屏幕高度 height
    # print(height)
    #
    # def swipeUp(driver,n = 5):
    #     """定义向上滑动方法"""
    #     print("定义向上滑动方法")
    #     x1 = width*0.5
    #     y1 = height*0.9
    #     y2 = height*0.25
    #     time.sleep(3)
    #     print("滑动前")
    #     for i in range(n):
    #         print("第%d次滑屏" % i)
    #         time.sleep(3)
    #         driver.swipe(x1, y1, x1, y2)
    #
    # def swipeDown(driver,n = 5):
    #     """定义向下滑动方法"""
    #     print("定义向下滑动方法")
    #     x1 = width*0.5
    #     y1 = height*0.25
    #     y2 = height*0.9
    #     time.sleep(3)
    #     print("滑动前")
    #         for i in range(n):
    #         print("第%d次滑屏" % i)
    #         time.sleep(3)
    #         driver.swipe(x1, y1, x1, y2)
    #
    # def swipeLeft(driver,n = 5):
    #     """定义向左滑动方法"""
    #     print("定义向左滑动方法")
    #     x1 = width*0.8
    #     x2 = width*0.2
    #     y1 = height*0.5
    #     time.sleep(3)
    #     print("滑动前")
    #         for i in range(n):
    #         print("第%d次滑屏" % i)
    #         time.sleep(3)
    #         driver.swipe(x1, y1, x2, y1)
    #
    # def swipeRight(driver,n = 5):
    #     """定义向右滑动方法"""
    #     print("定义向右滑动方法")
    #     x1 = width*0.2
    #     x2 = width*0.8
    #     y1 = height*0.5
    #     time.sleep(3)
    #     print("滑动前")
    #         for i in range(n):
    #         print("第%d次滑屏" % i)
    #         time.sleep(3)
    #         driver.swipe(x1, y1, x2, y1)

# if __name__ == '__main__':
#
#     swipeUp(driver)
#     swipeDown(driver)
#     swipeLeft(driver)
#     swipeRight(driver)
#
#     driver.quit()