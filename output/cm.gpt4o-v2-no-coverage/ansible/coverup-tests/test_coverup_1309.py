# file: lib/ansible/galaxy/api.py:56-60
# asked: {"lines": [60], "branches": []}
# gained: {"lines": [60], "branches": []}

import pytest
from ansible.errors import AnsibleError
from ansible.galaxy.api import is_rate_limit_exception
from ansible.galaxy.api import GalaxyError

RETRY_HTTP_ERROR_CODES = [429, 520]

def test_is_rate_limit_exception_with_retry_code():
    class MockHttpError:
        def __init__(self, code):
            self.code = code
            self.reason = "Too Many Requests"
            self.url = "http://example.com/api/v2/"

        def read(self):
            return '{"message": "Rate limit exceeded", "code": 429}'

        def geturl(self):
            return self.url

    exception = GalaxyError(MockHttpError(429), "Rate limit exceeded")
    assert is_rate_limit_exception(exception) is True

def test_is_rate_limit_exception_with_non_retry_code():
    class MockHttpError:
        def __init__(self, code):
            self.code = code
            self.reason = "Forbidden"
            self.url = "http://example.com/api/v2/"

        def read(self):
            return '{"message": "Forbidden", "code": 403}'

        def geturl(self):
            return self.url

    exception = GalaxyError(MockHttpError(403), "Forbidden")
    assert is_rate_limit_exception(exception) is False

def test_is_rate_limit_exception_with_non_galaxy_error():
    class NonGalaxyError(Exception):
        pass

    exception = NonGalaxyError("Some other error")
    assert is_rate_limit_exception(exception) is False
