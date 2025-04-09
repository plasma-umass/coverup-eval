# file: lib/ansible/playbook/role/requirement.py:51-65
# asked: {"lines": [51, 52, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65], "branches": [[56, 57], [56, 58], [59, 60], [59, 61], [61, 62], [61, 63], [63, 64], [63, 65]]}
# gained: {"lines": [51, 52, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65], "branches": [[56, 57], [56, 58], [59, 60], [59, 61], [61, 62], [61, 63], [63, 64], [63, 65]]}

import pytest
from ansible.playbook.role.requirement import RoleRequirement

class TestRoleRequirement:
    
    @pytest.mark.parametrize("repo_url, expected", [
        ("http://git.example.com/repos/repo.git", "repo"),
        ("http://git.example.com/repos/repo.tar.gz", "repo"),
        ("http://git.example.com/repos/repo,branch", "repo"),
        ("http://git.example.com/repos/repo", "repo"),
        ("ssh://git@example.com/repo.git", "repo"),
        ("ssh://git@example.com/repo.tar.gz", "repo"),
        ("ssh://git@example.com/repo,branch", "repo"),
        ("ssh://git@example.com/repo", "repo"),
        ("repo", "repo"),
    ])
    def test_repo_url_to_role_name(self, repo_url, expected):
        assert RoleRequirement.repo_url_to_role_name(repo_url) == expected
