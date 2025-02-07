# file: lib/ansible/playbook/role/definition.py:69-112
# asked: {"lines": [72, 73, 75, 76, 78, 79, 82, 87, 88, 89, 94, 95, 100, 101, 102, 103, 106, 109, 112], "branches": [[72, 73], [72, 75], [75, 76], [75, 78], [78, 79], [78, 82], [88, 89], [88, 94], [100, 101], [100, 106]]}
# gained: {"lines": [72, 73, 75, 76, 78, 79, 82, 87, 88, 89, 94, 95, 100, 101, 102, 103, 106, 109, 112], "branches": [[72, 73], [72, 75], [75, 76], [75, 78], [78, 79], [78, 82], [88, 89], [88, 94], [100, 101], [100, 106]]}

import pytest
from ansible.errors import AnsibleAssertionError, AnsibleError
from ansible.module_utils.six import string_types
from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject, AnsibleMapping
from ansible.playbook.role.definition import RoleDefinition

@pytest.fixture
def role_definition(mocker):
    mock_loader = mocker.Mock()
    mock_loader.get_basedir.return_value = '/mock_basedir'
    return RoleDefinition(loader=mock_loader, variable_manager=mocker.Mock(), collection_list=[])

def test_preprocess_data_with_int(role_definition):
    result = role_definition.preprocess_data(123)
    assert isinstance(result, AnsibleMapping)
    assert result['role'] == '123'

def test_preprocess_data_with_invalid_type(role_definition):
    with pytest.raises(AnsibleAssertionError):
        role_definition.preprocess_data([])

def test_preprocess_data_with_dict(role_definition, mocker):
    mocker.patch.object(RoleDefinition, '_load_role_name', return_value='test_role')
    mocker.patch.object(RoleDefinition, '_load_role_path', return_value=('test_role', '/path/to/role'))
    mocker.patch.object(RoleDefinition, '_split_role_params', return_value=({'key': 'value'}, {'param': 'value'}))
    
    ds = {'role': 'test_role'}
    result = role_definition.preprocess_data(ds)
    
    assert isinstance(result, AnsibleMapping)
    assert result['role'] == 'test_role'
    assert role_definition._role_path == '/path/to/role'
    assert role_definition._role_params == {'param': 'value'}

def test_preprocess_data_with_ansible_base_yaml_object(role_definition, mocker):
    class MockAnsibleBaseYAMLObject(AnsibleBaseYAMLObject):
        def __init__(self):
            self.ansible_pos = ('mock_source', 1, 1)
    
    mock_ds = MockAnsibleBaseYAMLObject()
    mocker.patch.object(RoleDefinition, '_load_role_name', return_value='test_role')
    mocker.patch.object(RoleDefinition, '_load_role_path', return_value=('test_role', '/path/to/role'))
    
    result = role_definition.preprocess_data(mock_ds)
    
    assert isinstance(result, AnsibleMapping)
    assert result.ansible_pos == ('mock_source', 1, 1)
    assert result['role'] == 'test_role'
    assert role_definition._role_path == '/path/to/role'
