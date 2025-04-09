# file lib/ansible/module_utils/urls.py:1052-1115
# lines [1052, 1053, 1056, 1057, 1059, 1060, 1061, 1062, 1064, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1094, 1095, 1097, 1099, 1100, 1101, 1102, 1103, 1105, 1106, 1109, 1110, 1111, 1112, 1113, 1115]
# branches ['1067->1068', '1067->1099', '1071->1072', '1071->1075', '1076->1077', '1076->1097', '1078->1079', '1078->1081', '1083->1084', '1083->1088', '1086->1083', '1086->1087', '1089->1090', '1089->1091', '1091->1092', '1091->1094', '1100->1101', '1100->1102', '1102->1103', '1102->1105']

import os
import pytest
import socket
import ssl
from unittest.mock import MagicMock, patch
from ansible.module_utils.urls import SSLValidationHandler, ProxyError, ConnectionError

# Constants used in the SSLValidationHandler
PROTOCOL = ssl.PROTOCOL_TLSv1
HAS_URLLIB3_SSL_WRAP_SOCKET = False

@pytest.fixture
def ssl_validation_handler():
    handler = SSLValidationHandler(hostname='example.com', port=443)
    handler.CONNECT_COMMAND = 'CONNECT %s:%s HTTP/1.0\r\n'
    return handler

@pytest.fixture
def cleanup_env():
    # Backup original environment variables
    original_https_proxy = os.environ.get('https_proxy')
    yield
    # Restore original environment variables
    if original_https_proxy is not None:
        os.environ['https_proxy'] = original_https_proxy
    else:
        os.environ.pop('https_proxy', None)

def test_ssl_validation_handler_proxy_error_scheme(ssl_validation_handler, cleanup_env):
    with patch('ansible.module_utils.urls.generic_urlparse') as mock_urlparse:
        with patch('ansible.module_utils.urls.socket.create_connection') as mock_create_connection:
            # Set up the environment and mocks
            os.environ['https_proxy'] = 'invalid://proxy.example.com:3128'
            mock_urlparse.return_value = {'scheme': 'invalid', 'hostname': 'proxy.example.com', 'port': 3128}
            req = MagicMock()
            req.get_full_url.return_value = 'https://example.com'

            # Run the test
            with pytest.raises(ProxyError) as excinfo:
                ssl_validation_handler.http_request(req)

            # Check the exception message
            assert 'Unsupported proxy scheme' in str(excinfo.value)

def test_ssl_validation_handler_proxy_error_parsing(ssl_validation_handler, cleanup_env):
    with patch('ansible.module_utils.urls.generic_urlparse') as mock_urlparse:
        with patch('ansible.module_utils.urls.socket.create_connection') as mock_create_connection:
            # Set up the environment and mocks
            os.environ['https_proxy'] = '://proxy.example.com:3128'
            mock_urlparse.return_value = {'scheme': '', 'hostname': None, 'port': 3128}
            req = MagicMock()
            req.get_full_url.return_value = 'https://example.com'

            # Run the test
            with pytest.raises(ProxyError) as excinfo:
                ssl_validation_handler.http_request(req)

            # Check the exception message
            assert 'Failed to parse https_proxy environment variable' in str(excinfo.value)

def test_ssl_validation_handler_socket_error(ssl_validation_handler, cleanup_env):
    with patch('ansible.module_utils.urls.socket.create_connection') as mock_create_connection:
        # Set up the environment and mocks
        os.environ.pop('https_proxy', None)
        mock_create_connection.side_effect = socket.error('Test socket error')
        req = MagicMock()
        req.get_full_url.return_value = 'https://example.com'

        # Run the test
        with pytest.raises(ConnectionError) as excinfo:
            ssl_validation_handler.http_request(req)

        # Check the exception message
        assert 'Failed to connect to example.com at port 443' in str(excinfo.value)
