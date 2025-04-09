# file mimesis/providers/internet.py:79-87
# lines [79, 87]
# branches []

import pytest
from mimesis.providers.internet import Internet

HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS', 'TRACE', 'CONNECT']

@pytest.fixture
def internet_provider():
    return Internet()

def test_http_method(internet_provider):
    method = internet_provider.http_method()
    assert method in HTTP_METHODS
