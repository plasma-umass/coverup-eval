# file httpie/utils.py:124-136
# lines [124, 131, 132, 133, 134, 135, 136]
# branches ['131->exit', '131->132', '132->133', '132->134', '135->131', '135->136']

import pytest
from datetime import datetime, timedelta
from httpie.utils import _max_age_to_expires

def test_max_age_to_expires():
    now = datetime.now().timestamp()
    cookies = [
        {'name': 'cookie1', 'max-age': '3600'},
        {'name': 'cookie2', 'expires': now + 7200},
        {'name': 'cookie3', 'max-age': 'not_a_digit'},
        {'name': 'cookie4', 'max-age': '1800'}
    ]

    _max_age_to_expires(cookies, now)

    assert 'expires' in cookies[0]
    assert cookies[0]['expires'] == now + 3600
    assert 'expires' in cookies[1]
    assert cookies[1]['expires'] == now + 7200
    assert 'expires' not in cookies[2]
    assert 'expires' in cookies[3]
    assert cookies[3]['expires'] == now + 1800
