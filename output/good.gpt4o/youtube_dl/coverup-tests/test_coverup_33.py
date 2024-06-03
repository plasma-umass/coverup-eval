# file youtube_dl/socks.py:272-273
# lines [273]
# branches []

import pytest
import socket
from unittest import mock

# Assuming the sockssocket class is imported from youtube_dl.socks
from youtube_dl.socks import sockssocket

@pytest.fixture
def mock_socket_connect_ex(mocker):
    mock_connect_ex = mocker.patch('socket.socket.connect_ex', return_value=0)
    return mock_connect_ex

def test_sockssocket_connect_ex(mock_socket_connect_ex):
    with mock.patch.object(sockssocket, '_make_proxy', return_value=0) as mock_make_proxy:
        s = sockssocket()
        address = ('localhost', 8080)
        result = s.connect_ex(address)
        
        mock_make_proxy.assert_called_once_with(socket.socket.connect_ex, address)
        assert result == 0
