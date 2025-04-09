# file: lib/ansible/galaxy/api.py:56-60
# asked: {"lines": [56, 60], "branches": []}
# gained: {"lines": [56, 60], "branches": []}

import pytest
from ansible.galaxy.api import is_rate_limit_exception, GalaxyError

class MockGalaxyError(GalaxyError):
    def __init__(self, http_code):
        self.http_code = http_code

def test_is_rate_limit_exception_with_retry_code():
    retry_code = 429  # Assuming 429 is in RETRY_HTTP_ERROR_CODES
    exception = MockGalaxyError(http_code=retry_code)
    assert is_rate_limit_exception(exception) is True

def test_is_rate_limit_exception_with_non_retry_code():
    non_retry_code = 403  # Assuming 403 is not in RETRY_HTTP_ERROR_CODES
    exception = MockGalaxyError(http_code=non_retry_code)
    assert is_rate_limit_exception(exception) is False

def test_is_rate_limit_exception_with_non_galaxy_error():
    class NonGalaxyError(Exception):
        pass

    exception = NonGalaxyError()
    assert is_rate_limit_exception(exception) is False
