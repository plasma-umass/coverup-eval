# file lib/ansible/playbook/role_include.py:127-166
# lines [130, 133, 136, 137, 138, 140, 141, 144, 145, 146, 149, 150, 151, 152, 153, 154, 156, 157, 158, 159, 160, 163, 164, 166]
# branches ['137->138', '137->140', '140->141', '140->144', '145->146', '145->149', '149->150', '149->156', '152->153', '152->154', '157->158', '157->159', '159->160', '159->163', '163->164', '163->166']

import pytest
from ansible.playbook.role_include import IncludeRole
from ansible.errors import AnsibleParserError
from unittest.mock import Mock, patch
from os.path import basename

def test_include_role_load(mocker):
    # Mocking the necessary components
    block = Mock()
    role = Mock()
    task_include = Mock()
    variable_manager = Mock()
    loader = Mock()

    # Mocking the data to trigger the specific lines
    data = {
        'name': 'test_role',
        'public': True,
        'apply': {'some_key': 'some_value'},
        'src_from': 'some_path'
    }

    # Mocking constants
    mocker.patch('ansible.playbook.role_include.C._ACTION_INCLUDE_ROLE', ['include_role'])

    # Mocking the IncludeRole.VALID_ARGS and other attributes
    mocker.patch.object(IncludeRole, 'VALID_ARGS', new_callable=lambda: frozenset(['name', 'public', 'apply', 'src_from']))
    mocker.patch.object(IncludeRole, 'FROM_ARGS', new_callable=lambda: frozenset(['src_from']))
    mocker.patch.object(IncludeRole, 'OTHER_ARGS', new_callable=lambda: frozenset(['public', 'apply']))

    # Mocking the load_data method to return a mock object with args
    mock_load_data = Mock()
    mock_load_data.args = data
    mock_load_data.action = 'include_role'
    mocker.patch.object(IncludeRole, 'load_data', return_value=mock_load_data)

    # Mocking the _from_files attribute to be a dictionary
    mock_load_data._from_files = {}

    # Test the load method
    ir = IncludeRole.load(data, block=block, role=role, task_include=task_include, variable_manager=variable_manager, loader=loader)

    # Assertions to verify the postconditions
    assert ir._role_name == 'test_role'
    assert ir._from_files['src'] == 'some_path'
    assert ir.public == True
    assert ir.apply == {'some_key': 'some_value'}

    # Clean up
    del ir

def test_include_role_load_invalid_option(mocker):
    # Mocking the necessary components
    block = Mock()
    role = Mock()
    task_include = Mock()
    variable_manager = Mock()
    loader = Mock()

    # Mocking the data to trigger the specific lines
    data = {
        'name': 'test_role',
        'public': True,
        'apply': {'some_key': 'some_value'},
        'invalid_option': 'invalid_value',
        'src_from': 'some_path'
    }

    # Mocking constants
    mocker.patch('ansible.playbook.role_include.C._ACTION_INCLUDE_ROLE', ['include_role'])

    # Mocking the IncludeRole.VALID_ARGS and other attributes
    mocker.patch.object(IncludeRole, 'VALID_ARGS', new_callable=lambda: frozenset(['name', 'public', 'apply', 'src_from']))
    mocker.patch.object(IncludeRole, 'FROM_ARGS', new_callable=lambda: frozenset(['src_from']))
    mocker.patch.object(IncludeRole, 'OTHER_ARGS', new_callable=lambda: frozenset(['public', 'apply']))

    # Mocking the load_data method to return a mock object with args
    mock_load_data = Mock()
    mock_load_data.args = data
    mock_load_data.action = 'include_role'
    mocker.patch.object(IncludeRole, 'load_data', return_value=mock_load_data)

    # Mocking the _from_files attribute to be a dictionary
    mock_load_data._from_files = {}

    # Test the load method and expect an error
    with pytest.raises(AnsibleParserError, match="Invalid options for include_role: invalid_option"):
        IncludeRole.load(data, block=block, role=role, task_include=task_include, variable_manager=variable_manager, loader=loader)
