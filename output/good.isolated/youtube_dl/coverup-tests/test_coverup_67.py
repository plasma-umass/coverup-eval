# file youtube_dl/socks.py:121-128
# lines [122, 123, 124, 125, 126, 127, 128]
# branches ['123->124', '123->128', '125->126', '125->127']

import pytest
import socket
from youtube_dl.socks import sockssocket

@pytest.fixture
def mock_socket(mocker):
    mock = mocker.MagicMock(spec=socket.socket)
    mock.recv = mocker.MagicMock(side_effect=[b'', EOFError])
    return mock

def test_sockssocket_recvall_eoferror(mock_socket):
    s = sockssocket()
    s.recv = mock_socket.recv

    with pytest.raises(EOFError) as excinfo:
        s.recvall(10)
    assert '10 bytes missing' in str(excinfo.value)
