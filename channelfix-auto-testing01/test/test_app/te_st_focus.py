import time
from plex.testcase import LoggedTestCase
from plex.utils import get_file, get_driver
from page.app.focus import LoginPage


class LoginTestCase(LoggedTestCase):
    """
    测试登录退出（QQ,微博，微信）
    """
    @classmethod
    def setUpClass(cls):
        cls.driver = get_driver()
        cls.page = LoginPage(cls.driver)

    def test_Case1_LoginQQ(self):
        """测试登录qq"""
        time.sleep(3)
        self.page.popup_close.click()
        time.sleep(2)
        self.page.my_btn.click()
        self.page.qq_login_btn.click()
        time.sleep(3)
        self.page.qq_username_input.clear()
        self.page.qq_username_input.send_keys("2417397061")
        self.page.qq_password_input.clear()
        self.page.qq_password_input.send_keys("GAOXING123456")
        self.page.qq_login_submit_btn.click()

    def test_Case2_LogOutQQ(self):
        """测试退出QQ"""
        self.page.my_btn.click()
        self.page.profile_setting_btn.click()
        self.page.logout_btn.click()
        time.sleep(1)
        self.page.confirm_btn.click()
        time.sleep(2)

    def test_Case3_Focus(self):
        """关注页面-未登录"""
        self.page.walk_around_btn.click()
        self.page.focus_btn.click()

    def test_Case4_LoginAgainQQ(self):
        """关注页面-登录"""
        self.page.login_focus_btn.click()
        self.page.qq_login_btn.click()
        time.sleep(2)
        self.page.qq_again_login_btn.click()

    # def test_login_weibo(self):
    #     """测试登录weibo"""
    #     self.page.login('weibo')
    #
    # def test_login_wechat(self):
    #     """测试登录微信"""
    #     self.page.login('wechat')
