# file lib/ansible/playbook/role/include.py:36-60
# lines [36, 38, 43, 44, 46, 47, 48, 50, 51, 53, 54, 56, 57, 59, 60]
# branches ['53->54', '53->56', '56->57', '56->59']

import pytest
from ansible.playbook.role.include import RoleInclude
from ansible.errors import AnsibleParserError, AnsibleError
from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
from ansible.module_utils._text import to_native
from ansible.module_utils.six import string_types

def test_role_include_load_invalid_data():
    with pytest.raises(AnsibleParserError, match="Invalid role definition:"):
        RoleInclude.load(123, play=None)

def test_role_include_load_invalid_old_style_role():
    with pytest.raises(AnsibleError, match="Invalid old style role requirement:"):
        RoleInclude.load("role1,role2", play=None)

def test_role_include_load_valid_string_data(mocker):
    mocker.patch('ansible.playbook.role.include.RoleInclude.load_data', return_value="mocked_data")
    result = RoleInclude.load("valid_role", play=None)
    assert result == "mocked_data"

def test_role_include_load_valid_dict_data(mocker):
    mocker.patch('ansible.playbook.role.include.RoleInclude.load_data', return_value="mocked_data")
    result = RoleInclude.load({"name": "valid_role"}, play=None)
    assert result == "mocked_data"

def test_role_include_load_valid_ansible_base_yaml_object(mocker):
    mocker.patch('ansible.playbook.role.include.RoleInclude.load_data', return_value="mocked_data")
    yaml_object = AnsibleBaseYAMLObject()
    result = RoleInclude.load(yaml_object, play=None)
    assert result == "mocked_data"
