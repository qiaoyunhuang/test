from plex.base import AppBasePage
from plex.element import IdElement, AccessibilityIdElement, XpathElement


class TournamentPage(AppBasePage):
    """
        推荐页面
    """
    boot_ad = IdElement('com.vs.vipsai:id/btn_go')  # 启动页广告
    tournament_btn = XpathElement('(//android.widget.ImageView[@content-desc="唯赛"])[2]')
