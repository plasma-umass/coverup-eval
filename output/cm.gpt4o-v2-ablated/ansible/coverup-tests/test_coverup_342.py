# file: lib/ansible/galaxy/api.py:56-60
# asked: {"lines": [56, 60], "branches": []}
# gained: {"lines": [56, 60], "branches": []}

import pytest
from ansible.galaxy.api import is_rate_limit_exception, GalaxyError

class MockGalaxyError(GalaxyError):
    def __init__(self, http_code):
        self.http_code = http_code

RETRY_HTTP_ERROR_CODES = [429, 503]

@pytest.mark.parametrize("exception,http_code,expected", [
    (MockGalaxyError(429), 429, True),
    (MockGalaxyError(503), 503, True),
    (MockGalaxyError(403), 403, False),
    (MockGalaxyError(401), 401, False),
    (Exception(), None, False),
])
def test_is_rate_limit_exception(monkeypatch, exception, http_code, expected):
    monkeypatch.setattr('ansible.galaxy.api.RETRY_HTTP_ERROR_CODES', RETRY_HTTP_ERROR_CODES)
    assert is_rate_limit_exception(exception) == expected
