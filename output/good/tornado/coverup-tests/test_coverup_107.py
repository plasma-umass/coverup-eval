# file tornado/simple_httpclient.py:226-231
# lines [226, 227, 228, 229, 230, 231]
# branches ['227->exit', '227->228', '229->230', '229->231']

import pytest
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.ioloop import IOLoop
from unittest.mock import Mock, patch

@pytest.fixture
def mock_ioloop():
    loop = Mock(spec=IOLoop)
    return loop

@pytest.fixture
def http_client(mock_ioloop):
    with patch('tornado.ioloop.IOLoop.current', return_value=mock_ioloop):
        client = SimpleAsyncHTTPClient()
    return client

def test_remove_timeout(http_client, mock_ioloop):
    key = object()
    request = Mock()
    callback = Mock()
    timeout_handle = Mock()
    
    # Set up the waiting dictionary to include the key
    http_client.waiting[key] = (request, callback, timeout_handle)
    
    # Ensure the key is in the waiting dictionary
    assert key in http_client.waiting
    
    # Call the method under test
    http_client._remove_timeout(key)
    
    # Assert that the timeout was removed
    mock_ioloop.remove_timeout.assert_called_once_with(timeout_handle)
    
    # Assert that the key is no longer in the waiting dictionary
    assert key not in http_client.waiting

def test_remove_timeout_with_none_handle(http_client, mock_ioloop):
    key = object()
    request = Mock()
    callback = Mock()
    timeout_handle = None
    
    # Set up the waiting dictionary to include the key with a None timeout_handle
    http_client.waiting[key] = (request, callback, timeout_handle)
    
    # Ensure the key is in the waiting dictionary
    assert key in http_client.waiting
    
    # Call the method under test
    http_client._remove_timeout(key)
    
    # Assert that the remove_timeout was not called since the handle is None
    mock_ioloop.remove_timeout.assert_not_called()
    
    # Assert that the key is no longer in the waiting dictionary
    assert key not in http_client.waiting
