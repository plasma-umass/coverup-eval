# file mimesis/providers/internet.py:79-87
# lines [79, 87]
# branches []

import pytest
from mimesis.providers.internet import Internet

@pytest.fixture
def internet():
    return Internet()

def test_http_method(internet):
    from mimesis.data import HTTP_METHODS
    method = internet.http_method()
    assert method in HTTP_METHODS
