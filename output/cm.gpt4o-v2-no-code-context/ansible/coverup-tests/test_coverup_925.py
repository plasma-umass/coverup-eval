# file: lib/ansible/plugins/connection/paramiko_ssh.py:546-611
# asked: {"lines": [549, 550, 551, 553, 554, 555, 557, 563, 564, 565, 567, 568, 570, 573, 574, 579, 580, 581, 582, 583, 584, 586, 587, 588, 594, 595, 596, 598, 599, 601, 603, 607, 608, 610, 611], "branches": [[553, 554], [553, 557], [554, 555], [554, 557], [557, 563], [557, 610], [580, 581], [580, 586]]}
# gained: {"lines": [549, 550, 551, 553, 554, 555, 557, 563, 564, 565, 567, 568, 570, 573, 574, 579, 580, 581, 582, 583, 584, 594, 595, 596, 598, 603, 607, 608, 610, 611], "branches": [[553, 554], [554, 555], [554, 557], [557, 563], [557, 610], [580, 581]]}

import pytest
import os
import tempfile
import fcntl
import traceback
from unittest import mock
from ansible.plugins.connection.paramiko_ssh import Connection
from ansible.playbook.play_context import PlayContext

@pytest.fixture
def connection():
    play_context = PlayContext()
    new_stdin = mock.Mock()
    conn = Connection(play_context, new_stdin)
    conn.ssh = mock.Mock()
    conn.sftp = mock.Mock()
    conn.keyfile = tempfile.NamedTemporaryFile(delete=False).name
    conn._connected = True
    return conn

def test_close_connection_with_sftp(connection, monkeypatch):
    monkeypatch.setattr(connection, '_cache_key', lambda: 'test_key')
    monkeypatch.setattr(connection, 'get_option', lambda x: True)
    monkeypatch.setattr(connection, '_any_keys_added', lambda: True)
    monkeypatch.setattr('ansible.plugins.connection.paramiko_ssh.SSH_CONNECTION_CACHE', {})
    monkeypatch.setattr('ansible.plugins.connection.paramiko_ssh.SFTP_CONNECTION_CACHE', {})

    connection.close()

    assert not connection._connected
    connection.sftp.close.assert_called_once()
    connection.ssh.close.assert_called_once()

def test_close_connection_without_sftp(connection, monkeypatch):
    connection.sftp = None
    monkeypatch.setattr(connection, '_cache_key', lambda: 'test_key')
    monkeypatch.setattr(connection, 'get_option', lambda x: True)
    monkeypatch.setattr(connection, '_any_keys_added', lambda: True)
    monkeypatch.setattr('ansible.plugins.connection.paramiko_ssh.SSH_CONNECTION_CACHE', {})
    monkeypatch.setattr('ansible.plugins.connection.paramiko_ssh.SFTP_CONNECTION_CACHE', {})

    connection.close()

    assert not connection._connected
    connection.ssh.close.assert_called_once()

def test_close_connection_with_host_key_checking(connection, monkeypatch):
    monkeypatch.setattr(connection, '_cache_key', lambda: 'test_key')
    monkeypatch.setattr(connection, 'get_option', lambda x: True)
    monkeypatch.setattr(connection, '_any_keys_added', lambda: True)
    monkeypatch.setattr('ansible.plugins.connection.paramiko_ssh.SSH_CONNECTION_CACHE', {})
    monkeypatch.setattr('ansible.plugins.connection.paramiko_ssh.SFTP_CONNECTION_CACHE', {})

    connection.close()

    assert not connection._connected
    connection.ssh.close.assert_called_once()

def test_close_connection_without_host_key_checking(connection, monkeypatch):
    monkeypatch.setattr(connection, '_cache_key', lambda: 'test_key')
    monkeypatch.setattr(connection, 'get_option', lambda x: False)
    monkeypatch.setattr(connection, '_any_keys_added', lambda: False)
    monkeypatch.setattr('ansible.plugins.connection.paramiko_ssh.SSH_CONNECTION_CACHE', {})
    monkeypatch.setattr('ansible.plugins.connection.paramiko_ssh.SFTP_CONNECTION_CACHE', {})

    connection.close()

    assert not connection._connected
    connection.ssh.close.assert_called_once()

def test_close_connection_with_exception(connection, monkeypatch):
    def raise_exception(*args, **kwargs):
        raise Exception("Test Exception")

    monkeypatch.setattr(connection, '_cache_key', lambda: 'test_key')
    monkeypatch.setattr(connection, 'get_option', lambda x: True)
    monkeypatch.setattr(connection, '_any_keys_added', lambda: True)
    monkeypatch.setattr(connection.ssh, 'load_system_host_keys', raise_exception)
    monkeypatch.setattr('ansible.plugins.connection.paramiko_ssh.SSH_CONNECTION_CACHE', {})
    monkeypatch.setattr('ansible.plugins.connection.paramiko_ssh.SFTP_CONNECTION_CACHE', {})

    connection.close()

    assert not connection._connected
    connection.ssh.close.assert_called_once()
