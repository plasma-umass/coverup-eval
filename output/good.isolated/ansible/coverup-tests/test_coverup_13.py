# file lib/ansible/playbook/role/requirement.py:67-123
# lines [67, 68, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 81, 83, 85, 86, 87, 88, 90, 92, 93, 94, 95, 97, 98, 100, 102, 104, 105, 107, 108, 110, 111, 113, 114, 116, 117, 119, 120, 121, 123]
# branches ['70->71', '70->92', '75->76', '75->83', '76->77', '76->78', '78->79', '78->81', '85->86', '85->87', '87->88', '87->90', '92->93', '92->100', '94->95', '94->97', '102->104', '102->113', '104->105', '104->107', '107->108', '107->110', '110->111', '110->113', '113->114', '113->116', '116->117', '116->119', '119->120', '119->123', '120->119', '120->121']

import pytest
from ansible.errors import AnsibleError
from ansible.playbook.role.requirement import RoleRequirement

# Assuming VALID_SPEC_KEYS is defined somewhere in the module
# If not, define it for the purpose of this test
VALID_SPEC_KEYS = ['name', 'src', 'scm', 'version']

def test_role_yaml_parse_with_invalid_role_line(mocker):
    with pytest.raises(AnsibleError) as excinfo:
        RoleRequirement.role_yaml_parse("invalid,role,line,with,too,many,commas")
    assert "Invalid role line" in str(excinfo.value)

def test_role_yaml_parse_with_old_style_role_requirement(mocker):
    with pytest.raises(AnsibleError) as excinfo:
        RoleRequirement.role_yaml_parse({'role': 'invalid,role'})
    assert "Invalid old style role requirement" in str(excinfo.value)

def test_role_yaml_parse_with_new_style_role_requirement_and_github_url(mocker):
    mocker.patch.object(RoleRequirement, 'repo_url_to_role_name', return_value='dummy_name')
    result = RoleRequirement.role_yaml_parse({'src': 'http://github.com/username/repo'})
    assert result['src'] == 'http://github.com/username/repo'
    assert result['name'] == 'dummy_name'
    assert result['version'] == ''
    assert result['scm'] == 'git'  # Corrected assertion

def test_role_yaml_parse_with_new_style_role_requirement_and_scm(mocker):
    mocker.patch.object(RoleRequirement, 'repo_url_to_role_name', return_value='dummy_name')
    result = RoleRequirement.role_yaml_parse({'src': 'git+http://github.com/username/repo'})
    assert result['src'] == 'http://github.com/username/repo'
    assert result['scm'] == 'git'
    assert result['name'] == 'dummy_name'
    assert result['version'] == ''

def test_role_yaml_parse_with_new_style_role_requirement_and_extra_keys(mocker):
    mocker.patch.object(RoleRequirement, 'repo_url_to_role_name', return_value='dummy_name')
    result = RoleRequirement.role_yaml_parse({'src': 'http://github.com/username/repo', 'extra_key': 'extra_value'})
    assert 'extra_key' not in result
    assert result['src'] == 'http://github.com/username/repo'
    assert result['name'] == 'dummy_name'
    assert result['version'] == ''
    assert result['scm'] == 'git'  # Corrected assertion
