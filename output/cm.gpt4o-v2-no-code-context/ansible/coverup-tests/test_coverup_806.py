# file: lib/ansible/plugins/connection/paramiko_ssh.py:235-236
# asked: {"lines": [235, 236], "branches": []}
# gained: {"lines": [235, 236], "branches": []}

import pytest
from ansible.plugins.connection.paramiko_ssh import Connection
from ansible.playbook.play_context import PlayContext

@pytest.fixture
def play_context():
    context = PlayContext()
    context.remote_addr = '192.168.0.1'
    context.remote_user = 'test_user'
    return context

@pytest.fixture
def connection(play_context, monkeypatch):
    conn = Connection(play_context, new_stdin=None)
    monkeypatch.setattr(conn, '_play_context', play_context)
    return conn

def test_cache_key(connection):
    expected_key = "192.168.0.1__test_user__"
    assert connection._cache_key() == expected_key
