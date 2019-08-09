from plex.testcase import LoggedTestCase
from page.web.login import LoginPage
from selenium.webdriver.common.keys import Keys
from plex.utils import get_file, get_driver

import settings


class LoginPageTestCase(LoggedTestCase):
    """
    测试web qq, weibo, weixin登录
    """
    @classmethod
    def setUpClass(cls) -> None:
        cls.page = LoginPage(driver=settings.WEB_DRIVER())
        cls.page.close_popup()

    def test_click_login_btn(self):
        self.page.login_btn.click()
        self.assertIsNotNone(self.page.login_popup)  # 点击登录按钮，存在登录弹窗

    def test_click_login_qq(self):
        import time
        time.sleep(10)
        self.page.login_qq.click()
        self.page.qq_login_btn.click()
        self.page.qq_username_input.send_keys('2961353602')
        self.page.qq_password_input.send_keys('KAIXIN123456')
        self.page.qq_login_submit_btn.click()







if __name__ == '__main__':
    LoggedTestCase.main()
