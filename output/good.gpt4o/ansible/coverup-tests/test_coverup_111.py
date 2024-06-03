# file lib/ansible/module_utils/urls.py:1187-1228
# lines [1187, 1188, 1189, 1190, 1209, 1210, 1211, 1212, 1213, 1214, 1215, 1216, 1217, 1218, 1219, 1220, 1221, 1222, 1223, 1224, 1225, 1226, 1228]
# branches ['1210->1211', '1210->1212', '1225->1226', '1225->1228']

import pytest
from ansible.module_utils.urls import Request
from http.cookiejar import CookieJar

def test_request_initialization():
    # Test default initialization
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

    # Test initialization with headers
    r = Request(headers={'foo': 'bar'})
    assert r.headers == {'foo': 'bar'}

    # Test initialization with invalid headers
    with pytest.raises(ValueError, match="headers must be a dict: 'invalid'"):
        Request(headers='invalid')

    # Test initialization with cookies
    cj = CookieJar()
    r = Request(cookies=cj)
    assert r.cookies is cj

    # Test initialization with invalid cookies
    r = Request(cookies='invalid')
    assert isinstance(r.cookies, CookieJar)

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Add any necessary cleanup code here
