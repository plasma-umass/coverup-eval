# file: lib/ansible/galaxy/api.py:56-60
# asked: {"lines": [56, 60], "branches": []}
# gained: {"lines": [56, 60], "branches": []}

import pytest
from ansible.galaxy.api import is_rate_limit_exception, GalaxyError

class MockHTTPError:
    def __init__(self, code, reason):
        self.code = code
        self.reason = reason

    def geturl(self):
        return "http://example.com"

    def read(self):
        return b'{"message": "Rate limit exceeded"}'

def test_is_rate_limit_exception_true():
    http_error = MockHTTPError(429, "Rate limit exceeded")
    exception = GalaxyError(http_error, "Rate limit error")
    assert is_rate_limit_exception(exception) is True

def test_is_rate_limit_exception_false_not_galaxy_error():
    class NotGalaxyError(Exception):
        def __init__(self, http_code):
            self.http_code = http_code

    exception = NotGalaxyError(429)
    assert is_rate_limit_exception(exception) is False

def test_is_rate_limit_exception_false_wrong_code():
    http_error = MockHTTPError(403, "Forbidden")
    exception = GalaxyError(http_error, "Forbidden error")
    assert is_rate_limit_exception(exception) is False
