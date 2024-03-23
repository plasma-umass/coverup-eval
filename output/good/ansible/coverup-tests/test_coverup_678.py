# file lib/ansible/modules/apt_repository.py:422-426
# lines [422, 423, 424, 425, 426]
# branches []

import pytest
from unittest.mock import MagicMock, patch

# Assuming the module under test is named 'ansible.modules.apt_repository'
# and it contains a class named 'UbuntuSourcesList'
from ansible.modules.apt_repository import UbuntuSourcesList

@pytest.fixture
def mock_module():
    mock_module = MagicMock()
    mock_module.params = {'codename': None}
    return mock_module

@pytest.fixture
def mock_distro(mocker):
    mocker.patch('ansible.modules.apt_repository.distro', codename='focal')

@pytest.fixture
def mock_apt_pkg(mocker):
    apt_pkg_mock = MagicMock()
    config_mock = MagicMock()
    config_mock.find_file.return_value = '/etc/apt/sources.list'
    apt_pkg_mock.config = config_mock
    mocker.patch('ansible.modules.apt_repository.apt_pkg', new=apt_pkg_mock)
    return apt_pkg_mock

def test_ubuntu_sources_list_init_with_none_codename(mock_module, mock_distro, mock_apt_pkg):
    # Setup callback function
    def mock_add_ppa_signing_keys_callback():
        pass

    # Instantiate UbuntuSourcesList with None codename
    ubuntu_sources_list = UbuntuSourcesList(mock_module, mock_add_ppa_signing_keys_callback)

    # Assertions to verify postconditions
    assert ubuntu_sources_list.module == mock_module
    assert ubuntu_sources_list.add_ppa_signing_keys_callback == mock_add_ppa_signing_keys_callback
    assert ubuntu_sources_list.codename == 'focal'  # codename should be set to the mocked distro codename

    # Clean up is handled by the fixture scope
