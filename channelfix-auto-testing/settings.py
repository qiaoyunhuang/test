import os
from selenium import webdriver

HOST_NAME = 'https://ishowwang.com'

ROOT_PATH = os.path.dirname(__file__)

APP_PACKAGE_PATH = ROOT_PATH + '/resource/app_package'

BIN_PATH = ROOT_PATH + '/bin'

WD_HUB_URL = 'http://localhost:4723/wd/hub'

APP_TEST_PATH = ROOT_PATH + '/test/test_app/'

WEB_TEST_PATH = ROOT_PATH + '/test/test_web/'

APP_REPORT_PATH = ROOT_PATH + '/report/app/'

WEB_REPORT_PATH = ROOT_PATH + '/report/web/'

DEVICE_INFO = None
# 火狐,chrome等
WEB_DRIVERS = ((webdriver.Firefox, 'firefox'),)

WEB_DRIVER = None

NORMAL_IMAGE_PATH = None

EXCEPTION_IMAGE_PATH = None

BASE_REPORT_PATH = None

try:
    from local_settings import *
except ImportError:
    pass
