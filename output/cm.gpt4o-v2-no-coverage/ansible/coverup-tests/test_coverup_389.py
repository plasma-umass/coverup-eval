# file: lib/ansible/plugins/connection/paramiko_ssh.py:501-508
# asked: {"lines": [501, 503, 504, 505, 506, 507, 508], "branches": [[503, 504], [503, 508], [504, 503], [504, 505], [506, 504], [506, 507]]}
# gained: {"lines": [501, 503, 504, 505, 506, 507, 508], "branches": [[503, 504], [503, 508], [504, 503], [504, 505], [506, 504], [506, 507]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.connection.paramiko_ssh import Connection
from ansible.module_utils.six import iteritems

@pytest.fixture
def connection():
    with patch('ansible.plugins.connection.get_shell_plugin', return_value=MagicMock()):
        conn = Connection(MagicMock(), MagicMock())
        conn.ssh = MagicMock()
        return conn

def test_any_keys_added_true(connection):
    # Mock the ssh._host_keys to simulate keys added by ansible
    connection.ssh._host_keys = {
        'hostname1': {
            'keytype1': MagicMock(_added_by_ansible_this_time=True)
        }
    }
    
    assert connection._any_keys_added() is True

def test_any_keys_added_false(connection):
    # Mock the ssh._host_keys to simulate no keys added by ansible
    connection.ssh._host_keys = {
        'hostname1': {
            'keytype1': MagicMock(_added_by_ansible_this_time=False)
        }
    }
    
    assert connection._any_keys_added() is False

def test_any_keys_added_empty(connection):
    # Mock the ssh._host_keys to be empty
    connection.ssh._host_keys = {}
    
    assert connection._any_keys_added() is False
