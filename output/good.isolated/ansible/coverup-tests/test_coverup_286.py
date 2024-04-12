# file lib/ansible/module_utils/urls.py:1522-1541
# lines [1522, 1523, 1524, 1525, 1526, 1527, 1528, 1534, 1535, 1536, 1537, 1538, 1539, 1540, 1541]
# branches []

import pytest
from ansible.module_utils.urls import open_url
from unittest.mock import patch, MagicMock

class MockRequest:
    def open(self, method, url, **kwargs):
        return url, method, kwargs

@pytest.fixture
def mock_request(mocker):
    mocker.patch('ansible.module_utils.urls.Request', return_value=MockRequest())

def test_open_url_with_all_parameters(mock_request):
    test_url = 'http://example.com'
    test_data = {'key': 'value'}
    test_headers = {'User-Agent': 'test-agent'}
    test_method = 'PUT'
    test_use_proxy = False
    test_force = True
    test_last_mod_time = 'Wed, 21 Oct 2015 07:28:00 GMT'
    test_timeout = 20
    test_validate_certs = False
    test_url_username = 'user'
    test_url_password = 'pass'
    test_http_agent = 'test-agent'
    test_force_basic_auth = True
    test_follow_redirects = 'yes'
    test_client_cert = '/path/to/cert'
    test_client_key = '/path/to/key'
    test_cookies = {'session': '123456'}
    test_use_gssapi = True
    test_unix_socket = '/path/to/socket'
    test_ca_path = '/path/to/ca'
    test_unredirected_headers = {'Host': 'example.com'}

    url, method, kwargs = open_url(
        url=test_url,
        data=test_data,
        headers=test_headers,
        method=test_method,
        use_proxy=test_use_proxy,
        force=test_force,
        last_mod_time=test_last_mod_time,
        timeout=test_timeout,
        validate_certs=test_validate_certs,
        url_username=test_url_username,
        url_password=test_url_password,
        http_agent=test_http_agent,
        force_basic_auth=test_force_basic_auth,
        follow_redirects=test_follow_redirects,
        client_cert=test_client_cert,
        client_key=test_client_key,
        cookies=test_cookies,
        use_gssapi=test_use_gssapi,
        unix_socket=test_unix_socket,
        ca_path=test_ca_path,
        unredirected_headers=test_unredirected_headers
    )

    assert url == test_url
    assert method == test_method
    assert kwargs['data'] == test_data
    assert kwargs['headers'] == test_headers
    assert kwargs['use_proxy'] == test_use_proxy
    assert kwargs['force'] == test_force
    assert kwargs['last_mod_time'] == test_last_mod_time
    assert kwargs['timeout'] == test_timeout
    assert kwargs['validate_certs'] == test_validate_certs
    assert kwargs['url_username'] == test_url_username
    assert kwargs['url_password'] == test_url_password
    assert kwargs['http_agent'] == test_http_agent
    assert kwargs['force_basic_auth'] == test_force_basic_auth
    assert kwargs['follow_redirects'] == test_follow_redirects
    assert kwargs['client_cert'] == test_client_cert
    assert kwargs['client_key'] == test_client_key
    assert kwargs['cookies'] == test_cookies
    assert kwargs['use_gssapi'] == test_use_gssapi
    assert kwargs['unix_socket'] == test_unix_socket
    assert kwargs['ca_path'] == test_ca_path
    assert kwargs['unredirected_headers'] == test_unredirected_headers
