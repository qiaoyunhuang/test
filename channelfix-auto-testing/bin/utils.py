import os
import settings
import unittest
from datetime import datetime
import calendar
from BeautifulReport import BeautifulReport
import logging


def run_test(data, path, log_path):
    now = datetime.utcnow()
    timestamp = now.strftime('%Y-%m-%d-%H-%M-%S')
    context = dict()
    context.update({'timestamp': timestamp}, **data)
    description = """
        测试时间：{timestamp}
        测试平台：{platformName}
    """.format(**context)
    base_report_path = '{}/{}/{}/{}'.format(log_path, now.year, calendar.month_abbr[now.month], timestamp)
    exception_image_path = '{}/image/exception'.format(base_report_path)
    normal_image_path = '{}/image/normal'.format(base_report_path)
    for _path in (exception_image_path, normal_image_path):
        os.makedirs(_path)
    props = (
        ('BASE_REPORT_PATH', base_report_path),
        ('EXCEPTION_IMAGE_PATH', exception_image_path),
        ('NORMAL_IMAGE_PATH', normal_image_path),
    )
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, filename='{}/report.log'.format(base_report_path),
                        filemode='a', format=log_format)
    for prop in props:
        setattr(settings, prop[0], prop[1])
    test_suite = unittest.defaultTestLoader.discover(path, pattern='test_*.py')
    result = BeautifulReport(test_suite)
    result.report(
        filename='测试报告', description=description, report_dir=base_report_path)
