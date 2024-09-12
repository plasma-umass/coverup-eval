# file: httpie/utils.py:124-136
# asked: {"lines": [124, 131, 132, 133, 134, 135, 136], "branches": [[131, 0], [131, 132], [132, 133], [132, 134], [135, 131], [135, 136]]}
# gained: {"lines": [124, 131, 132, 133, 134, 135, 136], "branches": [[131, 0], [131, 132], [132, 133], [132, 134], [135, 131], [135, 136]]}

import pytest
from datetime import datetime, timedelta
from httpie.utils import _max_age_to_expires

def test_max_age_to_expires_with_expires():
    cookies = [{'expires': 'some_value', 'max-age': '10'}]
    now = datetime.now().timestamp()
    _max_age_to_expires(cookies, now)
    assert 'expires' in cookies[0]
    assert cookies[0]['expires'] == 'some_value'

def test_max_age_to_expires_with_max_age():
    cookies = [{'max-age': '10'}]
    now = datetime.now().timestamp()
    _max_age_to_expires(cookies, now)
    assert 'expires' in cookies[0]
    assert cookies[0]['expires'] == now + 10.0

def test_max_age_to_expires_with_non_digit_max_age():
    cookies = [{'max-age': 'non_digit'}]
    now = datetime.now().timestamp()
    _max_age_to_expires(cookies, now)
    assert 'expires' not in cookies[0]

def test_max_age_to_expires_without_expires_or_max_age():
    cookies = [{}]
    now = datetime.now().timestamp()
    _max_age_to_expires(cookies, now)
    assert 'expires' not in cookies[0]
