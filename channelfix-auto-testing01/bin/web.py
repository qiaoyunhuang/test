import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
import settings
from bin.utils import run_test


for driver in settings.WEB_DRIVERS:
    setattr(settings, 'WEB_DRIVER', driver[0])
    data = {
        'platformName': 'web-{}'.format(driver[1]),
    }
    run_test(data, settings.WEB_TEST_PATH, settings.WEB_REPORT_PATH)
