# file lib/ansible/plugins/connection/paramiko_ssh.py:248-250
# lines [248, 250]
# branches []

import pytest
from ansible.plugins.connection.paramiko_ssh import Connection
from ansible.playbook.play_context import PlayContext

@pytest.fixture
def connection(mocker):
    play_context = PlayContext()
    new_stdin = mocker.Mock()
    return Connection(play_context, new_stdin)

def test_set_log_channel(connection):
    log_channel_name = "test_channel"
    connection._set_log_channel(log_channel_name)
    assert connection._log_channel == log_channel_name
