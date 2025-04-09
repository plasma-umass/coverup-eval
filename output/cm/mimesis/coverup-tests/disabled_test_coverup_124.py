# file mimesis/providers/internet.py:69-77
# lines [69, 77]
# branches []

import pytest
from mimesis.providers.internet import Internet

# Assuming HTTP_STATUS_CODES is a list of integers representing HTTP status codes.
HTTP_STATUS_CODES = [100, 101, 200, 201, 202, 204, 301, 302, 400, 401, 403, 404, 500, 501, 503]

@pytest.fixture
def internet_provider():
    return Internet()

def test_http_status_code(internet_provider):
    status_code = internet_provider.http_status_code()
    assert status_code in HTTP_STATUS_CODES
