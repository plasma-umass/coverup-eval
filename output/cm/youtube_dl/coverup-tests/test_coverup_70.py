# file youtube_dl/socks.py:269-270
# lines [270]
# branches []

import pytest
import socket
from youtube_dl.socks import sockssocket

# Mocking the original socket.socket.connect method
def mock_connect(self, address):
    raise Exception("Test Exception to trigger line 270")

# Test function to cover line 270
def test_sockssocket_connect(mocker):
    # Mocking the socket.socket.connect to raise an exception
    mocker.patch('socket.socket.connect', new=mock_connect)
    
    # Creating a sockssocket instance
    s = sockssocket()
    
    # Asserting that the Exception is raised when connect is called
    with pytest.raises(Exception) as excinfo:
        s.connect(('example.com', 80))
    assert str(excinfo.value) == "Test Exception to trigger line 270"
