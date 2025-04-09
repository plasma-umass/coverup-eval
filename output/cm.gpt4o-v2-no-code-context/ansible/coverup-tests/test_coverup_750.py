# file: lib/ansible/plugins/connection/paramiko_ssh.py:248-250
# asked: {"lines": [248, 250], "branches": []}
# gained: {"lines": [248, 250], "branches": []}

import pytest
from ansible.plugins.connection.paramiko_ssh import Connection

class MockConnectionBase:
    def __init__(self):
        self._log_channel = None

@pytest.fixture
def connection():
    class TestConnection(MockConnectionBase, Connection):
        pass
    return TestConnection()

def test_set_log_channel(connection):
    connection._set_log_channel('test_channel')
    assert connection._log_channel == 'test_channel'
