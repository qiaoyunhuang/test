from plex.base import AppBasePage
from plex.element import IdElement, AccessibilityIdElement, XpathElement
from plex.element import ClassElement


class ProfilePage(AppBasePage):
    """
        个人中心页面
    """
    boot_ad_close_btn = IdElement('com.vs.vipsai:id/img_home_popu_close')  # 关闭启动页广告
    profile_btn = XpathElement('(//android.widget.ImageView[@content-desc="唯赛"])[2]')  # 我的
    profile_dynamic_btn = IdElement('com.vs.vipsai:id/nav_tv_title')  # 动态按钮
    profile_award_btn = IdElement('com.vs.vipsai:id/nav_tv_title')   # 获奖
    profile_tournament_btn = IdElement('com.vs.vipsai:id/nav_tv_title')  # 比赛
    profile_works_btn = IdElement('com.vs.vipsai:id/nav_tv_title')  # 作品
    qq_login_btn = IdElement('com.vs.vipsai:id/activity_main_login_btn_qq')   # 选择QQ作为登录方式
    login_btn = XpathElement('/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.Button')  #点击登录




