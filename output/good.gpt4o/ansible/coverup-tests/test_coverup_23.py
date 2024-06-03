# file lib/ansible/vars/clean.py:118-164
# lines [118, 120, 122, 123, 127, 128, 131, 134, 135, 136, 137, 139, 140, 143, 144, 145, 148, 149, 150, 151, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 164]
# branches ['127->128', '127->131', '134->135', '134->143', '137->134', '137->139', '139->137', '139->140', '143->144', '143->148', '144->143', '144->145', '149->150', '149->153', '150->149', '150->151', '153->154', '153->164', '154->153', '154->155', '157->158', '157->161']

import pytest
from unittest.mock import patch, MagicMock
from ansible.vars.clean import clean_facts
from ansible.utils.display import Display
from ansible.module_utils._text import to_text
from ansible.plugins.loader import connection_loader
import os
import re

@pytest.fixture
def mock_constants(mocker):
    mocker.patch('ansible.vars.clean.C.MAGIC_VARIABLE_MAPPING', {
        'magic_var1': {'var1', 'var2'},
        'magic_var2': {'var3', 'var4'}
    })
    mocker.patch('ansible.vars.clean.C.COMMON_CONNECTION_VARS', {'conn_var1', 'conn_var2'})
    mocker.patch('ansible.vars.clean.C.RESTRICTED_RESULT_KEYS', ['restricted_key1', 'restricted_key2'])
    mocker.patch('ansible.vars.clean.C.INTERNAL_RESULT_KEYS', ['internal_key1', 'internal_key2'])

@pytest.fixture
def mock_connection_loader(mocker):
    mocker.patch('ansible.vars.clean.connection_loader.all', return_value=['/path/to/connection1.py', '/path/to/connection2.py'])

@pytest.fixture
def mock_display(mocker):
    return mocker.patch('ansible.vars.clean.display', new_callable=MagicMock)

@pytest.fixture
def mock_module_response_deepcopy(mocker):
    return mocker.patch('ansible.vars.clean.module_response_deepcopy', side_effect=lambda x: x.copy())

def test_clean_facts(mock_constants, mock_connection_loader, mock_display, mock_module_response_deepcopy):
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

    expected_cleaned_facts = {
        'ansible_ssh_host_key_rsa': 'ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAr...'
    }

    cleaned_facts = clean_facts(facts)

    assert cleaned_facts == expected_cleaned_facts
    assert mock_display.warning.call_count == 12
