# file lib/ansible/plugins/connection/paramiko_ssh.py:248-250
# lines [250]
# branches []

# test_paramiko_ssh.py

import pytest
from ansible.plugins.connection.paramiko_ssh import Connection

@pytest.fixture
def paramiko_connection(mocker):
    mocker.patch('ansible.plugins.connection.paramiko_ssh.Connection.__init__', return_value=None)
    conn = Connection()
    conn._log_channel = None
    return conn

def test_set_log_channel(paramiko_connection):
    # Test to cover line 250 in paramiko_ssh.py
    log_channel_name = "test_log_channel"
    paramiko_connection._set_log_channel(log_channel_name)
    assert paramiko_connection._log_channel == log_channel_name
