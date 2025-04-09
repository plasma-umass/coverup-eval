# file: lib/ansible/vars/clean.py:118-164
# asked: {"lines": [118, 120, 122, 123, 127, 128, 131, 134, 135, 136, 137, 139, 140, 143, 144, 145, 148, 149, 150, 151, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 164], "branches": [[127, 128], [127, 131], [134, 135], [134, 143], [137, 134], [137, 139], [139, 137], [139, 140], [143, 144], [143, 148], [144, 143], [144, 145], [149, 150], [149, 153], [150, 149], [150, 151], [153, 154], [153, 164], [154, 153], [154, 155], [157, 158], [157, 161]]}
# gained: {"lines": [118, 120, 122, 123, 127, 128, 131, 134, 135, 136, 137, 139, 140, 143, 144, 145, 148, 149, 150, 151, 153, 154, 155, 156, 157, 161, 162, 164], "branches": [[127, 128], [127, 131], [134, 135], [134, 143], [137, 134], [137, 139], [139, 137], [139, 140], [143, 144], [143, 148], [144, 143], [144, 145], [149, 150], [149, 153], [150, 149], [150, 151], [153, 154], [153, 164], [154, 153], [154, 155], [157, 161]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.vars.clean import clean_facts
from ansible import constants as C
from ansible.module_utils._text import to_text
from ansible.plugins.loader import connection_loader

@pytest.fixture
def mock_display_warning(mocker):
    return mocker.patch('ansible.utils.display.Display.warning')

@pytest.fixture
def mock_connection_loader(mocker):
    mock_loader = mocker.patch('ansible.plugins.loader.connection_loader')
    mock_loader.all.return_value = ['/path/to/connection/plugin']
    return mock_loader

@pytest.fixture
def mock_constants(mocker):
    mocker.patch('ansible.constants.MAGIC_VARIABLE_MAPPING', {
        'connection': ('ansible_connection',),
        'module_compression': ('ansible_module_compression',),
    })
    mocker.patch('ansible.constants.COMMON_CONNECTION_VARS', frozenset(('ansible_connection', 'ansible_host')))
    mocker.patch('ansible.constants.RESTRICTED_RESULT_KEYS', ('ansible_rsync_path', 'ansible_playbook_python', 'ansible_facts'))
    mocker.patch('ansible.constants.INTERNAL_RESULT_KEYS', ('add_host', 'add_group'))

def test_clean_facts_removes_magic_vars(mock_constants, mock_display_warning):
    facts = {
        'ansible_connection': 'ssh',
        'ansible_host': 'localhost',
        'custom_fact': 'value'
    }
    cleaned_facts = clean_facts(facts)
    assert 'ansible_connection' not in cleaned_facts
    assert 'ansible_host' not in cleaned_facts
    assert 'custom_fact' in cleaned_facts

def test_clean_facts_removes_common_connection_vars(mock_constants, mock_display_warning):
    facts = {
        'ansible_connection': 'ssh',
        'ansible_host': 'localhost',
        'custom_fact': 'value'
    }
    cleaned_facts = clean_facts(facts)
    assert 'ansible_connection' not in cleaned_facts
    assert 'ansible_host' not in cleaned_facts
    assert 'custom_fact' in cleaned_facts

def test_clean_facts_removes_plugin_specific_vars(mock_constants, mock_connection_loader, mock_display_warning):
    facts = {
        'ansible_paramiko_ssh_user': 'user',
        'ansible_become_user': 'root',
        'custom_fact': 'value'
    }
    cleaned_facts = clean_facts(facts)
    assert 'ansible_paramiko_ssh_user' not in cleaned_facts
    assert 'ansible_become_user' not in cleaned_facts
    assert 'custom_fact' in cleaned_facts

def test_clean_facts_removes_restricted_and_internal_keys(mock_constants, mock_display_warning):
    facts = {
        'ansible_rsync_path': '/usr/bin/rsync',
        'add_host': 'localhost',
        'custom_fact': 'value'
    }
    cleaned_facts = clean_facts(facts)
    assert 'ansible_rsync_path' not in cleaned_facts
    assert 'add_host' not in cleaned_facts
    assert 'custom_fact' in cleaned_facts

def test_clean_facts_removes_interpreter_keys(mock_constants, mock_display_warning):
    facts = {
        'ansible_python_interpreter': '/usr/bin/python3',
        'custom_fact': 'value'
    }
    cleaned_facts = clean_facts(facts)
    assert 'ansible_python_interpreter' not in cleaned_facts
    assert 'custom_fact' in cleaned_facts

def test_clean_facts_does_not_remove_ssh_host_keys(mock_constants, mock_display_warning):
    facts = {
        'ansible_ssh_host_key_rsa': 'AAAAB3NzaC1yc2EAAAABIwAAAQEAr...',
        'custom_fact': 'value'
    }
    cleaned_facts = clean_facts(facts)
    assert 'ansible_ssh_host_key_rsa' in cleaned_facts
    assert 'custom_fact' in cleaned_facts
