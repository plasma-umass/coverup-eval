# file: httpie/utils.py:92-121
# asked: {"lines": [97, 99, 100, 102, 103, 104, 106, 108, 109, 112, 114, 115, 116, 117, 119, 120], "branches": []}
# gained: {"lines": [97, 99, 100, 102, 103, 104, 106, 108, 109, 112, 114, 115, 116, 117, 119, 120], "branches": []}

import pytest
import time
from httpie.utils import get_expired_cookies

def test_get_expired_cookies():
    headers = [
        ('Set-Cookie', 'name=value; Expires=Wed, 09 Jun 2021 10:18:14 GMT'),
        ('Set-Cookie', 'name2=value2; Max-Age=3600'),
        ('Set-Cookie', 'name3=value3; Expires=Wed, 09 Jun 2021 10:18:14 GMT; Path=/test')
    ]
    
    # Mock current time to a fixed point
    fixed_time = 1623241094.0  # Corresponds to some fixed date/time
    expired_cookies = get_expired_cookies(headers, now=fixed_time)
    
    assert len(expired_cookies) == 2
    assert expired_cookies[0]['name'] == 'name'
    assert expired_cookies[0]['path'] == '/'
    assert expired_cookies[1]['name'] == 'name3'
    assert expired_cookies[1]['path'] == '/test'
