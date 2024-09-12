# file: lib/ansible/playbook/role_include.py:127-166
# asked: {"lines": [127, 128, 130, 133, 136, 137, 138, 140, 141, 144, 145, 146, 149, 150, 151, 152, 153, 154, 156, 157, 158, 159, 160, 163, 164, 166], "branches": [[137, 138], [137, 140], [140, 141], [140, 144], [145, 146], [145, 149], [149, 150], [149, 156], [152, 153], [152, 154], [157, 158], [157, 159], [159, 160], [159, 163], [163, 164], [163, 166]]}
# gained: {"lines": [127, 128, 130, 133, 136, 137, 138, 140, 141, 144, 145, 146, 149, 150, 151, 152, 153, 154, 156, 157, 158, 159, 160, 163, 164, 166], "branches": [[137, 138], [137, 140], [140, 141], [140, 144], [145, 146], [145, 149], [149, 150], [149, 156], [152, 153], [152, 154], [157, 158], [157, 159], [159, 160], [159, 163], [163, 164], [163, 166]]}

import pytest
from ansible.playbook.role_include import IncludeRole
from ansible.errors import AnsibleParserError
from unittest.mock import MagicMock

def test_include_role_load_valid_data(monkeypatch):
    data = {
        'name': 'test_role',
        'tasks_from': 'tasks/main.yml',
        'apply': {'key': 'value'}
    }
    block = MagicMock()
    role = MagicMock()
    task_include = MagicMock()
    variable_manager = MagicMock()
    loader = MagicMock()

    mock_load_data = MagicMock()
    mock_load_data.args = data
    mock_load_data.action = 'include_role'
    mock_load_data._from_files = {}
    monkeypatch.setattr(IncludeRole, 'load_data', MagicMock(return_value=mock_load_data))

    ir = IncludeRole.load(data, block, role, task_include, variable_manager, loader)

    assert ir._role_name == 'test_role'
    assert ir._from_files['tasks'] == 'main.yml'
    assert ir.apply == {'key': 'value'}

def test_include_role_load_missing_name(monkeypatch):
    data = {
        'tasks_from': 'tasks/main.yml'
    }
    block = MagicMock()
    role = MagicMock()
    task_include = MagicMock()
    variable_manager = MagicMock()
    loader = MagicMock()

    mock_load_data = MagicMock()
    mock_load_data.args = data
    mock_load_data.action = 'include_role'
    monkeypatch.setattr(IncludeRole, 'load_data', MagicMock(return_value=mock_load_data))

    with pytest.raises(AnsibleParserError, match="'name' is a required field for include_role."):
        IncludeRole.load(data, block, role, task_include, variable_manager, loader)

def test_include_role_load_invalid_public_option(monkeypatch):
    data = {
        'name': 'test_role',
        'public': True
    }
    block = MagicMock()
    role = MagicMock()
    task_include = MagicMock()
    variable_manager = MagicMock()
    loader = MagicMock()

    mock_load_data = MagicMock()
    mock_load_data.args = data
    mock_load_data.action = 'invalid_action'
    monkeypatch.setattr(IncludeRole, 'load_data', MagicMock(return_value=mock_load_data))

    with pytest.raises(AnsibleParserError, match='Invalid options for invalid_action: public'):
        IncludeRole.load(data, block, role, task_include, variable_manager, loader)

def test_include_role_load_invalid_apply_option(monkeypatch):
    data = {
        'name': 'test_role',
        'apply': {'key': 'value'}
    }
    block = MagicMock()
    role = MagicMock()
    task_include = MagicMock()
    variable_manager = MagicMock()
    loader = MagicMock()

    mock_load_data = MagicMock()
    mock_load_data.args = data
    mock_load_data.action = 'invalid_action'
    monkeypatch.setattr(IncludeRole, 'load_data', MagicMock(return_value=mock_load_data))

    with pytest.raises(AnsibleParserError, match='Invalid options for invalid_action: apply'):
        IncludeRole.load(data, block, role, task_include, variable_manager, loader)

def test_include_role_load_invalid_apply_type(monkeypatch):
    data = {
        'name': 'test_role',
        'apply': 'not_a_dict'
    }
    block = MagicMock()
    role = MagicMock()
    task_include = MagicMock()
    variable_manager = MagicMock()
    loader = MagicMock()

    mock_load_data = MagicMock()
    mock_load_data.args = data
    mock_load_data.action = 'include_role'
    monkeypatch.setattr(IncludeRole, 'load_data', MagicMock(return_value=mock_load_data))

    with pytest.raises(AnsibleParserError, match='Expected a dict for apply but got <class \'str\'> instead'):
        IncludeRole.load(data, block, role, task_include, variable_manager, loader)

def test_include_role_load_invalid_from_type(monkeypatch):
    data = {
        'name': 'test_role',
        'tasks_from': 123
    }
    block = MagicMock()
    role = MagicMock()
    task_include = MagicMock()
    variable_manager = MagicMock()
    loader = MagicMock()

    mock_load_data = MagicMock()
    mock_load_data.args = data
    mock_load_data.action = 'include_role'
    monkeypatch.setattr(IncludeRole, 'load_data', MagicMock(return_value=mock_load_data))

    with pytest.raises(AnsibleParserError, match='Expected a string for tasks_from but got <class \'int\'> instead'):
        IncludeRole.load(data, block, role, task_include, variable_manager, loader)

def test_include_role_load_invalid_options(monkeypatch):
    data = {
        'name': 'test_role',
        'invalid_option': 'value'
    }
    block = MagicMock()
    role = MagicMock()
    task_include = MagicMock()
    variable_manager = MagicMock()
    loader = MagicMock()

    mock_load_data = MagicMock()
    mock_load_data.args = data
    mock_load_data.action = 'include_role'
    monkeypatch.setattr(IncludeRole, 'load_data', MagicMock(return_value=mock_load_data))

    with pytest.raises(AnsibleParserError, match='Invalid options for include_role: invalid_option'):
        IncludeRole.load(data, block, role, task_include, variable_manager, loader)
