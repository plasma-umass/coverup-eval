# file lib/ansible/modules/apt_repository.py:280-289
# lines [287, 288]
# branches []

import pytest
from unittest.mock import MagicMock, patch

# Assuming the module structure is as follows:
# lib/
# └── ansible/
#     └── modules/
#         └── apt_repository.py

# We will import the SourcesList class from the apt_repository module
from ansible.modules.apt_repository import SourcesList

# Test function to cover the missing lines 287-288
def test_sources_list_apt_cfg_file_attribute_error(mocker):
    # Mock the apt_pkg module and its config attribute
    apt_pkg_mock = MagicMock()
    apt_pkg_mock.config.find_file.side_effect = AttributeError
    apt_pkg_mock.Config.FindFile.return_value = '/etc/apt/sources.list'

    # Patch the apt_pkg import in the apt_repository module
    with patch('ansible.modules.apt_repository.apt_pkg', new=apt_pkg_mock):
        # Call the method that we want to test
        result = SourcesList._apt_cfg_file('sources.list')

        # Assert that the AttributeError was caught and the fallback method was called
        apt_pkg_mock.Config.FindFile.assert_called_once_with('sources.list')

        # Assert that the result is as expected
        assert result == '/etc/apt/sources.list'
