# file lib/ansible/module_utils/urls.py:552-566
# lines [555, 556, 557, 558, 559, 560, 561, 563]
# branches ['556->557', '556->558']

import pytest
from ansible.module_utils.urls import CustomHTTPSHandler
from unittest.mock import patch, MagicMock, create_autospec
from urllib.request import HTTPSHandler

@pytest.fixture
def cleanup():
    # Fixture to perform cleanup after tests
    yield
    # No specific cleanup code needed for this test

@pytest.fixture
def mock_custom_https_connection():
    with patch('ansible.module_utils.urls.CustomHTTPSConnection') as mock_conn:
        yield mock_conn

def test_custom_https_handler_opens_connection(cleanup, mock_custom_https_connection):
    # Arrange
    handler = CustomHTTPSHandler()
    request = MagicMock()

    # Act
    with patch('ansible.module_utils.urls.HAS_SSLCONTEXT', True):
        with patch.object(handler, '_context', create_autospec(HTTPSHandler)):
            handler.https_open(request)

    # Assert
    assert mock_custom_https_connection.called, "CustomHTTPSConnection was not called"
    mock_custom_https_connection.assert_called()

def test_custom_https_handler_opens_connection_without_sslcontext(cleanup, mock_custom_https_connection):
    # Arrange
    handler = CustomHTTPSHandler()
    request = MagicMock()

    # Act
    with patch('ansible.module_utils.urls.HAS_SSLCONTEXT', False):
        handler.https_open(request)

    # Assert
    assert mock_custom_https_connection.called, "CustomHTTPSConnection was not called"
    mock_custom_https_connection.assert_called()
