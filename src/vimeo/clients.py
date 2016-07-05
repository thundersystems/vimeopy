# coding: utf-8

import json
import logging
import requests

from functools import wraps

from vimeo import exceptions
from vimeo.logger import LoggerSingleton
from vimeo.mixins import VimeoClientMethodMixin

# VIMEO-CLIENT CONFIGURATION FILE: the changes affect all instances, singleton and not singleton
_initial_client_configuration = {
    'API_ROOT': 'https://api.vimeo.com',
    'HTTP_METHODS': {'head', 'get', 'post', 'put', 'patch', 'options', 'delete'},  # set
    'ACCEPT_HEADER': "application/vnd.vimeo.*;version=3.2",
    'USER_AGENT': "pyvimeo 0.1; (http://developer.vimeo.com/api/docs)",
    'TIMEOUT': (1, 30),
}


class VimeoAuth(requests.auth.AuthBase):
    """
    Custom Authentication Class, docs at:
    http://docs.python-requests.org/en/master/user/authentication/#new-forms-of-authentication
    """
    def __init__(self, token):
        self.token = token

    def __call__(self, request):
        """
        Calling VimeoAuth, request headers is updated.
        Call Example:
        request = VimeoAuth(request)

        :param request:
        :return:
        """
        request.headers['Authorization'] = 'Bearer ' + self.token
        return request


class VimeoClient(VimeoClientMethodMixin):

    # VIMEO LOGGER
    logger = None

    # VIMEO CONFIGURATION
    configuration_dict = _initial_client_configuration

    def __init__(self, token=None, key=None, secret=None, **kwargs):
        # Init Logger
        logger_enabled = kwargs.get('logger_enabled', False)
        logger_level = kwargs.get('logger_level', logging.INFO)
        self.logger = LoggerSingleton(
            enabled=logger_enabled,
            level=logger_level,
        )

        self.token = token

        # Instance of VimeoAuth
        self.auth_instance = VimeoAuth(token) if token else None

        self.app_info = (key, secret)

        # Make sure we have enough info to be useful.
        try:
            assert token is not None or (key is not None and secret is not None)
        except AssertionError:
            raise exceptions.BadConfigurationException()

    def __getattr__(self, name):
        """
        Called when an attribute lookup has not found
        """

        if name in self.configuration_dict.keys():
            return self.configuration_dict[name]

        if name in self.configuration_dict['HTTP_METHODS']:
            http_method = name
            request_method = getattr(requests, http_method, None)
            if not request_method:
                raise exceptions.HTTPMethodNotImplementedException(
                    method_name=http_method,
                )

            @wraps(request_method)
            def caller(url, jsonify=True, **kwargs):
                """
                Call request_method after update:
                 - headers
                 - kwargs
                 - url
                """
                headers = kwargs.get('headers', dict())
                headers['Accept'] = self.configuration_dict['ACCEPT_HEADER']
                headers['User-Agent'] = self.configuration_dict['USER_AGENT']

                if jsonify and 'data' in kwargs and isinstance(kwargs['data'], (dict, list)):
                    kwargs['data'] = json.dumps(kwargs['data'])
                    headers['Content-Type'] = 'application/json'

                kwargs['timeout'] = kwargs.get('timeout', self.configuration_dict['TIMEOUT'])
                kwargs['auth'] = kwargs.get('auth', self.auth_instance)
                kwargs['headers'] = headers
                url = self.API_ROOT + url

                return request_method(url, **kwargs)

            # wrapped method of requests (GET, POST, ..) is returned
            return caller


class VimeoClientSingleton(object):

    _client = None

    def __new__(cls, token=None, key=None, secret=None, **kwargs):
        if not cls._client:
            cls._client = VimeoClient(token=token, key=key, secret=secret, **kwargs)
            return cls._client
        else:
            return cls._client
