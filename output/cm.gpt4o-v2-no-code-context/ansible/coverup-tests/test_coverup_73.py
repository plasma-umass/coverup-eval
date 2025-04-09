# file: lib/ansible/module_utils/urls.py:1187-1228
# asked: {"lines": [1187, 1188, 1189, 1190, 1209, 1210, 1211, 1212, 1213, 1214, 1215, 1216, 1217, 1218, 1219, 1220, 1221, 1222, 1223, 1224, 1225, 1226, 1228], "branches": [[1210, 1211], [1210, 1212], [1225, 1226], [1225, 1228]]}
# gained: {"lines": [1187, 1188, 1189, 1190, 1209, 1210, 1211, 1212, 1213, 1214, 1215, 1216, 1217, 1218, 1219, 1220, 1221, 1222, 1223, 1224, 1225, 1226, 1228], "branches": [[1210, 1211], [1210, 1212], [1225, 1226], [1225, 1228]]}

import pytest
from ansible.module_utils.urls import Request
from http.cookiejar import CookieJar

def test_request_initialization_defaults(monkeypatch):
    # Mock os.devnull to avoid FileNotFoundError
    monkeypatch.setattr('os.devnull', '/tmp/devnull')
    with open('/tmp/devnull', 'w') as f:
        pass

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
    assert isinstance(r.cookies, CookieJar)

def test_request_initialization_with_headers(monkeypatch):
    # Mock os.devnull to avoid FileNotFoundError
    monkeypatch.setattr('os.devnull', '/tmp/devnull')
    with open('/tmp/devnull', 'w') as f:
        pass

    r = Request(headers={'foo': 'bar'})
    assert r.headers == {'foo': 'bar'}

def test_request_initialization_with_invalid_headers(monkeypatch):
    # Mock os.devnull to avoid FileNotFoundError
    monkeypatch.setattr('os.devnull', '/tmp/devnull')
    with open('/tmp/devnull', 'w') as f:
        pass

    with pytest.raises(ValueError, match="headers must be a dict"):
        Request(headers='invalid_headers')

def test_request_initialization_with_cookies(monkeypatch):
    # Mock os.devnull to avoid FileNotFoundError
    monkeypatch.setattr('os.devnull', '/tmp/devnull')
    with open('/tmp/devnull', 'w') as f:
        pass

    cj = CookieJar()
    r = Request(cookies=cj)
    assert r.cookies is cj

def test_request_initialization_with_none_cookies(monkeypatch):
    # Mock os.devnull to avoid FileNotFoundError
    monkeypatch.setattr('os.devnull', '/tmp/devnull')
    with open('/tmp/devnull', 'w') as f:
        pass

    r = Request(cookies=None)
    assert isinstance(r.cookies, CookieJar)
