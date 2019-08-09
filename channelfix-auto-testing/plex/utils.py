import os
import platform
from appium import webdriver
import settings
import anyjson as json
from datetime import datetime


def get_app_package(data):
    system = platform.system()
    mobile_os = 'android' if system == 'Windows' or system == 'Linux' \
        else 'ios'
    path = os.path.join(settings.APP_PACKAGE_PATH, mobile_os)
    mobile_os = mobile_os[0].upper() + mobile_os[1:]
    if mobile_os != data['platformName']:
        raise Exception
    packages = os.listdir(path)

    return [
        handle_filename(path, package) for package in packages
    ]


def handle_filename(path, filename):
    package_type, version = filename.split('_')
    return {
        'type': package_type,
        'version': version,
        'path': os.path.join(path, filename)
    }


def get_desired_caps(automation_name='Appium', no_reset=True):
    data = settings.DEVICE_INFO.copy()
    if data:
        app_path = get_app_package(data)[0]['path']
        data.update(
            {
                'automationName': automation_name,
                'noReset': no_reset,
                'app': app_path
            }
        )
        return data
    else:
        raise AttributeError


def get_driver(**kwargs):
    try:
        return webdriver.Remote(settings.WD_HUB_URL, get_desired_caps(**kwargs))
    except AttributeError as e:
        return None


def get_file(root_path=settings.ROOT_PATH, filename=None, parser=json.loads):
    _file = os.path.join(root_path, filename)
    # for windows, has encoding issue, add 'utf-8' limit.
    with open(_file, encoding='utf-8') as file:
        return parser(file.read())


def handle_screenshot(driver, path):
    timestamp = datetime.utcnow().strftime('%Y-%m-%d-%H-%M-%S')
    file_name = '{}.png'.format(timestamp)
    driver.get_screenshot_as_file('{}/{}'.format(path, file_name))
