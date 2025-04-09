# file lib/ansible/playbook/role/definition.py:114-135
# lines [121, 122, 124, 125, 126, 130, 131, 132, 133, 135]
# branches ['121->122', '121->124', '125->126', '125->130', '130->131', '130->135']

import pytest
from ansible.playbook.role.definition import RoleDefinition
from ansible.errors import AnsibleError
from ansible.template import Templar
from unittest.mock import MagicMock

@pytest.fixture
def role_definition():
    return RoleDefinition()

def test_load_role_name_string(role_definition):
    ds = "simple_role_name"
    result = role_definition._load_role_name(ds)
    assert result == ds

def test_load_role_name_dict_with_role(role_definition):
    ds = {"role": "complex_role_name"}
    role_definition._variable_manager = None
    result = role_definition._load_role_name(ds)
    assert result == "complex_role_name"

def test_load_role_name_dict_with_name(role_definition):
    ds = {"name": "complex_role_name"}
    role_definition._variable_manager = None
    result = role_definition._load_role_name(ds)
    assert result == "complex_role_name"

def test_load_role_name_missing_name(role_definition):
    ds = {"not_role": "no_name"}
    with pytest.raises(AnsibleError, match="role definitions must contain a role name"):
        role_definition._load_role_name(ds)

def test_load_role_name_with_variable_manager(role_definition, mocker):
    ds = {"role": "complex_role_name"}
    mock_variable_manager = mocker.MagicMock()
    mock_variable_manager.get_vars.return_value = {"some_var": "some_value"}
    mock_templar = mocker.patch('ansible.playbook.role.definition.Templar')
    mock_templar_instance = mock_templar.return_value
    mock_templar_instance.template.return_value = "templated_role_name"

    role_definition._variable_manager = mock_variable_manager
    role_definition._loader = MagicMock()
    role_definition._play = MagicMock()

    result = role_definition._load_role_name(ds)
    assert result == "templated_role_name"
    mock_variable_manager.get_vars.assert_called_once_with(play=role_definition._play)
    mock_templar.assert_called_once_with(loader=role_definition._loader, variables={"some_var": "some_value"})
    mock_templar_instance.template.assert_called_once_with("complex_role_name")
