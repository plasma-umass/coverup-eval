# file lib/ansible/galaxy/api.py:56-60
# lines [56, 60]
# branches []

import pytest
from ansible.galaxy.api import is_rate_limit_exception, GalaxyError

class MockGalaxyError(GalaxyError):
    def __init__(self, http_code):
        self.http_code = http_code

RETRY_HTTP_ERROR_CODES = [429, 503]

def test_is_rate_limit_exception_retry_code():
    exception = MockGalaxyError(429)
    assert is_rate_limit_exception(exception) == True

def test_is_rate_limit_exception_non_retry_code():
    exception = MockGalaxyError(403)
    assert is_rate_limit_exception(exception) == False

def test_is_rate_limit_exception_non_galaxy_error():
    class NonGalaxyError(Exception):
        pass
    exception = NonGalaxyError()
    assert is_rate_limit_exception(exception) == False
