# file lib/ansible/playbook/role/requirement.py:51-65
# lines [51, 52, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65]
# branches ['56->57', '56->58', '59->60', '59->61', '61->62', '61->63', '63->64', '63->65']

import pytest
from ansible.playbook.role.requirement import RoleRequirement

def test_repo_url_to_role_name():
    # Test with a URL containing '://'
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.git') == 'repo'
    # Test with a URL containing '@'
    assert RoleRequirement.repo_url_to_role_name('git@example.com:repos/repo.git') == 'repo'
    # Test with a URL containing '.tar.gz'
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo.tar.gz') == 'repo'
    # Test with a URL containing a comma
    assert RoleRequirement.repo_url_to_role_name('http://git.example.com/repos/repo,something.git') == 'repo'
    # Test with a string that does not contain '://' or '@'
    assert RoleRequirement.repo_url_to_role_name('just-a-repo-name') == 'just-a-repo-name'
