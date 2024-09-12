# file: lib/ansible/module_utils/urls.py:1187-1228
# asked: {"lines": [1211, 1226], "branches": [[1210, 1211], [1225, 1226]]}
# gained: {"lines": [1211, 1226], "branches": [[1210, 1211], [1225, 1226]]}

import pytest
import ansible.module_utils.six.moves.http_cookiejar as cookiejar
from ansible.module_utils.urls import Request

def test_request_headers_not_dict():
    with pytest.raises(ValueError, match="headers must be a dict: 'not_a_dict'"):
        Request(headers='not_a_dict')

def test_request_cookies_is_cookiejar():
    cj = cookiejar.CookieJar()
    req = Request(cookies=cj)
    assert req.cookies is cj

def test_request_cookies_is_not_cookiejar():
    req = Request(cookies='not_a_cookiejar')
    assert isinstance(req.cookies, cookiejar.CookieJar)
