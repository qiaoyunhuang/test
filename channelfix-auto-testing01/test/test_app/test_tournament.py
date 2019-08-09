from plex.testcase import LoggedTestCase
from plex.utils import get_file, get_driver
from page.app.tournament import TournamentPage
import time


class TournamentTestCase(LoggedTestCase):
    """
    测试推荐页面
    """
    @classmethod
    def setUpClass(cls):         # 初始值   setUpClass是继承TestCase
        cls.driver = get_driver()
        cls.page = TournamentPage(cls.driver)  # 声明

    def test_FeedPage(self):
        self.page.tournament_btn.click()