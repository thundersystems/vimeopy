# coding: utf-8
"""
Exception
+-- VimeoException
    +-- ClientException
        +-- BadConfigurationException
        +-- HTTPErrorException
            +-- HTTPError400Exception
            +-- HTTPError403Exception
            +-- HTTPError404Exception
            +-- UnexpectedHTTPErrorException
        +-- HTTPMethodNotConfiguredException
        +-- HTTPMethodNotImplementedException
 """

from vimeo.logger import LoggerSingleton


# GENERIC EXCEPTION
class VimeoException(Exception):
    error_text = None

    def __init__(self, write_log=True):
        self.logger = LoggerSingleton()
        if write_log:
            self.write_log(self.error_text)

    def __str__(self):
        return repr(self.error_text)

    def __repr__(self):
        return repr(self.error_text)

    def write_log(self, msg):
        self.logger.error(msg)


# CLIENT GENERIC
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


# CLIENT BASE
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


# CLIENT HTTP
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


class HTTPErrorException(ClientException):
    """
    To import:
        from vimeo import exceptions

    To declare in a class add a class attribute:
        HTTPErrorException = exceptions.HTTPErrorException

    To raise:
        raise self.HTTPErrorException()
    """
    def __init__(self, response):
        self.response = response
        self.error_text = 'HTTP ERROR: {status_code} - DESCRIPTION: {error_msg} - URI: {url}'.format(
            status_code=self.response.status_code,
            error_msg=self.response.json()['error'],
            url=self.response.url
        )
        super(HTTPErrorException, self).__init__()


class HTTPError400Exception(HTTPErrorException):
    """
    To import:
        from vimeo import exceptions

    To declare in a class add a class attribute:
        HTTPError400Exception = exceptions.HTTPError400Exception

    To raise:
        raise self.HTTPError400Exception()
    """
    pass


class HTTPError403Exception(HTTPErrorException):
    """
    To import:
        from vimeo import exceptions

    To declare in a class add a class attribute:
        HTTPError403Exception = exceptions.HTTPError403Exception

    To raise:
        raise self.HTTPError403Exception()
    """
    pass


class HTTPError404Exception(HTTPErrorException):
    """
    To import:
        from vimeo import exceptions

    To declare in a class add a class attribute:
        HTTPError404Exception = exceptions.HTTPError404Exception

    To raise:
        raise self.HTTPError404Exception()
    """
    pass


class UnexpectedHTTPErrorException(HTTPErrorException):
    """
    To import:
        from vimeo import exceptions

    To declare in a class add a class attribute:
        UnexpectedHTTPErrorException = exceptions.UnexpectedHTTPErrorException

    To raise:
        raise self.UnexpectedHTTPErrorException()
    """
    pass

