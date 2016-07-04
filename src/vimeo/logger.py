# coding: utf-8

import logging


class Logger(object):
    """
    Logger
    """

    _logger = None

    def __new__(cls, logger=None):
        logger_manager = LoggerManager(logger)
        cls._logger = logger_manager.logger
        return cls._logger


class LoggerSingleton(object):
    """
    Singleton logger
    """

    _logger = None

    def __new__(cls, logger=None, **kwargs):
        if not cls._logger:
            logger_manager = LoggerManager(logger, **kwargs)
            cls._logger = logger_manager.logger
            return cls._logger
        else:
            cls._logger.debug('Singleton logger is already created')
            return cls._logger


class LoggerManager(object):
    logger = None

    def __init__(self, logger=None, enabled=False, level=logging.INFO):
        # build logger
        if logger:
            self.logger = logger
        else:
            self.set_default_logger(enabled=enabled, level=level)

    def set_default_logger(self, enabled=False, level=logging.INFO):
            logger = logging.getLogger('default_logger')
            logger.setLevel(level)
            console_handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s')
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

            self.logger = logger
            self.logger.disabled = not enabled
