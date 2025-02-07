# file: lib/ansible/plugins/connection/paramiko_ssh.py:248-250
# asked: {"lines": [248, 250], "branches": []}
# gained: {"lines": [248, 250], "branches": []}

import pytest
from ansible.plugins.connection.paramiko_ssh import Connection
from ansible.plugins.connection import ConnectionBase
from ansible.errors import AnsibleError

class MockPlayContext:
    def __init__(self):
        self.shell = 'sh'
        self.executable = '/bin/sh'

@pytest.fixture
def connection():
    play_context = MockPlayContext()
    new_stdin = None
    return Connection(play_context, new_stdin)

def test_set_log_channel(connection):
    log_channel_name = "test_channel"
    connection._set_log_channel(log_channel_name)
    assert connection._log_channel == log_channel_name
