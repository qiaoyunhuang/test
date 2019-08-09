from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Element:
    multi = False
    type = None
    func = None

    def __init__(self, value, need_shot=True):
        self.need_shot = need_shot
        self.value = value


class Elements(Element):
    multi = True


class IdElement(Element):
    type = By.ID
    func = 'find_element_by_id'


class ClassElement(Element):
    type = By.CLASS_NAME
    func = 'find_element_by_class_name'


class NameElement(Element):
    type = By.NAME
    func = 'find_element_by_name'


class XpathElement(Element):
    type = By.XPATH
    func = 'find_element_by_xpath'


class AccessibilityIdElement(Element):
    func = 'find_element_by_accessibility_id'


class PartialLinkTextElement(Element):
    type = By.PARTIAL_LINK_TEXT
    func = 'find_element_by_partial_link_text'


class ClassesElement(Elements):
    type = By.CLASS_NAME
    func = 'find_elements_by_class_name'

