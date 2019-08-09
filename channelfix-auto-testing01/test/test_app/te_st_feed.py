from plex.testcase import LoggedTestCase
from plex.utils import get_file, get_driver
from page.app.feed import FeedPage
import time


class FeedTestCase(LoggedTestCase):
    """
    测试推荐页面
    """
    @classmethod
    def setUpClass(cls):         # 初始值   setUpClass是继承TestCase
        cls.driver = get_driver()
        cls.page = FeedPage(cls.driver)  # 声明

    def test_FeedPage(self):
        self.page.boot_ad_close_btn.click()
        self.page.feed_btn.click()
        self.scroll_action(0.8, 0.25, 3)  # 向上滑3次
        self.scroll_action(0.25, 0.8, 5)  # 向下滑5次
        self.page.join_btn.click()
        # self.scroll_left(3)  # 向左滑动3次
        # self.page.join_btn.click()
        # size = self.driver.get_window_size()  # 获取屏幕尺寸
        # print(size)
        # width = size['width']  # 获取屏幕宽度
        # height = size['height']  # 获取屏幕高度
        # self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 1000)  # 上下滑动, 坐标变化：startx, endx保持一致, 改变starty, endy。endy > starty 上滑，反之下滑
        """
        测试3次上滑推荐页面
        """
        # size = self.driver.get_window_size()
        # self.scroll_action(0.8, 0.25, 3)
        # self.scroll_action(0.25, 0.8, 5)
        # print(size)
        # width = size['width']  # 获取屏幕宽度 width
        # print(width)
        # height = size['height']  # 获取屏幕高度 height
        # print(height)
        # x1 = width * 0.5
        # y1 = height * 0.8
        # y2 = height * 0.25
        # time.sleep(3)
        # print("滑动前")
        # self.driver.swipe(x1, y1, x1, y2)
        # print("滑动后")
        # # 增加滑动次数，滑动效果不明显，增加滑动次数
        # for i in range(3):
        #     print("第%d次滑屏" % i)
        #     time.sleep(3)
        #     self.driver.swipe(x1, y1, x1, y2)
        # time.sleep(3)
        # # 5次下滑
        # size = self.driver.get_window_size()
        # print(size)
        # width = size['width']  # 获取屏幕宽度 width
        # print(width)
        # height = size['height']
        # print(height)  # 获取屏幕高度 height
        # x1 = width * 0.5
        # y1 = height * 0.25
        # y2 = height * 0.8
        # time.sleep(3)
        # print("滑动前")
        # self.driver.swipe(x1, y1, x1, y2)
        # print("滑动后")
        # # 增加滑动次数，滑动效果不明显，增加滑动次数
        # for i in range(5):
        #     print("第%d次滑屏" % i)
        #     time.sleep(3)
        #     self.driver.swipe(x1, y1, x1, y2)
        # time.sleep(3)
        # self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 1000)  # 左右滑动, 坐标变化：starty, endy保持一致, 改变startx, endx。startx > endx 左滑，反之右滑

    def scroll_action(self, fixed_height, fixed_width, count):
        size = self.driver.get_window_size()
        width = size['width']  # 获取屏幕宽度 width
        height = size['height']
        x1 = width * 0.5
        y1 = height * fixed_height
        y2 = height * fixed_width
        self.driver.swipe(x1, y1, x1, y2)
        for i in range(count):
            print("第%d次滑屏" % i)
            time.sleep(3)
            self.driver.swipe(x1, y1, x1, y2)
        time.sleep(3)

    def scroll_left(self, count):
        size = self.driver.get_window_size()
        width = size['width']  # 获取屏幕宽度 width
        height = size['height']
        x1 = width * 0.8
        x2 = width * 0.2
        y1 = height * 0.5
        self.driver.swipe(x1, y1, x2, y1)
        for i in range(count):
            print("第%d次滑屏" % i)
            time.sleep(3)
            self.driver.swipe(x1, y1, x2, y1)
        time.sleep(3)


    # def test_swipe(self):
    #     self.page.swipe(273, 999, 445, 421, 30)
