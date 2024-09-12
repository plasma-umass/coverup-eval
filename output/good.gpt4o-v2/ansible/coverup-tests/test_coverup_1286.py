# file: lib/ansible/modules/apt_repository.py:454-456
# asked: {"lines": [455, 456], "branches": []}
# gained: {"lines": [455, 456], "branches": []}

import pytest
from unittest.mock import Mock, patch
from ansible.modules.apt_repository import UbuntuSourcesList

@pytest.fixture
def mock_module():
    module = Mock()
    module.params = {'codename': 'focal'}
    return module

@pytest.fixture(autouse=True)
def mock_apt_pkg():
    with patch('ansible.modules.apt_repository.apt_pkg') as mock_apt:
        mock_apt.config.find_file.return_value = '/etc/apt/sources.list'
        yield mock_apt

def test_key_already_exists(mock_module):
    ubuntu_sources_list = UbuntuSourcesList(mock_module)
    key_fingerprint = "ABC123"

    with patch.object(mock_module, 'run_command', return_value=(0, "output", "")) as mock_run_command:
        result = ubuntu_sources_list._key_already_exists(key_fingerprint)
        mock_run_command.assert_called_once_with('apt-key export ABC123', check_rc=True)
        assert result == True

    with patch.object(mock_module, 'run_command', return_value=(0, "output", "error")) as mock_run_command:
        result = ubuntu_sources_list._key_already_exists(key_fingerprint)
        mock_run_command.assert_called_once_with('apt-key export ABC123', check_rc=True)
        assert result == False
