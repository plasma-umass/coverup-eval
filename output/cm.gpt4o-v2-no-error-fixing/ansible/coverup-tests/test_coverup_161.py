# file: lib/ansible/module_utils/urls.py:1522-1541
# asked: {"lines": [1522, 1523, 1524, 1525, 1526, 1527, 1528, 1534, 1535, 1536, 1537, 1538, 1539, 1540, 1541], "branches": []}
# gained: {"lines": [1522, 1523, 1524, 1525, 1526, 1527, 1528, 1534, 1535, 1536, 1537, 1538, 1539, 1540, 1541], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.urls import open_url

@pytest.fixture
def mock_request_open():
    with patch('ansible.module_utils.urls.Request.open') as mock:
        yield mock

def test_open_url_get_request(mock_request_open):
    url = 'http://example.com'
    open_url(url)
    mock_request_open.assert_called_once_with(
        'GET', url, data=None, headers=None, use_proxy=True, force=False,
        last_mod_time=None, timeout=10, validate_certs=True, url_username=None,
        url_password=None, http_agent=None, force_basic_auth=False,
        follow_redirects='urllib2', client_cert=None, client_key=None,
        cookies=None, use_gssapi=False, unix_socket=None, ca_path=None,
        unredirected_headers=None
    )

def test_open_url_post_request(mock_request_open):
    url = 'http://example.com'
    data = 'some data'
    open_url(url, data=data)
    mock_request_open.assert_called_once_with(
        'POST', url, data=data, headers=None, use_proxy=True, force=False,
        last_mod_time=None, timeout=10, validate_certs=True, url_username=None,
        url_password=None, http_agent=None, force_basic_auth=False,
        follow_redirects='urllib2', client_cert=None, client_key=None,
        cookies=None, use_gssapi=False, unix_socket=None, ca_path=None,
        unredirected_headers=None
    )

def test_open_url_custom_method(mock_request_open):
    url = 'http://example.com'
    method = 'PUT'
    open_url(url, method=method)
    mock_request_open.assert_called_once_with(
        method, url, data=None, headers=None, use_proxy=True, force=False,
        last_mod_time=None, timeout=10, validate_certs=True, url_username=None,
        url_password=None, http_agent=None, force_basic_auth=False,
        follow_redirects='urllib2', client_cert=None, client_key=None,
        cookies=None, use_gssapi=False, unix_socket=None, ca_path=None,
        unredirected_headers=None
    )

def test_open_url_with_headers(mock_request_open):
    url = 'http://example.com'
    headers = {'Content-Type': 'application/json'}
    open_url(url, headers=headers)
    mock_request_open.assert_called_once_with(
        'GET', url, data=None, headers=headers, use_proxy=True, force=False,
        last_mod_time=None, timeout=10, validate_certs=True, url_username=None,
        url_password=None, http_agent=None, force_basic_auth=False,
        follow_redirects='urllib2', client_cert=None, client_key=None,
        cookies=None, use_gssapi=False, unix_socket=None, ca_path=None,
        unredirected_headers=None
    )
