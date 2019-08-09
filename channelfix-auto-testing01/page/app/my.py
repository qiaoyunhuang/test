from plex.base import AppBasePage
from plex.element import IdElement, AccessibilityIdElement, XpathElement
from plex.element import ClassElement


class MyPage(AppBasePage):
    """
        个人中心页面
    """
    boot_ad_close_btn = IdElement('com.vs.vipsai:id/img_home_popu_close')  # 关闭启动页广告
    my_btn = XpathElement('(//android.widget.ImageView[@content-desc="唯赛"])[4]')  # 我的
    # profile_dynamic_btn = IdElement('com.vs.vipsai:id/nav_tv_title')  # 动态按钮
    # profile_award_btn = IdElement('com.vs.vipsai:id/nav_tv_title')   # 获奖
    # profile_tournament_btn = IdElement('com.vs.vipsai:id/nav_tv_title')  # 比赛
    # profile_works_btn = IdElement('com.vs.vipsai:id/nav_tv_title')  # 作品
    # qq_login_btn = IdElement('com.vs.vipsai:id/activity_main_login_btn_qq')   # 选择QQ作为登录方式
    # login_btn = IdElement('com.tencent.mobileqq:id/login')  # 点击登录
    login_btn = IdElement('com.vs.vipsai:id/nav_item_me')
    profile_image = IdElement('com.vs.vipsai:id/fragment_main_user_home_protrait_bg_layout')
    profile_setting_btn = IdElement('com.vs.vipsai:id/fragment_main_user_home_btn_setting')
    logout_btn = IdElement('com.vs.vipsai:id/fragment_setttings_btn_logout')
    confirm_btn = IdElement('com.vs.vipsai:id/positive_btn')
    # qq登录相关按钮
    qq_login_btn = IdElement('com.vs.vipsai:id/activity_main_login_btn_qq')
    qq_username_input = AccessibilityIdElement('请输入QQ号码或手机或邮箱')
    qq_password_input = AccessibilityIdElement('密码 安全', need_shot=False)
    qq_login_submit_btn = AccessibilityIdElement('登 录')

