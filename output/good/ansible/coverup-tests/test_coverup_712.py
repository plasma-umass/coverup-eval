# file lib/ansible/modules/apt_repository.py:428-432
# lines [428, 429, 430, 431]
# branches []

import pytest
from unittest.mock import MagicMock, patch
from ansible.modules.apt_repository import UbuntuSourcesList

@pytest.fixture
def mock_module():
    mock = MagicMock()
    return mock

@pytest.fixture
def mock_add_ppa_signing_keys_callback():
    return MagicMock()

@pytest.fixture
def mock_apt_pkg():
    apt_pkg_mock = MagicMock()
    apt_pkg_mock.config.find_file.return_value = '/etc/apt/sources.list'
    return apt_pkg_mock

def test_ubuntu_sources_list_deepcopy(mock_module, mock_add_ppa_signing_keys_callback, mock_apt_pkg):
    with patch('ansible.modules.apt_repository.apt_pkg', mock_apt_pkg):
        original = UbuntuSourcesList(mock_module, add_ppa_signing_keys_callback=mock_add_ppa_signing_keys_callback)
        copied = original.__deepcopy__()

    assert isinstance(copied, UbuntuSourcesList)
    assert copied.module is mock_module
    assert copied.add_ppa_signing_keys_callback is mock_add_ppa_signing_keys_callback
