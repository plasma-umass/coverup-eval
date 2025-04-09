# file lib/ansible/module_utils/connection.py:120-121
# lines [120]
# branches []

import pytest
from ansible.module_utils.connection import Connection

class MockConnection(Connection):
    def __init__(self, socket_path, *args, **kwargs):
        super().__init__(socket_path, *args, **kwargs)
        self.connected = False

    def connect(self):
        self.connected = True

    def disconnect(self):
        self.connected = False

@pytest.fixture
def mock_connection():
    conn = MockConnection(socket_path='/tmp/mock_socket')
    yield conn
    conn.disconnect()

def test_connection(mock_connection):
    assert not mock_connection.connected
    mock_connection.connect()
    assert mock_connection.connected
    mock_connection.disconnect()
    assert not mock_connection.connected
