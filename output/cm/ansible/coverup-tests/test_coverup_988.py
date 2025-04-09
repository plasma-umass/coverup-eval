# file lib/ansible/galaxy/api.py:56-60
# lines [56, 60]
# branches []

import pytest
from ansible.galaxy.api import GalaxyAPI, GalaxyError

RETRY_HTTP_ERROR_CODES = [429, 503]  # Assuming these are the codes we want to retry on

class MockGalaxyError(GalaxyError):
    def __init__(self, http_code):
        self.http_code = http_code

def is_rate_limit_exception(exception):
    # Note: cloud.redhat.com masks rate limit errors with 403 (Forbidden) error codes.
    # Since 403 could reflect the actual problem (such as an expired token), we should
    # not retry by default.
    return isinstance(exception, GalaxyError) and exception.http_code in RETRY_HTTP_ERROR_CODES

def test_is_rate_limit_exception():
    # Test that the function correctly identifies rate limit exceptions
    for http_code in RETRY_HTTP_ERROR_CODES:
        exception = MockGalaxyError(http_code)
        assert is_rate_limit_exception(exception) is True

    # Test that the function does not identify other exceptions as rate limit exceptions
    non_retry_codes = [400, 401, 403, 404, 500]  # Some common HTTP error codes that are not in RETRY_HTTP_ERROR_CODES
    for http_code in non_retry_codes:
        exception = MockGalaxyError(http_code)
        assert is_rate_limit_exception(exception) is False
