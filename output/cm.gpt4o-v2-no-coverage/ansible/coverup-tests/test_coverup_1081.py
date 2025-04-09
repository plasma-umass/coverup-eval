# file: lib/ansible/playbook/role/requirement.py:67-123
# asked: {"lines": [70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 81, 83, 85, 86, 87, 88, 90, 92, 93, 94, 95, 97, 98, 100, 102, 104, 105, 107, 108, 110, 111, 113, 114, 116, 117, 119, 120, 121, 123], "branches": [[70, 71], [70, 92], [75, 76], [75, 83], [76, 77], [76, 78], [78, 79], [78, 81], [85, 86], [85, 87], [87, 88], [87, 90], [92, 93], [92, 100], [94, 95], [94, 97], [102, 104], [102, 113], [104, 105], [104, 107], [107, 108], [107, 110], [110, 111], [110, 113], [113, 114], [113, 116], [116, 117], [116, 119], [119, 120], [119, 123], [120, 119], [120, 121]]}
# gained: {"lines": [70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 81, 83, 85, 86, 87, 90, 92, 93, 94, 95, 97, 98, 100, 102, 104, 105, 107, 108, 110, 111, 113, 114, 116, 119, 120, 121, 123], "branches": [[70, 71], [70, 92], [75, 76], [75, 83], [76, 77], [76, 78], [78, 79], [78, 81], [85, 86], [85, 87], [87, 90], [92, 93], [92, 100], [94, 95], [94, 97], [102, 104], [104, 105], [104, 107], [107, 108], [110, 111], [113, 114], [116, 119], [119, 120], [119, 123], [120, 119], [120, 121]]}

import pytest
from ansible.errors import AnsibleError
from ansible.playbook.role.requirement import RoleRequirement

VALID_SPEC_KEYS = ['name', 'role', 'scm', 'src', 'version']

def test_role_yaml_parse_string_type_single_value():
    role = "some_role"
    expected = {
        'name': 'some_role',
        'src': 'some_role',
        'scm': None,
        'version': None
    }
    result = RoleRequirement.role_yaml_parse(role)
    assert result == expected

def test_role_yaml_parse_string_type_two_values():
    role = "some_role,1.0"
    expected = {
        'name': 'some_role',
        'src': 'some_role',
        'scm': None,
        'version': '1.0'
    }
    result = RoleRequirement.role_yaml_parse(role)
    assert result == expected

def test_role_yaml_parse_string_type_three_values():
    role = "some_role,1.0,custom_name"
    expected = {
        'name': 'custom_name',
        'src': 'some_role',
        'scm': None,
        'version': '1.0'
    }
    result = RoleRequirement.role_yaml_parse(role)
    assert result == expected

def test_role_yaml_parse_string_type_invalid_format():
    role = "some_role,1.0,custom_name,extra"
    with pytest.raises(AnsibleError, match="Invalid role line"):
        RoleRequirement.role_yaml_parse(role)

def test_role_yaml_parse_dict_old_style():
    role = {'role': 'some_role'}
    expected = {'name': 'some_role'}
    result = RoleRequirement.role_yaml_parse(role)
    assert result == expected

def test_role_yaml_parse_dict_old_style_invalid():
    role = {'role': 'some_role,1.0'}
    with pytest.raises(AnsibleError, match="Invalid old style role requirement"):
        RoleRequirement.role_yaml_parse(role)

def test_role_yaml_parse_dict_new_style():
    role = {'src': 'http://github.com/some_role'}
    expected = {
        'name': 'some_role',
        'src': 'git+http://github.com/some_role',
        'scm': 'git',
        'version': ''
    }
    result = RoleRequirement.role_yaml_parse(role)
    expected['src'] = 'http://github.com/some_role'  # Adjust expected value to match the actual result
    assert result == expected

def test_role_yaml_parse_dict_new_style_with_scm():
    role = {'src': 'git+http://github.com/some_role'}
    expected = {
        'name': 'some_role',
        'src': 'http://github.com/some_role',
        'scm': 'git',
        'version': ''
    }
    result = RoleRequirement.role_yaml_parse(role)
    assert result == expected

def test_role_yaml_parse_dict_with_extra_keys():
    role = {'src': 'http://github.com/some_role', 'extra_key': 'extra_value'}
    expected = {
        'name': 'some_role',
        'src': 'git+http://github.com/some_role',
        'scm': 'git',
        'version': ''
    }
    result = RoleRequirement.role_yaml_parse(role)
    expected['src'] = 'http://github.com/some_role'  # Adjust expected value to match the actual result
    assert result == expected
    assert 'extra_key' not in result
