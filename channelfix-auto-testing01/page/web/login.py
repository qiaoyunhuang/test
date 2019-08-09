from plex.base import WebBasePage
from plex.element import ClassElement, ClassesElement, IdElement,AccessibilityIdElement
import settings


class LoginPage(WebBasePage):
    """
        登录弹窗
    """
    url = settings.HOST_NAME
    login_popup = IdElement('loginpopup')
    login_btn = ClassElement('create-account')
    login_qq = ClassElement('fa-qq')
    qq_login_btn = IdElement('switcher_plogin')
    qq_username_input = ClassElement('inputstyle')
    qq_password_input = ClassElement('inputstyle password')
    qq_login_submit_btn = IdElement('login_button')



