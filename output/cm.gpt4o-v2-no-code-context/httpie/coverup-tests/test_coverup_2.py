# file: httpie/utils.py:124-136
# asked: {"lines": [124, 131, 132, 133, 134, 135, 136], "branches": [[131, 0], [131, 132], [132, 133], [132, 134], [135, 131], [135, 136]]}
# gained: {"lines": [124, 131, 132, 133, 134, 135, 136], "branches": [[131, 0], [131, 132], [132, 133], [132, 134], [135, 131], [135, 136]]}

import pytest
from datetime import datetime, timedelta

# Assuming the function _max_age_to_expires is imported from httpie/utils.py
from httpie.utils import _max_age_to_expires

def test_max_age_to_expires_with_expires(monkeypatch):
    now = datetime.now().timestamp()
    cookies = [{'expires': now + 1000}]
    
    _max_age_to_expires(cookies, now)
    
    assert 'expires' in cookies[0]
    assert cookies[0]['expires'] == now + 1000

def test_max_age_to_expires_with_max_age(monkeypatch):
    now = datetime.now().timestamp()
    cookies = [{'max-age': '1000'}]
    
    _max_age_to_expires(cookies, now)
    
    assert 'expires' in cookies[0]
    assert cookies[0]['expires'] == now + 1000

def test_max_age_to_expires_with_non_digit_max_age(monkeypatch):
    now = datetime.now().timestamp()
    cookies = [{'max-age': 'abc'}]
    
    _max_age_to_expires(cookies, now)
    
    assert 'expires' not in cookies[0]

def test_max_age_to_expires_with_no_max_age_or_expires(monkeypatch):
    now = datetime.now().timestamp()
    cookies = [{}]
    
    _max_age_to_expires(cookies, now)
    
    assert 'expires' not in cookies[0]
