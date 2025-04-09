# file lib/ansible/plugins/connection/paramiko_ssh.py:510-538
# lines [510, 516, 517, 519, 520, 522, 524, 526, 529, 530, 531, 533, 535, 536, 537, 538]
# branches ['516->517', '516->519', '524->526', '524->533', '526->524', '526->529', '530->526', '530->531', '533->exit', '533->535', '535->533', '535->536', '537->535', '537->538']

import os
import pytest
from unittest import mock
from ansible.plugins.connection.paramiko_ssh import Connection
from ansible.playbook.play_context import PlayContext

@pytest.fixture
def mock_ssh_host_keys():
    class MockKey:
        def __init__(self, base64, added_by_ansible):
            self._base64 = base64
            self._added_by_ansible_this_time = added_by_ansible

        def get_base64(self):
            return self._base64

    return {
        'hostname1': {
            'ssh-rsa': MockKey('AAAAB3NzaC1yc2EAAAABIwAAAQEAr', False),
            'ssh-dss': MockKey('AAAAB3NzaC1kc3MAAACBAK', True)
        },
        'hostname2': {
            'ssh-rsa': MockKey('AAAAB3NzaC1yc2EAAAABIwAAAQEAr2', True)
        }
    }

@pytest.fixture
def connection(mock_ssh_host_keys):
    play_context = PlayContext()
    new_stdin = mock.Mock()
    conn = Connection(play_context, new_stdin)
    conn.ssh = mock.Mock()
    conn.ssh._host_keys = mock_ssh_host_keys
    return conn

@pytest.fixture
def temp_file(tmp_path):
    return tmp_path / "known_hosts"

def test_save_ssh_host_keys(connection, temp_file, mocker):
    mocker.patch('os.path.expanduser', return_value=str(temp_file.parent))
    mocker.patch('ansible.plugins.connection.paramiko_ssh.makedirs_safe')

    connection._any_keys_added = mock.Mock(return_value=True)

    result = connection._save_ssh_host_keys(str(temp_file))

    assert result is None  # The function does not return anything
    assert temp_file.exists()

    with open(temp_file, 'r') as f:
        lines = f.readlines()

    expected_lines = [
        "hostname1 ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAr\n",
        "hostname1 ssh-dss AAAAB3NzaC1kc3MAAACBAK\n",
        "hostname2 ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAr2\n"
    ]

    assert lines == expected_lines
