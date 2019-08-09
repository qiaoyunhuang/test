from plex.base import AppBasePage
from plex.element import IdElement, AccessibilityIdElement


class LoginPage(AppBasePage):
    """
        登录页面
    """

    login_btn = IdElement('com.vs.vipsai:id/nav_item_me')
    profile_image = IdElement('com.vs.vipsai:id/fragment_main_user_home_protrait_bg_layout')
    profile_setting_btn = IdElement('com.vs.vipsai:id/fragment_main_user_home_btn_setting')
    logout_btn = IdElement('com.vs.vipsai:id/fragment_setttings_btn_logout')
    confirm_btn = IdElement('com.vs.vipsai:id/positive_btn')
    # qq登录相关按钮
    qq_login_btn = IdElement('com.vs.vipsai:id/activity_main_login_btn_qq')
    qq_username_input = AccessibilityIdElement('请输入QQ号码或手机或邮箱')
    qq_password_input = AccessibilityIdElement('密码 安全', need_shot=False)
    qq_login_submit_btn = AccessibilityIdElement('登录')

    def login(self, option, kwargs):
        getattr(self, 'login_{}'.format(option))(**kwargs)

    def login_qq(self, username, password):
        self.qq_login_btn.click()
        self.qq_username_input.send_keys(username)
        self.qq_password_input.send_keys(password)
        self.qq_login_submit_btn.click()

    def logout(self):
        self.profile_setting_btn.click()
        self.logout_btn.click()
        self.confirm_btn.click()
