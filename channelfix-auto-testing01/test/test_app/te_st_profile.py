from plex.testcase import LoggedTestCase
from plex.utils import get_file, get_driver
from page.app.login import LoginPage
from page.app.profile import ProfilePage


class ProfilePageTestCase(LoggedTestCase):
    """
    测试个人中心
    """
    @classmethod
    def setUpClass(cls):
        cls.driver = get_driver()  # 启动APP
        cls.page = ProfilePage(cls.driver)  # 启动个人中心页面元素的类

    def test_ProfilePage(self):
        self.page.boot_ad_close_btn.click()  # 点击启动页广告的关闭选项
        self.page.profile_btn.click()  # 点击我的
        self.page.qq_login_btn.click()  # 选择qq登录方式
        self.page.login_btn.click()    # 点击登录,登录成功
        self.page.profile_btn.click()  # 点击我的
        self.page.profile_dynamic_btn.click()   # 点击动态按钮
        self.page.profile_award_btn.click()  # 点击动态按钮
        self.page.profile_tournament_btn.click()  # 点击获奖
        self.page.profile_works_btn.click()  # 点击比赛

# if __name__ == '__main__':
#     ProfilePageTestCase.main