# file: lib/ansible/vars/clean.py:118-164
# asked: {"lines": [118, 120, 122, 123, 127, 128, 131, 134, 135, 136, 137, 139, 140, 143, 144, 145, 148, 149, 150, 151, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 164], "branches": [[127, 128], [127, 131], [134, 135], [134, 143], [137, 134], [137, 139], [139, 137], [139, 140], [143, 144], [143, 148], [144, 143], [144, 145], [149, 150], [149, 153], [150, 149], [150, 151], [153, 154], [153, 164], [154, 153], [154, 155], [157, 158], [157, 161]]}
# gained: {"lines": [118, 120, 122, 123, 127, 128, 131, 134, 135, 136, 137, 139, 140, 143, 144, 145, 148, 149, 150, 151, 153, 154, 155, 156, 157, 159, 160, 161, 162, 164], "branches": [[127, 128], [127, 131], [134, 135], [134, 143], [137, 134], [137, 139], [139, 137], [139, 140], [143, 144], [143, 148], [144, 143], [144, 145], [149, 150], [149, 153], [150, 149], [150, 151], [153, 154], [153, 164], [154, 155], [157, 161]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.vars.clean import clean_facts
from ansible.module_utils.common.text.converters import to_text
from ansible.utils.display import Display

@pytest.fixture
def mock_constants(monkeypatch):
    class MockConstants:
        MAGIC_VARIABLE_MAPPING = {
            'magic_var1': {'key1', 'key2'},
            'magic_var2': {'key3', 'key4'}
        }
        COMMON_CONNECTION_VARS = {'conn_var1', 'conn_var2'}
        RESTRICTED_RESULT_KEYS = ['restricted_key1', 'restricted_key2']
        INTERNAL_RESULT_KEYS = ['internal_key1', 'internal_key2']

    monkeypatch.setattr('ansible.vars.clean.C', MockConstants)

@pytest.fixture
def mock_connection_loader(monkeypatch):
    mock_loader = MagicMock()
    mock_loader.all.return_value = ['/path/to/connection1.py', '/path/to/connection2.py']
    monkeypatch.setattr('ansible.vars.clean.connection_loader', mock_loader)

@pytest.fixture
def mock_display(monkeypatch):
    display = MagicMock(wraps=Display())
    monkeypatch.setattr('ansible.vars.clean.display', display)
    return display

def test_clean_facts_removes_magic_vars(mock_constants, mock_connection_loader, mock_display):
    facts = {
        'key1': 'value1',
        'key2': 'value2',
        'key3': 'value3',
        'key4': 'value4',
        'conn_var1': 'conn_value1',
        'conn_var2': 'conn_value2',
        'ansible_connection1_var': 'conn1_value',
        'ansible_connection2_var': 'conn2_value',
        'ansible_become_var': 'become_value',
        'restricted_key1': 'restricted_value1',
        'internal_key1': 'internal_value1',
        'ansible_python_interpreter': '/usr/bin/python',
        'ansible_ssh_host_key_rsa': 'ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAr...'
    }

    cleaned_facts = clean_facts(facts)

    assert 'key1' not in cleaned_facts
    assert 'key2' not in cleaned_facts
    assert 'key3' not in cleaned_facts
    assert 'key4' not in cleaned_facts
    assert 'conn_var1' not in cleaned_facts
    assert 'conn_var2' not in cleaned_facts
    assert 'ansible_connection1_var' not in cleaned_facts
    assert 'ansible_connection2_var' not in cleaned_facts
    assert 'ansible_become_var' not in cleaned_facts
    assert 'restricted_key1' not in cleaned_facts
    assert 'internal_key1' not in cleaned_facts
    assert 'ansible_python_interpreter' not in cleaned_facts
    assert 'ansible_ssh_host_key_rsa' in cleaned_facts

def test_clean_facts_handles_conversion_errors(mock_constants, mock_connection_loader, mock_display):
    facts = {
        'key1': 'value1',
        'restricted_key1': object()  # This will cause a conversion error
    }

    with patch('ansible.vars.clean.to_text', side_effect=Exception('conversion error')):
        cleaned_facts = clean_facts(facts)

    assert 'restricted_key1' not in cleaned_facts
    assert mock_display.warning.called
    warning_call_args = mock_display.warning.call_args_list
    assert any(' <failed to convert value to a string> ' in call[0][0] for call in warning_call_args)
