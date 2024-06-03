# file mimesis/providers/internet.py:69-77
# lines [69, 77]
# branches []

import pytest
from mimesis.providers.internet import Internet
from mimesis.data import HTTP_STATUS_CODES

@pytest.fixture
def internet():
    return Internet()

def test_http_status_code(internet):
    status_code = internet.http_status_code()
    assert status_code in HTTP_STATUS_CODES
