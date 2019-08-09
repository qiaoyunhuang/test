from plex.testcase import LoggedTestCase
from plex.utils import get_file, get_driver
from page.app.bootad import BootAdPage


class BootAdTestCase(LoggedTestCase):
    """
    测试推荐页面
    """
    @classmethod
    def setUpClass(cls):         # 初始值   setUpClass是继承TestCase
        cls.driver = get_driver()
        cls.page = BootAdPage(cls.driver)  # 声明

    def test_BootAdPage(self):
        self.page.boot_ad_skin_btn.click()