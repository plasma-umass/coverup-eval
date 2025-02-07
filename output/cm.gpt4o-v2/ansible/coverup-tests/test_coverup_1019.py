# file: lib/ansible/modules/dnf.py:398-401
# asked: {"lines": [398, 401], "branches": []}
# gained: {"lines": [398, 401], "branches": []}

import pytest
from ansible.modules.dnf import DnfModule
from unittest.mock import MagicMock, patch

@pytest.fixture
def mock_module():
    module = MagicMock()
    module.params = {
        'allowerasing': False,
        'nobest': False,
        'allow_downgrade': False,
        'autoremove': False,
        'bugfix': False,
        'cacheonly': False,
        'conf_file': None,
        'disable_excludes': None,
        'disable_gpg_check': False,
        'disable_plugin': None,
        'disablerepo': [],
        'download_only': False,
        'download_dir': None,
        'enable_plugin': None,
        'enablerepo': [],
        'exclude': [],
        'installroot': '/',
        'install_repoquery': False,
        'install_weak_deps': False,
        'list': None,
        'name': [],
        'releasever': None,
        'security': False,
        'skip_broken': False,
        'state': 'present',
        'update_only': False,
        'update_cache': False,
        'validate_certs': True,
        'lock_timeout': 30
    }
    return module

@patch('ansible.modules.dnf.get_best_parsable_locale', return_value='C')
def test_is_lockfile_pid_valid(mock_get_best_parsable_locale, mock_module):
    dnf_module = DnfModule(mock_module)
    assert dnf_module.is_lockfile_pid_valid() == True
