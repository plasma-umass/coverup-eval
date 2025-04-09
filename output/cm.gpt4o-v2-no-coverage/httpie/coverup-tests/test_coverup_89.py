# file: httpie/utils.py:92-121
# asked: {"lines": [97, 99, 100, 102, 103, 104, 106, 108, 109, 112, 114, 115, 116, 117, 119, 120], "branches": []}
# gained: {"lines": [97, 99, 100, 102, 103, 104, 106, 108, 109, 112, 114, 115, 116, 117, 119, 120], "branches": []}

import pytest
import time
from httpie.utils import get_expired_cookies

def test_get_expired_cookies_no_cookies():
    headers = []
    assert get_expired_cookies(headers) == []

def test_get_expired_cookies_no_expired_cookies(monkeypatch):
    headers = [('Set-Cookie', 'cookie1=value1; Max-Age=3600')]
    now = time.time()

    def mock_time():
        return now

    monkeypatch.setattr(time, 'time', mock_time)
    assert get_expired_cookies(headers) == []

def test_get_expired_cookies_with_expired_cookies(monkeypatch):
    headers = [('Set-Cookie', 'cookie1=value1; Max-Age=0')]
    now = time.time()

    def mock_time():
        return now

    monkeypatch.setattr(time, 'time', mock_time)
    assert get_expired_cookies(headers) == [{'name': 'cookie1', 'path': '/'}]

def test_get_expired_cookies_with_mixed_cookies(monkeypatch):
    headers = [
        ('Set-Cookie', 'cookie1=value1; Max-Age=0'),
        ('Set-Cookie', 'cookie2=value2; Max-Age=3600')
    ]
    now = time.time()

    def mock_time():
        return now

    monkeypatch.setattr(time, 'time', mock_time)
    assert get_expired_cookies(headers) == [{'name': 'cookie1', 'path': '/'}]
