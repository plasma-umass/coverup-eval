# file lib/ansible/plugins/connection/paramiko_ssh.py:501-508
# lines [503, 504, 505, 506, 507, 508]
# branches ['503->504', '503->508', '504->503', '504->505', '506->504', '506->507']

import pytest
from ansible.plugins.connection.paramiko_ssh import Connection
from ansible.plugins.loader import connection_loader
from unittest.mock import MagicMock, patch
from collections import defaultdict

@pytest.fixture
def paramiko_ssh_connection(mocker):
    mocker.patch('ansible.plugins.connection.paramiko_ssh.paramiko', return_value=MagicMock())
    connection = connection_loader.get('paramiko', None, None, '/dev/null')
    connection._play_context = MagicMock()
    connection._play_context.remote_addr = 'localhost'
    connection._connected = True
    connection.ssh = MagicMock()
    return connection

def test_any_keys_added(paramiko_ssh_connection):
    # Mock the _host_keys to simulate keys with the '_added_by_ansible_this_time' attribute
    fake_host_keys = defaultdict(dict)
    fake_host_key = MagicMock()
    setattr(fake_host_key, '_added_by_ansible_this_time', True)
    fake_host_keys['localhost']['ssh-rsa'] = fake_host_key
    paramiko_ssh_connection.ssh._host_keys = fake_host_keys

    # Assert that _any_keys_added returns True when a key has the '_added_by_ansible_this_time' attribute set to True
    assert paramiko_ssh_connection._any_keys_added() is True

    # Clean up by removing the attribute
    delattr(fake_host_key, '_added_by_ansible_this_time')
    fake_host_keys['localhost']['ssh-rsa'] = fake_host_key
    paramiko_ssh_connection.ssh._host_keys = fake_host_keys

    # Assert that _any_keys_added returns False when no key has the '_added_by_ansible_this_time' attribute
    assert paramiko_ssh_connection._any_keys_added() is False
