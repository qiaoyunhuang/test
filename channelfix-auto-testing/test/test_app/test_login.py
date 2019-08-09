from plex.testcase import LoggedTestCase
from plex.utils import get_file, get_driver
from page.app.login import LoginPage


class LoginTestCase(LoggedTestCase):
    """
    测试登录退出（QQ,微博，微信）
    """
    @classmethod
    def setUpClass(cls):
        cls.driver = get_driver()
        cls.page = LoginPage(cls.driver)
        cls.page.popup_close.click()
        cls.page.login_btn.click()
        cls.user_info = get_file(filename='users_info.json')

    def setUp(self):
        self.option = None

    def test_login_qq(self):
        """测试登录qq, 退出qq"""
        self.option = 'qq'
        qq_account = self.user_info['qq-user1']
        self.page.login(self.option, qq_account)
        self.page.login_btn.click()
        self.assertIsNotNone(self.page.profile_image)

    # def test_login_weibo(self):
    #     """测试登录weibo"""
    #     self.page.login('weibo')
    #
    # def test_login_wechat(self):
    #     """测试登录微信"""
    #     self.page.login('wechat')

    def tearDown(self):
        self.page.logout()
        element = getattr(self.page, '{}_login_btn'.format(self.option))
        self.assertIsNotNone(element)
        self.page.close()
