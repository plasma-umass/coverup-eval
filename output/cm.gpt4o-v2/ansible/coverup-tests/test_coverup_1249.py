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

@patch('ansible.modules.apt_repository.apt_pkg')
@patch('ansible.modules.apt_repository.distro')
def test_ubuntu_sources_list_deepcopy(mock_distro, mock_apt_pkg, mock_module):
    # Mock the necessary attributes and methods
    mock_distro.codename = 'focal'
    mock_apt_pkg.config.find_file.return_value = '/etc/apt/sources.list'

    # Create an instance of UbuntuSourcesList
    original = UbuntuSourcesList(mock_module, add_ppa_signing_keys_callback=MagicMock())

    # Perform a deepcopy
    copied = original.__deepcopy__()

    # Assertions to verify the deepcopy
    assert isinstance(copied, UbuntuSourcesList)
    assert copied.module == original.module
    assert copied.add_ppa_signing_keys_callback == original.add_ppa_signing_keys_callback
