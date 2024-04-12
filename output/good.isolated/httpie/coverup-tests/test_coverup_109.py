# file httpie/utils.py:92-121
# lines [97, 99, 100, 102, 103, 104, 106, 108, 109, 112, 114, 115, 116, 117, 119, 120]
# branches []

import pytest
from httpie.utils import get_expired_cookies
from unittest.mock import patch
import time

@pytest.fixture
def mock_time(mocker):
    mock = mocker.patch('httpie.utils.time.time')
    mock.return_value = 1500000000.0  # Set to a time after the expiry of the first cookie
    return mock

def test_get_expired_cookies(mock_time):
    headers = [
        ('Set-Cookie', 'session=abc123; Expires=Wed, 21 Oct 2015 07:28:00 GMT; Path=/'),
        ('Set-Cookie', 'id=xyz789; Expires=Wed, 21 Oct 2099 07:28:00 GMT; Path=/'),
    ]
    expired_cookies = get_expired_cookies(headers)
    assert len(expired_cookies) == 1
    assert expired_cookies[0]['name'] == 'session'
    assert expired_cookies[0]['path'] == '/'
    mock_time.assert_called_once()
