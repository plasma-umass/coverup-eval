# file: lib/ansible/vars/clean.py:118-164
# asked: {"lines": [120, 122, 123, 127, 128, 131, 134, 135, 136, 137, 139, 140, 143, 144, 145, 148, 149, 150, 151, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 164], "branches": [[127, 128], [127, 131], [134, 135], [134, 143], [137, 134], [137, 139], [139, 137], [139, 140], [143, 144], [143, 148], [144, 143], [144, 145], [149, 150], [149, 153], [150, 149], [150, 151], [153, 154], [153, 164], [154, 153], [154, 155], [157, 158], [157, 161]]}
# gained: {"lines": [120, 122, 123, 127, 128, 131, 134, 135, 136, 137, 139, 140, 143, 144, 145, 148, 149, 150, 151, 153, 154, 155, 156, 157, 158, 161, 162, 164], "branches": [[127, 128], [127, 131], [134, 135], [134, 143], [137, 134], [137, 139], [139, 137], [139, 140], [143, 144], [143, 148], [144, 145], [149, 150], [149, 153], [150, 149], [150, 151], [153, 154], [153, 164], [154, 155], [157, 158], [157, 161]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.vars.clean import clean_facts
from ansible import constants as C

@pytest.fixture
def mock_connection_loader():
    with patch('ansible.plugins.loader.connection_loader.all') as mock_all:
        mock_all.return_value = ['/path/to/connection/plugin']
        yield mock_all

@pytest.fixture
def mock_display_warning():
    with patch('ansible.utils.display.Display.warning') as mock_warning:
        yield mock_warning

def test_clean_facts_removes_magic_vars(mock_connection_loader, mock_display_warning):
    facts = {
        'ansible_connection': 'ssh',
        'ansible_shell_type': 'bash',
        'ansible_ssh_host': 'localhost',
        'ansible_user': 'root',
        'ansible_password': 'password',
        'ansible_port': 22,
        'ansible_become': True,
        'ansible_become_user': 'admin',
        'ansible_become_password': 'admin_pass',
        'ansible_become_method': 'sudo',
        'ansible_become_exe': 'sudo',
        'ansible_become_flags': '-H',
        'ansible_ssh_private_key_file': '/path/to/key',
        'ansible_network_os': 'ios',
        'ansible_ssh_common_args': '-o StrictHostKeyChecking=no',
        'ansible_sftp_extra_args': '-o SftpExtraArgs',
        'ansible_scp_extra_args': '-o ScpExtraArgs',
        'ansible_ssh_extra_args': '-o SshExtraArgs',
        'ansible_ssh_transfer_method': 'sftp',
        'ansible_docker_extra_args': '--privileged',
        'ansible_ssh_timeout': 30,
        'ansible_shell_executable': '/bin/bash',
        'ansible_module_compression': 'ZIP_DEFLATED',
        'ansible_pipelining': True,
        'ansible_host': 'localhost',
        'ansible_rsync_path': '/usr/bin/rsync',
        'ansible_playbook_python': '/usr/bin/python3',
        'ansible_facts': {},
        'add_host': 'new_host',
        'add_group': 'new_group',
        'ansible_python_interpreter': '/usr/bin/python3',
        'ansible_ssh_host_key_rsa': 'AAAAB3NzaC1yc2EAAAABIwAAAQEAr...'
    }

    cleaned_facts = clean_facts(facts)

    # Assertions to verify that restricted keys are removed
    assert 'ansible_connection' not in cleaned_facts
    assert 'ansible_shell_type' not in cleaned_facts
    assert 'ansible_ssh_host' not in cleaned_facts
    assert 'ansible_user' not in cleaned_facts
    assert 'ansible_password' not in cleaned_facts
    assert 'ansible_port' not in cleaned_facts
    assert 'ansible_become' not in cleaned_facts
    assert 'ansible_become_user' not in cleaned_facts
    assert 'ansible_become_password' not in cleaned_facts
    assert 'ansible_become_method' not in cleaned_facts
    assert 'ansible_become_exe' not in cleaned_facts
    assert 'ansible_become_flags' not in cleaned_facts
    assert 'ansible_ssh_private_key_file' not in cleaned_facts
    assert 'ansible_network_os' not in cleaned_facts
    assert 'ansible_ssh_common_args' not in cleaned_facts
    assert 'ansible_sftp_extra_args' not in cleaned_facts
    assert 'ansible_scp_extra_args' not in cleaned_facts
    assert 'ansible_ssh_extra_args' not in cleaned_facts
    assert 'ansible_ssh_transfer_method' not in cleaned_facts
    assert 'ansible_docker_extra_args' not in cleaned_facts
    assert 'ansible_ssh_timeout' not in cleaned_facts
    assert 'ansible_shell_executable' not in cleaned_facts
    assert 'ansible_module_compression' not in cleaned_facts
    assert 'ansible_pipelining' not in cleaned_facts
    assert 'ansible_host' not in cleaned_facts
    assert 'ansible_rsync_path' not in cleaned_facts
    assert 'ansible_playbook_python' not in cleaned_facts
    assert 'ansible_facts' not in cleaned_facts
    assert 'add_host' not in cleaned_facts
    assert 'add_group' not in cleaned_facts
    assert 'ansible_python_interpreter' not in cleaned_facts

    # Assertions to verify that ssh host keys are not removed
    assert 'ansible_ssh_host_key_rsa' in cleaned_facts

    # Verify that display.warning was called for each removed key
    assert mock_display_warning.call_count == len(facts) - 1  # minus 1 for the ssh host key
