# file: lib/ansible/vars/clean.py:118-164
# asked: {"lines": [120, 122, 123, 127, 128, 131, 134, 135, 136, 137, 139, 140, 143, 144, 145, 148, 149, 150, 151, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 164], "branches": [[127, 128], [127, 131], [134, 135], [134, 143], [137, 134], [137, 139], [139, 137], [139, 140], [143, 144], [143, 148], [144, 143], [144, 145], [149, 150], [149, 153], [150, 149], [150, 151], [153, 154], [153, 164], [154, 153], [154, 155], [157, 158], [157, 161]]}
# gained: {"lines": [120, 122, 123, 127, 128, 131, 134, 135, 136, 137, 139, 140, 143, 144, 145, 148, 149, 150, 151, 153, 154, 155, 156, 157, 161, 162, 164], "branches": [[127, 128], [127, 131], [134, 135], [134, 143], [137, 134], [137, 139], [139, 137], [139, 140], [143, 144], [143, 148], [144, 143], [144, 145], [149, 150], [149, 153], [150, 149], [150, 151], [153, 154], [153, 164], [154, 155], [157, 161]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.vars.clean import clean_facts
from ansible.module_utils.common.text.converters import to_text
from ansible.utils.display import Display
from ansible.plugins.loader import connection_loader
import ansible.constants as C

@pytest.fixture
def mock_constants(monkeypatch):
    monkeypatch.setattr(C, 'MAGIC_VARIABLE_MAPPING', {
        'magic_var1': {'var1', 'var2'},
        'magic_var2': {'var3', 'var4'}
    })
    monkeypatch.setattr(C, 'COMMON_CONNECTION_VARS', {'conn_var1', 'conn_var2'})
    monkeypatch.setattr(C, 'RESTRICTED_RESULT_KEYS', ['restricted_key1', 'restricted_key2'])
    monkeypatch.setattr(C, 'INTERNAL_RESULT_KEYS', ['internal_key1', 'internal_key2'])

@pytest.fixture
def mock_connection_loader(monkeypatch):
    mock_loader = MagicMock()
    mock_loader.all.return_value = ['/path/to/connection1.py', '/path/to/connection2.py']
    monkeypatch.setattr(connection_loader, 'all', mock_loader.all)

@pytest.fixture
def mock_display(monkeypatch):
    mock_display = MagicMock(spec=Display)
    monkeypatch.setattr('ansible.vars.clean.display', mock_display)
    return mock_display

@pytest.fixture
def mock_module_response_deepcopy(monkeypatch):
    def mock_deepcopy(data):
        return data.copy()
    monkeypatch.setattr('ansible.vars.clean.module_response_deepcopy', mock_deepcopy)

@pytest.fixture
def mock_strip_internal_keys(monkeypatch):
    def mock_strip(data):
        return data
    monkeypatch.setattr('ansible.vars.clean.strip_internal_keys', mock_strip)

def test_clean_facts(mock_constants, mock_connection_loader, mock_display, mock_module_response_deepcopy, mock_strip_internal_keys):
    facts = {
        'var1': 'value1',
        'var2': 'value2',
        'var3': 'value3',
        'var4': 'value4',
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

    assert 'var1' not in cleaned_facts
    assert 'var2' not in cleaned_facts
    assert 'var3' not in cleaned_facts
    assert 'var4' not in cleaned_facts
    assert 'conn_var1' not in cleaned_facts
    assert 'conn_var2' not in cleaned_facts
    assert 'ansible_connection1_var' not in cleaned_facts
    assert 'ansible_connection2_var' not in cleaned_facts
    assert 'ansible_become_var' not in cleaned_facts
    assert 'restricted_key1' not in cleaned_facts
    assert 'internal_key1' not in cleaned_facts
    assert 'ansible_python_interpreter' not in cleaned_facts
    assert 'ansible_ssh_host_key_rsa' in cleaned_facts

    mock_display.warning.assert_any_call("Removed restricted key from module data: var1 = value1")
    mock_display.warning.assert_any_call("Removed restricted key from module data: var2 = value2")
    mock_display.warning.assert_any_call("Removed restricted key from module data: var3 = value3")
    mock_display.warning.assert_any_call("Removed restricted key from module data: var4 = value4")
    mock_display.warning.assert_any_call("Removed restricted key from module data: conn_var1 = conn_value1")
    mock_display.warning.assert_any_call("Removed restricted key from module data: conn_var2 = conn_value2")
    mock_display.warning.assert_any_call("Removed restricted key from module data: ansible_connection1_var = conn1_value")
    mock_display.warning.assert_any_call("Removed restricted key from module data: ansible_connection2_var = conn2_value")
    mock_display.warning.assert_any_call("Removed restricted key from module data: ansible_become_var = become_value")
    mock_display.warning.assert_any_call("Removed restricted key from module data: restricted_key1 = restricted_value1")
    mock_display.warning.assert_any_call("Removed restricted key from module data: internal_key1 = internal_value1")
    mock_display.warning.assert_any_call("Removed restricted key from module data: ansible_python_interpreter = /usr/bin/python")
