# file: lib/ansible/playbook/role/include.py:36-60
# asked: {"lines": [47, 48, 53, 54, 56, 57, 59, 60], "branches": [[53, 54], [53, 56], [56, 57], [56, 59]]}
# gained: {"lines": [47, 48, 53, 54, 56, 57, 59, 60], "branches": [[53, 54], [53, 56], [56, 57], [56, 59]]}

import pytest
from ansible.playbook.role.include import RoleInclude
from ansible.errors import AnsibleParserError, AnsibleError
from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
from ansible.module_utils.six import string_types
from unittest.mock import Mock

def test_role_include_init(mocker):
    mock_super_init = mocker.patch('ansible.playbook.role.include.RoleDefinition.__init__')
    play = Mock()
    role_basedir = Mock()
    variable_manager = Mock()
    loader = Mock()
    collection_list = Mock()
    
    role_include = RoleInclude(play=play, role_basedir=role_basedir, variable_manager=variable_manager, loader=loader, collection_list=collection_list)
    
    mock_super_init.assert_called_once_with(play=play, role_basedir=role_basedir, variable_manager=variable_manager, loader=loader, collection_list=collection_list)

def test_role_include_load_invalid_data():
    play = Mock()
    with pytest.raises(AnsibleParserError, match="Invalid role definition:"):
        RoleInclude.load(data=123, play=play)

def test_role_include_load_invalid_old_style_role():
    play = Mock()
    with pytest.raises(AnsibleError, match="Invalid old style role requirement:"):
        RoleInclude.load(data="role1,role2", play=play)

def test_role_include_load_valid_data(mocker):
    play = Mock()
    variable_manager = Mock()
    loader = Mock()
    current_role_path = Mock()
    collection_list = Mock()
    data = Mock(spec=AnsibleBaseYAMLObject)
    
    mock_load_data = mocker.patch.object(RoleInclude, 'load_data', return_value='loaded_data')
    
    result = RoleInclude.load(data=data, play=play, current_role_path=current_role_path, variable_manager=variable_manager, loader=loader, collection_list=collection_list)
    
    assert result == 'loaded_data'
    mock_load_data.assert_called_once_with(data, variable_manager=variable_manager, loader=loader)
