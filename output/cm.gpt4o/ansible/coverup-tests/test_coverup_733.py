# file lib/ansible/modules/apt_repository.py:454-456
# lines [454, 455, 456]
# branches []

import pytest
from unittest.mock import MagicMock, patch

# Assuming the class UbuntuSourcesList is defined in the module ansible.modules.apt_repository
from ansible.modules.apt_repository import UbuntuSourcesList

@pytest.fixture
def mock_module(mocker):
    return mocker.MagicMock()

@pytest.fixture
def ubuntu_sources_list(mock_module):
    with patch('ansible.modules.apt_repository.apt_pkg') as mock_apt_pkg:
        mock_apt_pkg.config.find_file.return_value = '/etc/apt/sources.list'
        return UbuntuSourcesList(module=mock_module)

def test_key_already_exists_success(ubuntu_sources_list, mock_module):
    key_fingerprint = 'test-fingerprint'
    mock_module.run_command.return_value = (0, 'some output', '')

    result = ubuntu_sources_list._key_already_exists(key_fingerprint)

    mock_module.run_command.assert_called_once_with(f'apt-key export {key_fingerprint}', check_rc=True)
    assert result is True

def test_key_already_exists_failure(ubuntu_sources_list, mock_module):
    key_fingerprint = 'test-fingerprint'
    mock_module.run_command.return_value = (1, '', 'some error')

    result = ubuntu_sources_list._key_already_exists(key_fingerprint)

    mock_module.run_command.assert_called_once_with(f'apt-key export {key_fingerprint}', check_rc=True)
    assert result is False
