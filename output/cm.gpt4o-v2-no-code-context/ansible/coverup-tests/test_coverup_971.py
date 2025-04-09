# file: lib/ansible/playbook/role/definition.py:114-135
# asked: {"lines": [121, 122, 124, 125, 126, 130, 131, 132, 133, 135], "branches": [[121, 122], [121, 124], [125, 126], [125, 130], [130, 131], [130, 135]]}
# gained: {"lines": [121, 122, 124, 125, 126, 130, 131, 132, 133, 135], "branches": [[121, 122], [121, 124], [125, 126], [125, 130], [130, 131], [130, 135]]}

import pytest
from ansible.playbook.role.definition import RoleDefinition
from ansible.errors import AnsibleError
from ansible.template import Templar
from unittest.mock import Mock

@pytest.fixture
def role_definition():
    return RoleDefinition()

def test_load_role_name_with_string(role_definition):
    ds = "simple_role_name"
    result = role_definition._load_role_name(ds)
    assert result == ds

def test_load_role_name_with_dict_role(role_definition):
    ds = {"role": "complex_role_name"}
    result = role_definition._load_role_name(ds)
    assert result == "complex_role_name"

def test_load_role_name_with_dict_name(role_definition):
    ds = {"name": "complex_role_name"}
    result = role_definition._load_role_name(ds)
    assert result == "complex_role_name"

def test_load_role_name_with_invalid_dict(role_definition):
    ds = {"invalid_key": "no_role_name"}
    with pytest.raises(AnsibleError, match="role definitions must contain a role name"):
        role_definition._load_role_name(ds)

def test_load_role_name_with_variable_manager(monkeypatch, role_definition):
    ds = {"role": "complex_role_name"}
    mock_variable_manager = Mock()
    mock_variable_manager.get_vars.return_value = {"var1": "value1"}
    mock_templar = Mock()
    mock_templar.template.return_value = "templated_role_name"
    
    monkeypatch.setattr(role_definition, '_variable_manager', mock_variable_manager)
    monkeypatch.setattr(role_definition, '_loader', Mock())
    
    def mock_templar_init(self, loader, variables):
        self.template = mock_templar.template
    
    monkeypatch.setattr(Templar, '__init__', mock_templar_init)
    
    result = role_definition._load_role_name(ds)
    assert result == "templated_role_name"
    mock_variable_manager.get_vars.assert_called_once_with(play=role_definition._play)
    mock_templar.template.assert_called_once_with("complex_role_name")
