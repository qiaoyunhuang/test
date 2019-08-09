from plex.element import Element, ClassElement, IdElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from plex.utils import handle_screenshot
from selenium.common.exceptions import TimeoutException
import settings
import logging
import traceback


class BasePage:
    """
        基础页面类
    """
    popup_close = None

    def __init__(self, driver):
        self.driver = driver

    def __getattribute__(self, item):
        obj = super().__getattribute__(item)
        if isinstance(obj, Element):
            return self.find_element(obj)
        return obj

    def find_element(self, path):
        if path.type:
            try:
                WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located(
                        (path.type, path.value))
                )
            except TimeoutException as e:
                logging.error(traceback.format_exc())
                handle_screenshot(self.driver, settings.EXCEPTION_IMAGE_PATH)
        _fun = getattr(self.driver, path.func)
        element = _fun(path.value)
        # need auto screenshot
        if not path.need_shot:
            return element
        for action in ['click', 'send_keys']:
            fun = getattr(element, action)

            def wrap(args=None, _fun=fun, _action=action):
                if args:
                    _fun(args)
                else:
                    _fun()
                handle_screenshot(self.driver, settings.NORMAL_IMAGE_PATH)
            setattr(element, action, wrap)
        return element

    def close(self):
        self.driver.quit()

    def click_event(self, element):
        element.click()

    def close_popup(self):
        if self.popup_close:
            self.popup_close.click()


class WebBasePage(BasePage):
    """web页面基类"""
    url = None
    popup_close = ClassElement('popup__close')

    def __init__(self, driver):
        super().__init__(driver)
        if self.url:
            self.driver.get(self.url)


class AppBasePage(BasePage):
    """App页面基类"""
    popup_close = IdElement('com.vs.vipsai:id/img_home_popu_close')
