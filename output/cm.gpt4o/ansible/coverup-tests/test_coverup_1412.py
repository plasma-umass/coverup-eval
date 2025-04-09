# file lib/ansible/module_utils/urls.py:552-566
# lines [555, 556, 557, 558, 559, 560, 561, 563]
# branches ['556->557', '556->558']

import pytest
import urllib.request as urllib_request
import functools
from ansible.module_utils.urls import HAS_SSLCONTEXT, CustomHTTPSHandler, CustomHTTPSConnection

@pytest.fixture
def mock_https_connection(mocker):
    return mocker.patch('ansible.module_utils.urls.CustomHTTPSConnection')

def test_custom_https_handler_https_open(mock_https_connection, mocker):
    mocker.patch('ansible.module_utils.urls.HAS_SSLCONTEXT', True)
    mock_context = mocker.Mock()
    handler = CustomHTTPSHandler()
    handler._context = mock_context

    req = urllib_request.Request('https://example.com')
    req.timeout = 10  # Set a timeout attribute to avoid the AttributeError
    handler.https_open(req)

    mock_https_connection.assert_called_once_with('example.com', timeout=10, context=mock_context)
    assert mock_https_connection.call_args[1]['context'] == mock_context
