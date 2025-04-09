# file: lib/ansible/playbook/role_include.py:127-166
# asked: {"lines": [130, 133, 136, 137, 138, 140, 141, 144, 145, 146, 149, 150, 151, 152, 153, 154, 156, 157, 158, 159, 160, 163, 164, 166], "branches": [[137, 138], [137, 140], [140, 141], [140, 144], [145, 146], [145, 149], [149, 150], [149, 156], [152, 153], [152, 154], [157, 158], [157, 159], [159, 160], [159, 163], [163, 164], [163, 166]]}
# gained: {"lines": [130, 133, 136, 137, 138, 140, 141, 144, 145, 146, 149, 150, 151, 152, 153, 156, 157, 159, 160, 163, 164, 166], "branches": [[137, 138], [137, 140], [140, 141], [140, 144], [145, 146], [145, 149], [149, 150], [149, 156], [152, 153], [157, 159], [159, 160], [159, 163], [163, 164], [163, 166]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.errors import AnsibleParserError
from ansible.playbook.role_include import IncludeRole

@pytest.fixture
def mock_task_include():
    with patch('ansible.playbook.role_include.TaskInclude.load_data') as mock_load_data:
        yield mock_load_data

def test_load_with_valid_data(mock_task_include):
    data = {'name': 'test_role'}
    mock_task_include.return_value = MagicMock(args=data, action='include_role')

    ir = IncludeRole.load(data)
    assert ir._role_name == 'test_role'

def test_load_missing_name_and_role(mock_task_include):
    data = {}
    mock_task_include.return_value = MagicMock(args=data, action='include_role')

    with pytest.raises(AnsibleParserError, match="'name' is a required field"):
        IncludeRole.load(data)

def test_load_invalid_public_option(mock_task_include):
    data = {'name': 'test_role', 'public': True}
    mock_task_include.return_value = MagicMock(args=data, action='invalid_action')

    with pytest.raises(AnsibleParserError, match="Invalid options for invalid_action: public"):
        IncludeRole.load(data)

def test_load_invalid_args(mock_task_include):
    data = {'name': 'test_role', 'invalid_arg': 'value'}
    mock_task_include.return_value = MagicMock(args=data, action='include_role')

    with pytest.raises(AnsibleParserError, match="Invalid options for include_role: invalid_arg"):
        IncludeRole.load(data)

def test_load_from_args_not_string(mock_task_include):
    data = {'name': 'test_role', 'tasks_from': 123}
    mock_task_include.return_value = MagicMock(args=data, action='include_role')

    with pytest.raises(AnsibleParserError, match="Expected a string for tasks_from but got <class 'int'> instead"):
        IncludeRole.load(data)

def test_load_apply_not_dict(mock_task_include):
    data = {'name': 'test_role', 'apply': 'not_a_dict'}
    mock_task_include.return_value = MagicMock(args=data, action='include_role')

    with pytest.raises(AnsibleParserError, match="Expected a dict for apply but got <class 'str'> instead"):
        IncludeRole.load(data)

def test_load_with_apply(mock_task_include):
    data = {'name': 'test_role', 'apply': {'key': 'value'}}
    mock_task_include.return_value = MagicMock(args=data, action='include_role')

    ir = IncludeRole.load(data)
    assert ir.apply == {'key': 'value'}
