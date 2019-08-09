from plex.testcase import LoggedTestCase  # import 语句来引入模块,from...import语句:从模块中导入一个指定的部分到当前命名空间中
from plex.utils import get_file, get_driver
from page.app.login import LoginPage


class LoginTestCase(LoggedTestCase):
    pass
    """
    测试登录退出（QQ,微博，微信）,使用 class 语句来创建一个新类，class 之后为类的名称并以冒号结尾:
类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。 LoginTestCase继承LoggedTestCase，继承机制：
通过继承创建的新类称为子类或派生类，被继承的类称为基类、父类或超类。
    """
    @classmethod
    def setUpClass(cls):
        """Setup中定义了执行测试用例前的一些实例化工作"""
        cls.driver = get_driver()
        cls.page = LoginPage(cls.driver)
        cls.page.popup_close.click()
        cls.page.login_btn.click()
        cls.user_info = get_file(filename='users_info.json')['qq-user1']

    def setUp(self):
        self.option = None

    def test_login_qq(self):
        """测试登录qq, 退出qq, def 关键词开头，后接函数标识符名称和圆括号()。任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数"""
        self.option = 'qq'
        self.page.login(self.option, self.user_info)
        self.page.login_btn.click()
        self.assertIsNotNone(self.page.profile_image)  # 登录成功后，判断是否有我的页面存在

    # def test_login_weibo(self):
    #     """测试登录weibo"""
    #     self.page.login('weibo')
    #
    # def test_login_wechat(self):
    #     """测试登录微信"""
    #     self.page.login('wechat')

    def tearDown(self):
        """tearDown对执行完测试做了清理和写日志文件工作"""
        self.page.logout()
        element = getattr(self.page, '{}_login_btn'.format(self.option))
        self.assertIsNotNone(element)
        self.page.close()
