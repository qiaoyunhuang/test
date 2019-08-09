import logging
import traceback
import unittest
from plex.utils import handle_screenshot
import settings


class LogForTestCase(type):
    def __new__(cls, name, bases, dct):
        if 'setUp' in dct:
            set_up = dct['setUp']
        else:
            set_up = lambda self: None

        def wrapped_set_up(self):
            logging.info('Test Case Start: {}'.format(repr(self)))
            set_up(self)

        dct['setUp'] = wrapped_set_up

        if 'tearDown' in dct:
            tear_down = dct['tearDown']
        else:
            tear_down = lambda self: None

        def wrapped_tear_down(self):
            tear_down(self)
            errors = self._outcome.errors
            val = None
            for error in errors:
                val = val or error[1]
            if val:
                etype, value, tb = val
                trace = ''.join(traceback.format_exception(etype=etype, value=value, tb=tb, limit=None))
                logging.error(trace)
                handle_screenshot(self.driver, settings.EXCEPTION_IMAGE_PATH)
            logging.info('Test Case Finish: {}'.format(repr(self)))

        dct['tearDown'] = wrapped_tear_down
        return type.__new__(cls, name, bases, dct)


class LoggedTestCase(unittest.TestCase, metaclass=LogForTestCase):
    pass
