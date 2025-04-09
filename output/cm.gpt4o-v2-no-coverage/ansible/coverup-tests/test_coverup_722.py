# file: lib/ansible/modules/yum_repository.py:575-578
# asked: {"lines": [575, 577, 578], "branches": [[577, 0], [577, 578]]}
# gained: {"lines": [575, 577, 578], "branches": [[577, 0], [577, 578]]}

import pytest
from unittest.mock import Mock, patch

@pytest.fixture
def mock_module():
    module = Mock()
    module.params = {
        'repoid': 'test-repo',
        'reposdir': '/tmp/repos',
        'file': 'test'
    }
    return module

@pytest.fixture
def yum_repo(mock_module):
    with patch('os.path.isdir', return_value=True), \
         patch('os.path.isfile', return_value=True), \
         patch('configparser.ConfigParser.read', return_value=True):
        from ansible.modules.yum_repository import YumRepo
        return YumRepo(mock_module)

def test_remove_section_exists(yum_repo):
    yum_repo.repofile = Mock()
    yum_repo.repofile.has_section.return_value = True

    yum_repo.remove()

    yum_repo.repofile.has_section.assert_called_once_with('test-repo')
    yum_repo.repofile.remove_section.assert_called_once_with('test-repo')

def test_remove_section_not_exists(yum_repo):
    yum_repo.repofile = Mock()
    yum_repo.repofile.has_section.return_value = False

    yum_repo.remove()

    yum_repo.repofile.has_section.assert_called_once_with('test-repo')
    yum_repo.repofile.remove_section.assert_not_called()
