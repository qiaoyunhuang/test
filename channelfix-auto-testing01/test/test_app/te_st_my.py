from plex.testcase import LoggedTestCase
from plex.utils import get_file, get_driver
from page.app.login import LoginPage
from page.app.my import MyPage


class MyPageTestCase(LoggedTestCase):
    """测试个人中心"""
    @classmethod
    def setUpClass(cls):
        """Setup中定义了执行测试用例前的一些实例化工作"""
        cls.driver = get_driver()  # 启动APP
        cls.page = MyPage(cls.driver)  # 启动个人中心页面元素的类

    def test_MyPage(self):
        self.page.boot_ad_close_btn.click()  # 点击启动页广告的关闭选项
        self.page.my_btn.click()  # 点击我的
        self.page.qq_login_btn.click()  # 选择qq登录方式
        self.page.qq_username_input.clear()
        self.page.qq_username_input.send_keys("2961353602")
        self.page.qq_password_input.clear()
        self.page.qq_password_input.send_keys("KAIXIN123456")
        self.page.qq_login_submit_btn.click()
        # self.page.qq_login_btn.click()  # 选择qq登录方式
        # self.page.login_btn.click()    # 点击登录
        # self.page.profile_dynamic_btn.click()   # 点击动态按钮
        # self.page.profile_award_btn.click()  # 点击动态按钮
        # self.page.profile_tournament_btn.click()  # 点击获奖
        # self.page.profile_works_btn.click()  # 点击比赛

    def test_logout(self):
        self.page.profile_setting_btn.click()
        self.page.logout_btn.click()
        self.page.confirm_btn.click()
