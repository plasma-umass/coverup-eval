# file lib/ansible/playbook/role/definition.py:69-112
# lines [69, 72, 73, 75, 76, 78, 79, 82, 87, 88, 89, 94, 95, 100, 101, 102, 103, 106, 109, 112]
# branches ['72->73', '72->75', '75->76', '75->78', '78->79', '78->82', '88->89', '88->94', '100->101', '100->106']

import pytest
from ansible.playbook.role.definition import RoleDefinition
from ansible.errors import AnsibleAssertionError
from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject, AnsibleMapping
from ansible.module_utils.six import string_types

class MockBase:
    def preprocess_data(self, ds):
        return ds

class MockConditional:
    pass

class MockTaggable:
    pass

class MockCollectionSearch:
    pass

class MockRoleDefinition(RoleDefinition, MockBase, MockConditional, MockTaggable, MockCollectionSearch):
    def _load_role_name(self, ds):
        return "mock_role_name"

    def _load_role_path(self, role_name):
        return (role_name, "/mock/role/path")

    def _split_role_params(self, ds):
        return ({"mock_key": "mock_value"}, {"param_key": "param_value"})

@pytest.fixture
def role_definition():
    return MockRoleDefinition()

def test_preprocess_data_with_int(role_definition):
    ds = 123
    result = role_definition.preprocess_data(ds)
    assert role_definition._ds == "123"
    assert result['role'] == "mock_role_name"

def test_preprocess_data_with_invalid_type(role_definition):
    ds = []
    with pytest.raises(AnsibleAssertionError):
        role_definition.preprocess_data(ds)

def test_preprocess_data_with_dict(role_definition):
    ds = {"role": "test_role"}
    result = role_definition.preprocess_data(ds)
    assert role_definition._ds == ds
    assert result['role'] == "mock_role_name"
    assert role_definition._role_params == {"param_key": "param_value"}

def test_preprocess_data_with_ansible_base_yaml_object(role_definition, mocker):
    ds = mocker.Mock(spec=AnsibleBaseYAMLObject)
    ds.ansible_pos = ("mock_source", 1, 1)
    result = role_definition.preprocess_data(ds)
    assert role_definition._ds == ds
    assert result.ansible_pos == ("mock_source", 1, 1)
    assert result['role'] == "mock_role_name"
