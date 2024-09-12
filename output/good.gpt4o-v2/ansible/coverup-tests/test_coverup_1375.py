# file: lib/ansible/playbook/role/include.py:36-60
# asked: {"lines": [47, 48, 53, 54, 56, 57, 59, 60], "branches": [[53, 54], [53, 56], [56, 57], [56, 59]]}
# gained: {"lines": [47, 48, 53, 54, 56, 57, 59, 60], "branches": [[53, 54], [53, 56], [56, 57], [56, 59]]}

import pytest
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.module_utils.six import string_types
from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
from ansible.playbook.role.include import RoleInclude
from ansible.module_utils._text import to_native

def test_role_include_init(mocker):
    mock_super_init = mocker.patch('ansible.playbook.role.definition.RoleDefinition.__init__')
    play = mocker.Mock()
    role_basedir = 'test_dir'
    variable_manager = mocker.Mock()
    loader = mocker.Mock()
    collection_list = mocker.Mock()

    role_include = RoleInclude(play=play, role_basedir=role_basedir, variable_manager=variable_manager, loader=loader, collection_list=collection_list)

    mock_super_init.assert_called_once_with(play=play, role_basedir=role_basedir, variable_manager=variable_manager, loader=loader, collection_list=collection_list)

def test_role_include_load_invalid_data_type():
    play = None
    invalid_data = 12345  # Not a string, dict, or AnsibleBaseYAMLObject

    with pytest.raises(AnsibleParserError, match="Invalid role definition: %s" % to_native(invalid_data)):
        RoleInclude.load(invalid_data, play)

def test_role_include_load_invalid_old_style_role():
    play = None
    invalid_data = "invalid,role,style"

    with pytest.raises(AnsibleError, match="Invalid old style role requirement: %s" % invalid_data):
        RoleInclude.load(invalid_data, play)

def test_role_include_load_valid_data(mocker):
    play = mocker.Mock()
    valid_data = "valid_role"
    current_role_path = 'test_path'
    variable_manager = mocker.Mock()
    loader = mocker.Mock()
    collection_list = mocker.Mock()

    mock_load_data = mocker.patch.object(RoleInclude, 'load_data', return_value='loaded_data')

    result = RoleInclude.load(valid_data, play, current_role_path=current_role_path, variable_manager=variable_manager, loader=loader, collection_list=collection_list)

    assert result == 'loaded_data'
    mock_load_data.assert_called_once_with(valid_data, variable_manager=variable_manager, loader=loader)
