# file lib/ansible/plugins/connection/paramiko_ssh.py:510-538
# lines [510, 516, 517, 519, 520, 522, 524, 526, 529, 530, 531, 533, 535, 536, 537, 538]
# branches ['516->517', '516->519', '524->526', '524->533', '526->524', '526->529', '530->526', '530->531', '533->exit', '533->535', '535->533', '535->536', '537->535', '537->538']

import os
import pytest
from unittest.mock import MagicMock
from ansible.plugins.connection.paramiko_ssh import Connection
from ansible.module_utils.six import iteritems
from ansible.playbook.play_context import PlayContext

# Mocking iteritems to control the flow of the _save_ssh_host_keys method
def mock_iteritems(dictionary):
    for item in dictionary.items():
        yield item

@pytest.fixture
def paramiko_ssh_connection(mocker):
    play_context = PlayContext()
    play_context.shell = 'sh'
    new_stdin = MagicMock()
    connection = Connection(play_context, new_stdin)
    connection.ssh = MagicMock()
    connection.ssh._host_keys = {
        'example.com': {
            'ssh-rsa': MagicMock(get_base64=MagicMock(return_value='AAAAB3NzaC1yc2EAAAADAQABAAABAQD')),
            'ssh-dss': MagicMock(get_base64=MagicMock(return_value='AAAAB3NzaC1kc3MAAACBAQABAAABAQD'))
        }
    }
    connection.ssh._host_keys['example.com']['ssh-rsa']._added_by_ansible_this_time = False
    connection.ssh._host_keys['example.com']['ssh-dss']._added_by_ansible_this_time = True
    connection._any_keys_added = MagicMock(return_value=True)
    mocker.patch('ansible.plugins.connection.paramiko_ssh.makedirs_safe')
    mocker.patch('ansible.plugins.connection.paramiko_ssh.os.path.expanduser', return_value='/fake/home/.ssh')
    mocker.patch('ansible.plugins.connection.paramiko_ssh.iteritems', side_effect=mock_iteritems)
    return connection

def test_save_ssh_host_keys(paramiko_ssh_connection, tmp_path):
    host_keys_file = tmp_path / 'ssh_host_keys'
    paramiko_ssh_connection._save_ssh_host_keys(str(host_keys_file))

    # Read the file and check if the keys are correctly written
    with host_keys_file.open() as f:
        lines = f.readlines()

    assert 'example.com ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD\n' in lines
    assert 'example.com ssh-dss AAAAB3NzaC1kc3MAAACBAQABAAABAQD\n' in lines

    # Check that the key added by ansible is at the bottom
    assert lines[-1] == 'example.com ssh-dss AAAAB3NzaC1kc3MAAACBAQABAAABAQD\n'
