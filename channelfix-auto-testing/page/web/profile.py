from plex.base import WebBasePage
from plex.element import ClassElement, ClassesElement
import settings


class ProfilePage(WebBasePage):
    """
        个人详情页
    """
    url = '{}/profile/chand/'.format(settings.HOST_NAME)
    third_party_btn = ClassElement('third-party-links a')
    stat_box = ClassElement('stat-box')
    click_tabs_item = ClassesElement('tabs__item')
    weibo_logo_btn = ClassElement('gn_logo')
