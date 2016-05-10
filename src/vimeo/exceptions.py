
# coding: utf-8

from vimeo.logger import LoggerSingleton


# GENERIC EXCEPTION
class VimeoException(Exception):
    error_text = None

    def __init__(self, write_log):
        self.logger = LoggerSingleton()
        if write_log:
            self.logger.error(self.error_text)

    def __str__(self):
        return repr(self.error_text)

    def __repr__(self):
        return repr(self.error_text)