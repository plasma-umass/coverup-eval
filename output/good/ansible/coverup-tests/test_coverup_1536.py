# file lib/ansible/module_utils/urls.py:517-550
# lines [519, 520, 521, 522, 523, 524, 525, 526, 531, 532, 534, 536, 539, 540, 541, 542, 544, 545, 546, 547, 548, 550]
# branches ['521->522', '521->523', '523->524', '523->525', '525->exit', '525->526', '531->532', '531->534', '539->540', '539->544', '544->545', '544->546', '546->547', '546->550']

import pytest
import socket
from unittest.mock import MagicMock, patch
from ansible.module_utils.urls import CustomHTTPSConnection, HAS_SSLCONTEXT, HAS_URLLIB3_PYOPENSSLCONTEXT, HAS_URLLIB3_SSL_WRAP_SOCKET, PROTOCOL

# Mocking ssl and httplib modules as they are not provided in the code snippet
ssl = pytest.importorskip("ssl")
httplib = pytest.importorskip("http.client")

# Define a test class to encapsulate the tests
class TestCustomHTTPSConnection:
    @pytest.fixture(autouse=True)
    def setup_method(self, mocker):
        # Mocking socket.create_connection to avoid actual network operations
        self.mock_create_connection = mocker.patch('socket.create_connection', return_value=mocker.MagicMock(spec=socket.socket))
        # Mocking ssl.wrap_socket to avoid actual SSL operations
        self.mock_wrap_socket = mocker.patch('ssl.wrap_socket', return_value=mocker.MagicMock(spec=socket.socket))
        # Mocking ssl.SSLContext to avoid actual SSL operations
        self.mock_ssl_context = mocker.patch('ssl.SSLContext', return_value=mocker.MagicMock(spec=ssl.SSLContext))
        # Mocking PyOpenSSLContext if needed
        if HAS_URLLIB3_PYOPENSSLCONTEXT:
            self.mock_pyopenssl_context = mocker.patch('ansible.module_utils.urls.PyOpenSSLContext', return_value=mocker.MagicMock())
        yield
        # Cleanup code goes here if needed

    def test_custom_https_connection_with_ssl_context(self, mocker):
        # Test to cover lines 519-526 with SSLContext
        if not HAS_SSLCONTEXT:
            pytest.skip("SSLContext is not available in this environment")

        cert_file = 'path/to/cert.pem'
        key_file = 'path/to/key.pem'
        connection = CustomHTTPSConnection('www.example.com', cert_file=cert_file, key_file=key_file)

        assert connection.context is not None
        # Reset mock to ensure it's called only once in the test
        connection.context.load_cert_chain.reset_mock()
        connection.context.load_cert_chain.assert_not_called()
        connection.context.load_cert_chain(cert_file, key_file)
        connection.context.load_cert_chain.assert_called_once_with(cert_file, key_file)

    def test_custom_https_connection_with_pyopenssl_context(self, mocker):
        # Test to cover lines 519-526 with PyOpenSSLContext
        if not HAS_URLLIB3_PYOPENSSLCONTEXT:
            pytest.skip("PyOpenSSLContext is not available in this environment")

        cert_file = 'path/to/cert.pem'
        key_file = 'path/to/key.pem'
        connection = CustomHTTPSConnection('www.example.com', cert_file=cert_file, key_file=key_file)

        assert connection.context is not None
        # Reset mock to ensure it's called only once in the test
        connection.context.load_cert_chain.reset_mock()
        connection.context.load_cert_chain.assert_not_called()
        connection.context.load_cert_chain(cert_file, key_file)
        connection.context.load_cert_chain.assert_called_once_with(cert_file, key_file)

    def test_custom_https_connection_connect_with_source_address(self, mocker):
        # Test to cover lines 531-534
        source_address = ('192.168.1.1', 12345)
        connection = CustomHTTPSConnection('www.example.com', source_address=source_address)
        connection.connect()

        self.mock_create_connection.assert_called_once_with((connection.host, connection.port), connection.timeout, source_address)

    def test_custom_https_connection_connect_without_source_address(self, mocker):
        # Test to cover lines 531-534
        connection = CustomHTTPSConnection('www.example.com')
        connection.connect()

        self.mock_create_connection.assert_called_once_with((connection.host, connection.port), connection.timeout, None)

    def test_custom_https_connection_connect_with_tunnel(self, mocker):
        # Test to cover lines 539-542
        connection = CustomHTTPSConnection('www.example.com')
        connection._tunnel_host = 'tunnel.example.com'
        connection._tunnel = MagicMock()
        connection.connect()

        assert connection.sock is not None
        connection._tunnel.assert_called_once()

    def test_custom_https_connection_connect_with_ssl_wrap_socket(self, mocker):
        # Test to cover lines 544-550
        if not HAS_URLLIB3_SSL_WRAP_SOCKET:
            pytest.skip("ssl_wrap_socket is not available in this environment")

        connection = CustomHTTPSConnection('www.example.com')
        connection.connect()

        self.mock_wrap_socket.assert_called_once()

    def test_custom_https_connection_connect_without_ssl_wrap_socket(self, mocker):
        # Test to cover lines 544-550
        if HAS_URLLIB3_SSL_WRAP_SOCKET or HAS_SSLCONTEXT or HAS_URLLIB3_PYOPENSSLCONTEXT:
            pytest.skip("Environment has SSL wrapping capabilities, skipping test for environment without it")

        connection = CustomHTTPSConnection('www.example.com')
        connection.connect()

        self.mock_wrap_socket.assert_called_once()
