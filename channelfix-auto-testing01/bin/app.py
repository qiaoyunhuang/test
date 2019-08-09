import sys
import os
import re
import subprocess
from plex.utils import get_file
import settings
from bin.utils import run_test

sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
_shell = subprocess.run('adb devices', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
response = _shell.stdout
response = re.split(r'\n(?P<udid>[\w-]+)\t', response.decode('utf-8'))
data = [val for index, val in enumerate(response) if index % 2 != 0]
DEVICE_INFO = None


if len(data) == 0:
    print('please check the usb has connect to phone')
else:
    _data = get_file(filename='devices_info.json')
    DEVICE_INFO = [
        _data[udid] for udid in data
    ][0]
    # 暂时只支持单个手机测试
    setattr(settings, 'DEVICE_INFO', DEVICE_INFO)
    run_test(DEVICE_INFO, settings.APP_TEST_PATH, settings.APP_REPORT_PATH)
