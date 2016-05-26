# coding: utf-8
"""
Exception
 +-- VimeoException
      +-- ClientException
           +-- BadConfigurationException
           +-- HTTPMethodNotConfiguredException
           +-- HTTPMethodNotImplementedException
 """

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


# CLIENT
class ClientException(VimeoException):
    """
    To import:
        from vimeo import exceptions

    To declare in a class add a class attribute:
        ClientException = exceptions.ClientException

    To raise:
        raise self.ClientException()
    """

    def __init__(self, error_text=None):
        if error_text:
            self.error_text = error_text
        super(ClientException, self).__init__()


class HTTPMethodNotConfiguredException(ClientException):
    """
    To import:
        from vimeo import exceptions

    To declare in a class add a class attribute:
        HTTPMethodNotConfiguredException = exceptions.HTTPMethodNotConfiguredException

    To raise:
        raise self.HTTPMethodNotConfiguredException()
    """

    def __init__(self, method_name, possible_methods):
        self.error_text = 'Method {method_name} not in possible methods: {possible_methods}'.format(
            method_name=method_name,
            possible_methods=possible_methods,
        )
        super(HTTPMethodNotConfiguredException, self).__init__()


class HTTPMethodNotImplementedException(ClientException):
    """
    To import:
        from vimeo import exceptions

    To declare in a class add a class attribute:
        HTTPMethodNotImplementedException = exceptions.HTTPMethodNotImplementedException

    To raise:
        raise self.HTTPMethodNotImplementedException()
    """

    def __init__(self, method_name):
        self.error_text = 'Method {method_name} not implemented in VimeoClient'.format(
            method_name=method_name,
        )
        super(HTTPMethodNotImplementedException, self).__init__()


class BadConfigurationException(ClientException):
    """
    To import:
        from vimeo import exceptions

    To declare in a class add a class attribute:
        BadConfigurationException = exceptions.BadConfigurationException

    To raise:
        raise self.BadConfigurationException()
    """

    def __init__(self):
        self.error_text = '"token" or ("key", "secret") not initialized'
        super(BadConfigurationException, self).__init__()


