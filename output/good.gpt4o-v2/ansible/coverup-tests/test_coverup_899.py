# file: lib/ansible/galaxy/api.py:56-60
# asked: {"lines": [56, 60], "branches": []}
# gained: {"lines": [56, 60], "branches": []}

import pytest
from ansible.galaxy.api import is_rate_limit_exception, GalaxyError

RETRY_HTTP_ERROR_CODES = [429, 520]

def test_is_rate_limit_exception_with_retry_code():
    class MockHttpError:
        def __init__(self, code):
            self.code = code
            self.reason = "Rate limit exceeded"
            self.url = "http://example.com/api/v2/"

        def read(self):
            return '{"message": "Rate limit exceeded"}'
        
        def geturl(self):
            return self.url

    exception = GalaxyError(MockHttpError(429), "Rate limit error")
    assert is_rate_limit_exception(exception) == True

def test_is_rate_limit_exception_with_non_retry_code():
    class MockHttpError:
        def __init__(self, code):
            self.code = code
            self.reason = "Forbidden"
            self.url = "http://example.com/api/v2/"

        def read(self):
            return '{"message": "Forbidden"}'
        
        def geturl(self):
            return self.url

    exception = GalaxyError(MockHttpError(403), "Forbidden error")
    assert is_rate_limit_exception(exception) == False

def test_is_rate_limit_exception_with_non_galaxy_error():
    class MockException(Exception):
        pass

    exception = MockException("Some other error")
    assert is_rate_limit_exception(exception) == False
