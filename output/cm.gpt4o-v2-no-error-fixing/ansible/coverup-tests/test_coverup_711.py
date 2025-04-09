# file: lib/ansible/vars/clean.py:118-164
# asked: {"lines": [120, 122, 123, 127, 128, 131, 134, 135, 136, 137, 139, 140, 143, 144, 145, 148, 149, 150, 151, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 164], "branches": [[127, 128], [127, 131], [134, 135], [134, 143], [137, 134], [137, 139], [139, 137], [139, 140], [143, 144], [143, 148], [144, 143], [144, 145], [149, 150], [149, 153], [150, 149], [150, 151], [153, 154], [153, 164], [154, 153], [154, 155], [157, 158], [157, 161]]}
# gained: {"lines": [120, 122, 123, 127, 128, 131, 134, 135, 136, 137, 139, 140, 143, 144, 145, 148, 149, 150, 151, 153, 154, 155, 156, 157, 161, 162, 164], "branches": [[127, 128], [127, 131], [134, 135], [134, 143], [137, 134], [137, 139], [139, 137], [139, 140], [143, 144], [143, 148], [144, 145], [149, 150], [149, 153], [150, 149], [150, 151], [153, 154], [153, 164], [154, 153], [154, 155], [157, 161]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.vars.clean import clean_facts
from ansible import constants as C
from ansible.module_utils._text import to_text
from ansible.plugins.loader import connection_loader

@pytest.fixture
def mock_constants():
    with patch('ansible.constants.MAGIC_VARIABLE_MAPPING', {
        'connection': ('ansible_connection',),
        'module_compression': ('ansible_module_compression',),
        'shell': ('ansible_shell_type',),
        'executable': ('ansible_shell_executable',),
        'remote_addr': ('ansible_ssh_host', 'ansible_host'),
        'remote_user': ('ansible_ssh_user', 'ansible_user'),
        'password': ('ansible_ssh_pass', 'ansible_password'),
        'port': ('ansible_ssh_port', 'ansible_port'),
        'pipelining': ('ansible_ssh_pipelining', 'ansible_pipelining'),
        'timeout': ('ansible_ssh_timeout', 'ansible_timeout'),
        'private_key_file': ('ansible_ssh_private_key_file', 'ansible_private_key_file'),
        'network_os': ('ansible_network_os',),
        'connection_user': ('ansible_connection_user',),
        'ssh_executable': ('ansible_ssh_executable',),
        'ssh_common_args': ('ansible_ssh_common_args',),
        'sftp_extra_args': ('ansible_sftp_extra_args',),
        'scp_extra_args': ('ansible_scp_extra_args',),
        'ssh_extra_args': ('ansible_ssh_extra_args',),
        'ssh_transfer_method': ('ansible_ssh_transfer_method',),
        'docker_extra_args': ('ansible_docker_extra_args',),
        'become': ('ansible_become',),
        'become_method': ('ansible_become_method',),
        'become_user': ('ansible_become_user',),
        'become_pass': ('ansible_become_password', 'ansible_become_pass'),
        'become_exe': ('ansible_become_exe',),
        'become_flags': ('ansible_become_flags',)
    }), patch('ansible.constants.COMMON_CONNECTION_VARS', frozenset((
        'ansible_connection', 'ansible_host', 'ansible_user', 'ansible_shell_executable', 'ansible_port',
        'ansible_pipelining', 'ansible_password', 'ansible_timeout', 'ansible_shell_type', 'ansible_module_compression',
        'ansible_private_key_file'
    ))), patch('ansible.constants.RESTRICTED_RESULT_KEYS', (
        'ansible_rsync_path', 'ansible_playbook_python', 'ansible_facts'
    )), patch('ansible.constants.INTERNAL_RESULT_KEYS', (
        'add_host', 'add_group'
    )):
        yield

@pytest.fixture
def mock_connection_loader():
    with patch('ansible.plugins.loader.connection_loader.all', return_value=[
        '/path/to/connection/ssh.py',
        '/path/to/connection/docker.py'
    ]):
        yield

@pytest.fixture
def mock_display_warning():
    with patch('ansible.utils.display.Display.warning') as mock_warning:
        yield mock_warning

def test_clean_facts(mock_constants, mock_connection_loader, mock_display_warning):
    facts = {
        'ansible_connection': 'ssh',
        'ansible_host': 'localhost',
        'ansible_user': 'root',
        'ansible_shell_executable': '/bin/bash',
        'ansible_port': 22,
        'ansible_pipelining': True,
        'ansible_password': 'password',
        'ansible_timeout': 10,
        'ansible_shell_type': 'sh',
        'ansible_module_compression': 'ZIP',
        'ansible_private_key_file': '/path/to/key',
        'ansible_ssh_host': 'localhost',
        'ansible_ssh_user': 'root',
        'ansible_ssh_pass': 'password',
        'ansible_ssh_port': 22,
        'ansible_ssh_pipelining': True,
        'ansible_ssh_timeout': 10,
        'ansible_ssh_private_key_file': '/path/to/key',
        'ansible_docker_extra_args': '--privileged',
        'ansible_become': True,
        'ansible_become_method': 'sudo',
        'ansible_become_user': 'root',
        'ansible_become_password': 'password',
        'ansible_become_exe': 'sudo',
        'ansible_become_flags': '-H',
        'ansible_rsync_path': '/usr/bin/rsync',
        'ansible_playbook_python': '/usr/bin/python3',
        'ansible_facts': {},
        'add_host': 'localhost',
        'add_group': 'all',
        'ansible_python_interpreter': '/usr/bin/python3',
        'ansible_ssh_host_key_rsa': 'AAAAB3NzaC1yc2EAAAABIwAAAQEAr...'
    }

    cleaned_facts = clean_facts(facts)

    assert 'ansible_connection' not in cleaned_facts
    assert 'ansible_host' not in cleaned_facts
    assert 'ansible_user' not in cleaned_facts
    assert 'ansible_shell_executable' not in cleaned_facts
    assert 'ansible_port' not in cleaned_facts
    assert 'ansible_pipelining' not in cleaned_facts
    assert 'ansible_password' not in cleaned_facts
    assert 'ansible_timeout' not in cleaned_facts
    assert 'ansible_shell_type' not in cleaned_facts
    assert 'ansible_module_compression' not in cleaned_facts
    assert 'ansible_private_key_file' not in cleaned_facts
    assert 'ansible_ssh_host' not in cleaned_facts
    assert 'ansible_ssh_user' not in cleaned_facts
    assert 'ansible_ssh_pass' not in cleaned_facts
    assert 'ansible_ssh_port' not in cleaned_facts
    assert 'ansible_ssh_pipelining' not in cleaned_facts
    assert 'ansible_ssh_timeout' not in cleaned_facts
    assert 'ansible_ssh_private_key_file' not in cleaned_facts
    assert 'ansible_docker_extra_args' not in cleaned_facts
    assert 'ansible_become' not in cleaned_facts
    assert 'ansible_become_method' not in cleaned_facts
    assert 'ansible_become_user' not in cleaned_facts
    assert 'ansible_become_password' not in cleaned_facts
    assert 'ansible_become_exe' not in cleaned_facts
    assert 'ansible_become_flags' not in cleaned_facts
    assert 'ansible_rsync_path' not in cleaned_facts
    assert 'ansible_playbook_python' not in cleaned_facts
    assert 'ansible_facts' not in cleaned_facts
    assert 'add_host' not in cleaned_facts
    assert 'add_group' not in cleaned_facts
    assert 'ansible_python_interpreter' not in cleaned_facts
    assert 'ansible_ssh_host_key_rsa' in cleaned_facts
