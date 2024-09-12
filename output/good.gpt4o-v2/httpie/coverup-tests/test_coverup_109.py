# file: httpie/utils.py:92-121
# asked: {"lines": [97, 99, 100, 102, 103, 104, 106, 108, 109, 112, 114, 115, 116, 117, 119, 120], "branches": []}
# gained: {"lines": [97, 99, 100, 102, 103, 104, 106, 108, 109, 112, 114, 115, 116, 117, 119, 120], "branches": []}

import pytest
import time
from httpie.utils import get_expired_cookies

def test_get_expired_cookies():
    headers = [
        ('Set-Cookie', 'name=value; expires=Wed, 09 Jun 2021 10:18:14 GMT'),
        ('Set-Cookie', 'name2=value2; max-age=3600'),
        ('Set-Cookie', 'name3=value3; path=/test')
    ]
    now = time.time()

    # Mock time to control the current time
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(time, 'time', lambda: now)

        expired_cookies = get_expired_cookies(headers, now=now + 7200)  # 2 hours later

        assert len(expired_cookies) == 1
        assert expired_cookies[0]['name'] == 'name'
        assert expired_cookies[0]['path'] == '/'

        non_expired_cookies = get_expired_cookies(headers, now=now + 1800)  # 30 minutes later

        assert len(non_expired_cookies) == 1
        assert non_expired_cookies[0]['name'] == 'name'
        assert non_expired_cookies[0]['path'] == '/'
