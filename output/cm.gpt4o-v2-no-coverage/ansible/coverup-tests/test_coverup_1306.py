# file: lib/ansible/modules/apt_repository.py:454-456
# asked: {"lines": [455, 456], "branches": []}
# gained: {"lines": [455, 456], "branches": []}

import pytest
from unittest.mock import Mock, patch
from ansible.modules.apt_repository import UbuntuSourcesList

@pytest.fixture
def mock_module():
    mock = Mock()
    mock.params = {'codename': 'focal'}
    return mock

@pytest.fixture
def ubuntu_sources_list(mock_module):
    with patch('ansible.modules.apt_repository.apt_pkg') as mock_apt_pkg:
        mock_apt_pkg.config = Mock()
        mock_apt_pkg.config.find_file = Mock(return_value='/mock/path')
        return UbuntuSourcesList(module=mock_module)

def test_key_already_exists(ubuntu_sources_list, mock_module):
    key_fingerprint = "dummy_fingerprint"
    
    # Mock the run_command method
    mock_module.run_command = Mock(return_value=(0, "output", ""))
    
    # Call the method
    result = ubuntu_sources_list._key_already_exists(key_fingerprint)
    
    # Assertions
    mock_module.run_command.assert_called_once_with(f'apt-key export {key_fingerprint}', check_rc=True)
    assert result == True

    # Test with error output
    mock_module.run_command = Mock(return_value=(0, "output", "error"))
    result = ubuntu_sources_list._key_already_exists(key_fingerprint)
    assert result == False
