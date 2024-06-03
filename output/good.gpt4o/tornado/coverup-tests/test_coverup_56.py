# file tornado/simple_httpclient.py:226-231
# lines [226, 227, 228, 229, 230, 231]
# branches ['227->exit', '227->228', '229->230', '229->231']

import pytest
from tornado.ioloop import IOLoop
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from unittest.mock import Mock

@pytest.fixture
def mock_ioloop(mocker):
    return mocker.patch('tornado.ioloop.IOLoop.current', return_value=Mock(spec=IOLoop))

@pytest.fixture
def client(mock_ioloop):
    return SimpleAsyncHTTPClient()

def test_remove_timeout_with_key_in_waiting(client, mock_ioloop):
    key = object()
    request = Mock()
    callback = Mock()
    timeout_handle = Mock()
    
    client.waiting = {key: (request, callback, timeout_handle)}
    client._remove_timeout(key)
    
    mock_ioloop().remove_timeout.assert_called_once_with(timeout_handle)
    assert key not in client.waiting

def test_remove_timeout_with_key_not_in_waiting(client):
    key = object()
    client.waiting = {}
    
    client._remove_timeout(key)
    
    assert key not in client.waiting
