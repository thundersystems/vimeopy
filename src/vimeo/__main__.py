# coding: utf-8

import getopt
import logging
import sys
import unittest

from vimeo.logger import LoggerSingleton
LOGGER_SINGLETON = LoggerSingleton()
LOG_LEVEL_DICT = {
    'CRITICAL': 50,
    'ERROR': 40,
    'WARNING': 30,
    'INFO': 20,
    'DEBUG': 10,
    'NOTSET': 0,
}

# STATIC VAR
LOG_LEVEL = None
LOGGER_ENABLED = False
TOKEN = None


class TestVimeopyBase(unittest.TestCase):
    def __init__(self, methodName='runTest'):

        # CLIENT
        from vimeo.clients import VimeoClientSingleton
        self.client = VimeoClientSingleton(
            token=TOKEN,
            logger_enabled=LOGGER_ENABLED,
            logger_level=LOG_LEVEL,
        )

        # SETTING LOG
        LOGGER_SINGLETON.setLevel(LOG_LEVEL)
        if LOGGER_ENABLED:
            LOGGER_SINGLETON.disabled = False
        else:
            LOGGER_SINGLETON.disabled = True
        super(TestVimeopyBase, self).__init__(methodName)


class TestReadUser(TestVimeopyBase):
    def test_dummy(self):
        try:
            self.client.read_user()
        except Exception as e:
            LOGGER_SINGLETON.error(getattr(e, 'error_text'))
        return True


if __name__ == '__main__':

    opts, args = getopt.getopt(sys.argv[1:], '', [
        'token=',
        'log-level=',
        'logger-enabled',
    ])

    for option, value in opts:
        if option == '--token':
            TOKEN = value
        if option == '--logger-enabled':
            LOGGER_ENABLED = True
        if option == '--log-level':
            LOGGER_ENABLED = True
            if value in LOG_LEVEL_DICT.keys():
                LOG_LEVEL = LOG_LEVEL_DICT[value]
            if value in LOG_LEVEL_DICT.values():
                LOG_LEVEL = value

    if not LOG_LEVEL:
        LOG_LEVEL = LOG_LEVEL_DICT['INFO']

    if not TOKEN:
        LOGGER_SINGLETON.error('Token is required')
    else:
        del sys.argv[1:]
        unittest.main()

