# file lib/ansible/plugins/connection/paramiko_ssh.py:510-538
# lines [516, 517, 519, 520, 522, 524, 526, 529, 530, 531, 533, 535, 536, 537, 538]
# branches ['516->517', '516->519', '524->526', '524->533', '526->524', '526->529', '530->526', '530->531', '533->exit', '533->535', '535->533', '535->536', '537->535', '537->538']

import os
import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.connection.paramiko_ssh import Connection
from ansible.playbook.play_context import PlayContext

@pytest.fixture
def paramiko_ssh_connection(mocker):
    play_context = PlayContext()
    new_stdin = mocker.MagicMock()
    connection = Connection(play_context, new_stdin)
    connection._any_keys_added = MagicMock(return_value=True)
    connection.ssh = MagicMock()
    connection.ssh._host_keys = {
        'example.com': {
            'ssh-rsa': MagicMock(get_base64=MagicMock(return_value='AAAAB3NzaC1yc2EAAAADAQABAAABAQD')),
            'ssh-dss': MagicMock(get_base64=MagicMock(return_value='AAAAB3NzaC1kc3MAAACBAQD'))
        }
    }
    connection.ssh._host_keys['example.com']['ssh-rsa']._added_by_ansible_this_time = False
    connection.ssh._host_keys['example.com']['ssh-dss']._added_by_ansible_this_time = True
    return connection

def test_save_ssh_host_keys(paramiko_ssh_connection, tmp_path, mocker):
    host_keys_file = tmp_path / "ssh_host_keys"
    paramiko_ssh_connection._save_ssh_host_keys(str(host_keys_file))

    # Verify that the file has been written to
    assert host_keys_file.exists()

    # Read the contents of the file
    with host_keys_file.open() as f:
        contents = f.readlines()

    # Verify the contents of the file
    assert 'example.com ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD\n' in contents
    assert 'example.com ssh-dss AAAAB3NzaC1kc3MAAACBAQD\n' in contents

    # Verify that the ssh-dss key was added this time and ssh-rsa was not
    assert contents.count('example.com ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD\n') == 1
    assert contents.count('example.com ssh-dss AAAAB3NzaC1kc3MAAACBAQD\n') == 1

    # Cleanup
    host_keys_file.unlink()
