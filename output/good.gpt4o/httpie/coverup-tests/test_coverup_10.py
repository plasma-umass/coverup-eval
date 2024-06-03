# file httpie/utils.py:92-121
# lines [92, 94, 97, 99, 100, 102, 103, 104, 106, 108, 109, 112, 114, 115, 116, 117, 119, 120]
# branches []

import pytest
from httpie.utils import get_expired_cookies
from unittest.mock import patch
import time

def test_get_expired_cookies(mocker):
    headers = [
        ('Set-Cookie', 'sessionid=abc123; Expires=Wed, 09 Jun 2021 10:18:14 GMT; Path=/'),
        ('Set-Cookie', 'userid=xyz789; Max-Age=3600; Path=/')
    ]

    # Mock time to control the current time
    mock_now = 1623233894.0  # This is a fixed timestamp for testing
    mocker.patch('time.time', return_value=mock_now)

    # Mock _max_age_to_expires to convert Max-Age to Expires
    def mock_max_age_to_expires(cookies, now):
        for cookie in cookies:
            if 'Max-Age' in cookie:
                cookie['expires'] = now + int(cookie['Max-Age'])

    mocker.patch('httpie.utils._max_age_to_expires', side_effect=mock_max_age_to_expires)

    expired_cookies = get_expired_cookies(headers)

    assert len(expired_cookies) == 1
    assert expired_cookies[0]['name'] == 'sessionid'
    assert expired_cookies[0]['path'] == '/'

    # Clean up
    mocker.stopall()
