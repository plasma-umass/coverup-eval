# file: lib/ansible/module_utils/urls.py:1187-1228
# asked: {"lines": [1187, 1188, 1189, 1190, 1209, 1210, 1211, 1212, 1213, 1214, 1215, 1216, 1217, 1218, 1219, 1220, 1221, 1222, 1223, 1224, 1225, 1226, 1228], "branches": [[1210, 1211], [1210, 1212], [1225, 1226], [1225, 1228]]}
# gained: {"lines": [1187, 1188, 1189, 1190, 1209, 1210, 1211, 1212, 1213, 1214, 1215, 1216, 1217, 1218, 1219, 1220, 1221, 1222, 1223, 1224, 1225, 1226, 1228], "branches": [[1210, 1211], [1210, 1212], [1225, 1226], [1225, 1228]]}

import pytest
import ansible.module_utils.six.moves.http_cookiejar as cookiejar
from ansible.module_utils.urls import Request

def test_request_init_default():
    r = Request()
    assert r.headers == {}
    assert r.use_proxy is True
    assert r.force is False
    assert r.timeout == 10
    assert r.validate_certs is True
    assert r.url_username is None
    assert r.url_password is None
    assert r.http_agent is None
    assert r.force_basic_auth is False
    assert r.follow_redirects == 'urllib2'
    assert r.client_cert is None
    assert r.client_key is None
    assert r.unix_socket is None
    assert r.ca_path is None
    assert isinstance(r.cookies, cookiejar.CookieJar)

def test_request_init_custom_headers():
    r = Request(headers={'foo': 'bar'})
    assert r.headers == {'foo': 'bar'}

def test_request_init_invalid_headers():
    with pytest.raises(ValueError, match="headers must be a dict: 'invalid'"):
        Request(headers='invalid')

def test_request_init_custom_cookies():
    custom_cookies = cookiejar.CookieJar()
    r = Request(cookies=custom_cookies)
    assert r.cookies is custom_cookies

def test_request_init_invalid_cookies():
    r = Request(cookies='invalid')
    assert isinstance(r.cookies, cookiejar.CookieJar)
