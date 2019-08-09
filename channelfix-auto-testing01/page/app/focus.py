from plex.base import AppBasePage
from plex.element import IdElement, AccessibilityIdElement, XpathElement, ClassElement


class LoginPage(AppBasePage):
    """
        登录页面
    """
    popup_close = IdElement('com.vs.vipsai:id/img_home_popu_close')  # 关闭广告页“×”元素
    my_btn = XpathElement('(//android.widget.ImageView[@content-desc="唯赛"])[2]')  # “我的”元素

    # qq登录相关按钮
    qq_login_btn = IdElement('com.vs.vipsai:id/activity_main_login_btn_qq')
    qq_username_input = AccessibilityIdElement('请输入QQ号码或手机或邮箱')
    qq_password_input = AccessibilityIdElement('密码 安全', need_shot=False)
    qq_login_submit_btn = AccessibilityIdElement('登 录')

    #qq退出相关按钮
    profile_setting_btn = IdElement('com.vs.vipsai:id/fragment_main_user_home_image_setting') # 我的-设置按钮
    logout_btn = IdElement('com.vs.vipsai:id/fragment_setttings_btn_logout')  # 退出账户按钮
    confirm_btn = IdElement('com.vs.vipsai:id/positive_btn')  # 提示框确定按钮

    # 未登录状态下-关注页面
    walk_around_btn = IdElement('com.vs.vipsai:id/walk_around')  # 随便逛逛 按钮
    # 关注
    focus_btn = XpathElement('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[2]')
    login_focus_btn = IdElement('com.vs.vipsai:idn_error_layout')  # 未登录时，在关注页面的 登录按钮
    # QQ已登录时，QQ授权登录微赛按钮
    qq_again_login_btn = XpathElement('/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.Button')
