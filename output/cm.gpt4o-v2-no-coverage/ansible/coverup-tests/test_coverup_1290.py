# file: lib/ansible/modules/apt_repository.py:428-432
# asked: {"lines": [429, 430, 431], "branches": []}
# gained: {"lines": [429, 430, 431], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.modules.apt_repository import UbuntuSourcesList, SourcesList

@pytest.fixture
def mock_module():
    module = MagicMock()
    module.params = {'codename': 'focal'}
    return module

@patch('ansible.modules.apt_repository.apt_pkg', autospec=True)
@patch('ansible.modules.apt_repository.distro', autospec=True)
def test_ubuntu_sources_list_deepcopy(mock_distro, mock_apt_pkg, mock_module):
    # Mock the add_ppa_signing_keys_callback
    mock_callback = MagicMock()

    # Mock the distro.codename
    mock_distro.codename = 'focal'

    # Create an instance of UbuntuSourcesList
    ubuntu_sources_list = UbuntuSourcesList(mock_module, add_ppa_signing_keys_callback=mock_callback)

    # Perform a deepcopy
    copied_list = ubuntu_sources_list.__deepcopy__()

    # Assertions to verify the deepcopy
    assert isinstance(copied_list, UbuntuSourcesList)
    assert copied_list.module == ubuntu_sources_list.module
    assert copied_list.add_ppa_signing_keys_callback == ubuntu_sources_list.add_ppa_signing_keys_callback
