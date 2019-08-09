from page.web.profile import ProfilePage
from plex.testcase import LoggedTestCase
import settings


class ProfilePageTestCase(LoggedTestCase):
    """
    个人详情页面测试
    """
    @classmethod
    def setUpClass(cls):
        cls.driver = settings.WEB_DRIVER()
        cls.page = ProfilePage(cls.driver)
        cls.page.close_popup()

    def test_stat_box(self):
        """
            测试点击排名按钮
        """
        self.page.stat_box.click()
        self.assertIn('leaderboard', self.driver.current_url)
        self.driver.back()

    def test_click_weibo_btn(self):
        """
            测试点击微博个人页面
        """
        self.page.third_party_btn.click()
        current_window_handle = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            if current_window_handle != handle:
                self.driver.switch_to.window(handle)
                self.page.weibo_logo_btn
                self.assertIn('微博', self.driver.title)
                self.driver.close()
                break
        self.driver.switch_to.window(current_window_handle)

    @classmethod
    def tearDownClass(cls):
        cls.page.close()
