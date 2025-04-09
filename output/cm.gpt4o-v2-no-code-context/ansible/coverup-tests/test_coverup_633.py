# file: lib/ansible/playbook/role/requirement.py:125-128
# asked: {"lines": [125, 126, 128], "branches": []}
# gained: {"lines": [125, 126, 128], "branches": []}

import pytest
from ansible.playbook.role.requirement import RoleRequirement
from ansible.playbook.role.requirement import scm_archive_resource

@pytest.fixture
def mock_scm_archive_resource(mocker):
    return mocker.patch('ansible.playbook.role.requirement.scm_archive_resource')

def test_scm_archive_role_git(mock_scm_archive_resource):
    src = 'some_repo_url'
    scm = 'git'
    name = 'role_name'
    version = 'v1.0'
    keep_scm_meta = True

    RoleRequirement.scm_archive_role(src, scm=scm, name=name, version=version, keep_scm_meta=keep_scm_meta)
    
    mock_scm_archive_resource.assert_called_once_with(src, scm=scm, name=name, version=version, keep_scm_meta=keep_scm_meta)

def test_scm_archive_role_default(mock_scm_archive_resource):
    src = 'some_repo_url'

    RoleRequirement.scm_archive_role(src)
    
    mock_scm_archive_resource.assert_called_once_with(src, scm='git', name=None, version='HEAD', keep_scm_meta=False)
