# file httpie/utils.py:68-74
# lines [74]
# branches []

import pytest
from httpie.utils import ExplicitNullAuth
from requests import Request

@pytest.fixture
def mock_request():
    return Request()

def test_explicit_null_auth(mock_request):
    auth = ExplicitNullAuth()
    modified_request = auth(mock_request)
    assert modified_request is mock_request
