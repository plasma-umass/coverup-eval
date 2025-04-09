# file: httpie/utils.py:92-121
# asked: {"lines": [92, 94, 97, 99, 100, 102, 103, 104, 106, 108, 109, 112, 114, 115, 116, 117, 119, 120], "branches": []}
# gained: {"lines": [92, 94, 97, 99, 100, 102, 103, 104, 106, 108, 109, 112, 114, 115, 116, 117, 119, 120], "branches": []}

import pytest
import time
from httpie.utils import get_expired_cookies

def test_get_expired_cookies_no_cookies():
    headers = []
    result = get_expired_cookies(headers)
    assert result == []

def test_get_expired_cookies_no_expired_cookies(monkeypatch):
    headers = [('Set-Cookie', 'cookie1=value1; Max-Age=3600')]
    now = time.time()

    def mock_time():
        return now

    monkeypatch.setattr(time, 'time', mock_time)
    result = get_expired_cookies(headers, now)
    assert result == []

def test_get_expired_cookies_with_expired_cookies(monkeypatch):
    headers = [('Set-Cookie', 'cookie1=value1; Expires=Thu, 01 Jan 1970 00:00:00 GMT')]
    now = time.time()

    def mock_time():
        return now

    monkeypatch.setattr(time, 'time', mock_time)
    result = get_expired_cookies(headers, now)
    assert result == [{'name': 'cookie1', 'path': '/'}]

def test_get_expired_cookies_with_path(monkeypatch):
    headers = [('Set-Cookie', 'cookie1=value1; Expires=Thu, 01 Jan 1970 00:00:00 GMT; Path=/test')]
    now = time.time()

    def mock_time():
        return now

    monkeypatch.setattr(time, 'time', mock_time)
    result = get_expired_cookies(headers, now)
    assert result == [{'name': 'cookie1', 'path': '/test'}]
