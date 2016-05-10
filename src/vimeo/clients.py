# coding: utf-8

import json
import requests

from vimeo import exceptions
from vimeo import utils
from vimeo.logger import LoggerSingleton

# MAILUP CONFIGURATION FILE
_initial_client_configuration = {
    'VIMEO_END_POINTS': {
        'LOGON_END_POINT': 'https://services.mailup.com/Authorization/OAuth/LogOn',
    },
    'VIMEO_USERNAME': None,
    'VIMEO_PASSWORD': None,
}


class VimeoClient(object):

    # VIMEO LOGGER SINGLETON
    logger = None

    # VIMEO CONFIGURATION
    configuration_dict = _initial_client_configuration

    def __init__(self, username, password, logger_enabled=False):
        # Init Logger
        self.logger = LoggerSingleton()
        if not logger_enabled:
            self.logger.disabled = True

        self.configuration_dict['VIMEO_USERNAME'] = username
        self.configuration_dict['VIMEO_PASSWORD'] = password


