# file lib/ansible/plugins/connection/paramiko_ssh.py:248-250
# lines [248, 250]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.plugins.connection.paramiko_ssh import Connection
from ansible.playbook.play_context import PlayContext

@pytest.fixture
def paramiko_connection():
    play_context = PlayContext()
    play_context.shell = 'sh'
    new_stdin = MagicMock()
    return Connection(play_context, new_stdin)

def test_set_log_channel(paramiko_connection):
    # Test setting the log channel
    log_channel_name = "test_log_channel"
    paramiko_connection._set_log_channel(log_channel_name)
    
    # Assert that the log channel is set correctly
    assert paramiko_connection._log_channel == log_channel_name, "Log channel name was not set correctly"
