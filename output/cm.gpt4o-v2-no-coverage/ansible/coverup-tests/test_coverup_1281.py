# file: lib/ansible/playbook/role/requirement.py:67-123
# asked: {"lines": [88, 117], "branches": [[87, 88], [102, 113], [107, 110], [110, 113], [113, 116], [116, 117]]}
# gained: {"lines": [88], "branches": [[87, 88], [113, 116]]}

import pytest
from ansible.errors import AnsibleError
from ansible.playbook.role.requirement import RoleRequirement

VALID_SPEC_KEYS = ['name', 'src', 'scm', 'version']

def test_role_yaml_parse_string_type_single_comma():
    role = "src,version"
    expected = {'name': 'src', 'src': 'src', 'scm': None, 'version': 'version'}
    result = RoleRequirement.role_yaml_parse(role)
    assert result == expected

def test_role_yaml_parse_string_type_double_comma():
    role = "src,version,name"
    expected = {'name': 'name', 'src': 'src', 'scm': None, 'version': 'version'}
    result = RoleRequirement.role_yaml_parse(role)
    assert result == expected

def test_role_yaml_parse_string_type_invalid_format():
    role = "src,version,name,extra"
    with pytest.raises(AnsibleError, match="Invalid role line"):
        RoleRequirement.role_yaml_parse(role)

def test_role_yaml_parse_string_type_no_comma():
    role = "src"
    expected = {'name': 'src', 'src': 'src', 'scm': None, 'version': None}
    result = RoleRequirement.role_yaml_parse(role)
    assert result == expected

def test_role_yaml_parse_string_type_with_scm():
    role = "git+src"
    expected = {'name': 'git+src', 'src': 'src', 'scm': 'git', 'version': None}
    result = RoleRequirement.role_yaml_parse(role)
    assert result == expected

def test_role_yaml_parse_dict_with_role_key():
    role = {'role': 'name'}
    expected = {'name': 'name'}
    result = RoleRequirement.role_yaml_parse(role)
    assert result == expected

def test_role_yaml_parse_dict_with_role_key_invalid_format():
    role = {'role': 'name,extra'}
    with pytest.raises(AnsibleError, match="Invalid old style role requirement"):
        RoleRequirement.role_yaml_parse(role)

def test_role_yaml_parse_dict_with_src_key():
    role = {'src': 'http://github.com/owner/repo'}
    expected = {'name': 'repo', 'src': 'http://github.com/owner/repo', 'scm': 'git', 'version': ''}
    result = RoleRequirement.role_yaml_parse(role)
    assert result == expected

def test_role_yaml_parse_dict_with_src_key_and_scm():
    role = {'src': 'git+http://github.com/owner/repo'}
    expected = {'name': 'repo', 'src': 'http://github.com/owner/repo', 'scm': 'git', 'version': ''}
    result = RoleRequirement.role_yaml_parse(role)
    assert result == expected

def test_role_yaml_parse_dict_with_version_key():
    role = {'src': 'http://github.com/owner/repo', 'version': '1.0'}
    expected = {'name': 'repo', 'src': 'http://github.com/owner/repo', 'scm': 'git', 'version': '1.0'}
    result = RoleRequirement.role_yaml_parse(role)
    assert result == expected

def test_role_yaml_parse_dict_with_extra_keys():
    role = {'src': 'http://github.com/owner/repo', 'extra': 'value'}
    expected = {'name': 'repo', 'src': 'http://github.com/owner/repo', 'scm': 'git', 'version': ''}
    result = RoleRequirement.role_yaml_parse(role)
    assert result == expected
    assert 'extra' not in result
