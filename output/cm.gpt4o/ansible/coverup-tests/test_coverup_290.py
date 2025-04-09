# file lib/ansible/module_utils/urls.py:1522-1541
# lines [1522, 1523, 1524, 1525, 1526, 1527, 1528, 1534, 1535, 1536, 1537, 1538, 1539, 1540, 1541]
# branches []

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.urls import open_url

@pytest.fixture
def mock_request():
    with patch('ansible.module_utils.urls.Request') as mock_request:
        yield mock_request

def test_open_url_get(mock_request):
    mock_request_instance = mock_request.return_value
    mock_request_instance.open.return_value = 'response'

    url = 'http://example.com'
    response = open_url(url)

    mock_request_instance.open.assert_called_once_with(
        'GET', url, data=None, headers=None, use_proxy=True,
        force=False, last_mod_time=None, timeout=10, validate_certs=True,
        url_username=None, url_password=None, http_agent=None,
        force_basic_auth=False, follow_redirects='urllib2',
        client_cert=None, client_key=None, cookies=None,
        use_gssapi=False, unix_socket=None, ca_path=None,
        unredirected_headers=None
    )
    assert response == 'response'

def test_open_url_post(mock_request):
    mock_request_instance = mock_request.return_value
    mock_request_instance.open.return_value = 'response'

    url = 'http://example.com'
    data = 'some data'
    response = open_url(url, data=data)

    mock_request_instance.open.assert_called_once_with(
        'POST', url, data=data, headers=None, use_proxy=True,
        force=False, last_mod_time=None, timeout=10, validate_certs=True,
        url_username=None, url_password=None, http_agent=None,
        force_basic_auth=False, follow_redirects='urllib2',
        client_cert=None, client_key=None, cookies=None,
        use_gssapi=False, unix_socket=None, ca_path=None,
        unredirected_headers=None
    )
    assert response == 'response'

def test_open_url_with_headers(mock_request):
    mock_request_instance = mock_request.return_value
    mock_request_instance.open.return_value = 'response'

    url = 'http://example.com'
    headers = {'Content-Type': 'application/json'}
    response = open_url(url, headers=headers)

    mock_request_instance.open.assert_called_once_with(
        'GET', url, data=None, headers=headers, use_proxy=True,
        force=False, last_mod_time=None, timeout=10, validate_certs=True,
        url_username=None, url_password=None, http_agent=None,
        force_basic_auth=False, follow_redirects='urllib2',
        client_cert=None, client_key=None, cookies=None,
        use_gssapi=False, unix_socket=None, ca_path=None,
        unredirected_headers=None
    )
    assert response == 'response'

def test_open_url_with_auth(mock_request):
    mock_request_instance = mock_request.return_value
    mock_request_instance.open.return_value = 'response'

    url = 'http://example.com'
    url_username = 'user'
    url_password = 'pass'
    response = open_url(url, url_username=url_username, url_password=url_password)

    mock_request_instance.open.assert_called_once_with(
        'GET', url, data=None, headers=None, use_proxy=True,
        force=False, last_mod_time=None, timeout=10, validate_certs=True,
        url_username=url_username, url_password=url_password, http_agent=None,
        force_basic_auth=False, follow_redirects='urllib2',
        client_cert=None, client_key=None, cookies=None,
        use_gssapi=False, unix_socket=None, ca_path=None,
        unredirected_headers=None
    )
    assert response == 'response'
