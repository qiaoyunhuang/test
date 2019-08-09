from plex.base import AppBasePage
from plex.element import IdElement, AccessibilityIdElement, XpathElement
from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction

class BootAdPage(AppBasePage):
    """
        启动广告页面测试
    """
    boot_ad = IdElement('com.vs.vipsai:id/btn_go')  # 启动页广告
    boot_ad_close_btn = IdElement('com.vs.vipsai:id/img_home_popu_close')  # 关闭广告
    boot_ad_skin_btn = XpathElement('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.TextView[1]')
    boot_ad_img_btn = XpathElement('com.vs.vipsai:id/img_home_adv')
    boot_ad_go_btn = XpathElement('com.vs.vipsai:id/btn_go')