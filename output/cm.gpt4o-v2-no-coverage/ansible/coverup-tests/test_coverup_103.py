# file: lib/ansible/playbook/role/definition.py:69-112
# asked: {"lines": [69, 72, 73, 75, 76, 78, 79, 82, 87, 88, 89, 94, 95, 100, 101, 102, 103, 106, 109, 112], "branches": [[72, 73], [72, 75], [75, 76], [75, 78], [78, 79], [78, 82], [88, 89], [88, 94], [100, 101], [100, 106]]}
# gained: {"lines": [69, 72, 73, 75, 76, 78, 79, 82, 87, 88, 89, 94, 95, 100, 101, 102, 103, 106, 109, 112], "branches": [[72, 73], [72, 75], [75, 76], [75, 78], [78, 79], [78, 82], [88, 89], [88, 94], [100, 101], [100, 106]]}

import pytest
from ansible.errors import AnsibleAssertionError
from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject, AnsibleMapping
from ansible.playbook.role.definition import RoleDefinition

class MockAnsibleBaseYAMLObject(AnsibleBaseYAMLObject):
    def __init__(self, ansible_pos=None):
        if ansible_pos:
            self.ansible_pos = ansible_pos

    @property
    def ansible_pos(self):
        return (self._data_source, self._line_number, self._column_number)

    @ansible_pos.setter
    def ansible_pos(self, value):
        if isinstance(value, tuple) and len(value) == 3:
            self._data_source, self._line_number, self._column_number = value
        else:
            raise AssertionError(
                'ansible_pos can only be set with a tuple/list of three values: source, line number, column number'
            )

class MockRoleDefinition(RoleDefinition):
    def _load_role_name(self, ds):
        return "mock_role_name"
    
    def _load_role_path(self, role_name):
        return (role_name, "mock_role_path")
    
    def _split_role_params(self, ds):
        return ({"mock_key": "mock_value"}, {"param_key": "param_value"})

@pytest.fixture
def role_definition():
    return MockRoleDefinition()

def test_preprocess_data_with_int(role_definition):
    result = role_definition.preprocess_data(123)
    assert role_definition._ds == "123"
    assert result['role'] == "mock_role_name"
    assert role_definition._role_path == "mock_role_path"

def test_preprocess_data_with_invalid_type(role_definition):
    with pytest.raises(AnsibleAssertionError):
        role_definition.preprocess_data([])

def test_preprocess_data_with_dict(role_definition):
    ds = {"some_key": "some_value"}
    result = role_definition.preprocess_data(ds)
    assert role_definition._ds == ds
    assert result['role'] == "mock_role_name"
    assert role_definition._role_path == "mock_role_path"
    assert role_definition._role_params == {"param_key": "param_value"}
    assert result["mock_key"] == "mock_value"

def test_preprocess_data_with_ansible_base_yaml_object(role_definition):
    ds = MockAnsibleBaseYAMLObject(ansible_pos=("mock_source", 1, 1))
    result = role_definition.preprocess_data(ds)
    assert role_definition._ds == ds
    assert result['role'] == "mock_role_name"
    assert role_definition._role_path == "mock_role_path"
    assert result.ansible_pos == ("mock_source", 1, 1)
