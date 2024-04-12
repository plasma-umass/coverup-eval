# file lib/ansible/modules/apt_repository.py:291-300
# lines [291, 292, 296, 297, 298, 299, 300]
# branches []

import pytest
from unittest.mock import patch, MagicMock

# Assuming the module structure is as follows:
# lib/
# └── ansible/
#     └── modules/
#         └── apt_repository.py

# We need to import the SourcesList class from the apt_repository module
from ansible.modules.apt_repository import SourcesList

# Define a test function for the SourcesList._apt_cfg_dir method
def test_sources_list_apt_cfg_dir(mocker):
    # Mock the apt_pkg module and its config attribute
    apt_pkg_mock = MagicMock()
    mocker.patch('ansible.modules.apt_repository.apt_pkg', new=apt_pkg_mock)

    # Case 1: apt_pkg has the find_dir method
    apt_pkg_mock.config.find_dir.return_value = '/etc/apt'
    assert SourcesList._apt_cfg_dir('Dir') == '/etc/apt'
    apt_pkg_mock.config.find_dir.assert_called_once_with('Dir')

    # Reset mock
    apt_pkg_mock.reset_mock()

    # Case 2: apt_pkg does not have the find_dir method, but has Config.FindDir
    del apt_pkg_mock.config.find_dir
    apt_pkg_mock.Config.FindDir.return_value = '/etc/apt'
    assert SourcesList._apt_cfg_dir('Dir') == '/etc/apt'
    apt_pkg_mock.Config.FindDir.assert_called_once_with('Dir')

    # Clean up by removing the patch
    mocker.stopall()
