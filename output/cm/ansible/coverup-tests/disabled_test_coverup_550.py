# file lib/ansible/modules/apt_repository.py:280-289
# lines [280, 281, 285, 286, 287, 288, 289]
# branches []

import pytest
from unittest.mock import MagicMock, patch

# Assuming the module structure is as follows:
# lib/
# └── ansible/
#     └── modules/
#         └── apt_repository.py

# We need to import the SourcesList class from the apt_repository module
from ansible.modules.apt_repository import SourcesList

# Mocking the apt_pkg module since it's not available in a standard Python environment
# and we don't want to actually interact with the system's package manager in a test.
apt_pkg_mock = MagicMock()

# Define the test function
def test_sources_list_apt_cfg_file(mocker):
    # Patch the apt_pkg module with our mock
    mocker.patch('ansible.modules.apt_repository.apt_pkg', new=apt_pkg_mock)

    # Set up the mock to raise an AttributeError when `config.find_file` is called
    apt_pkg_mock.config.find_file.side_effect = AttributeError

    # Call the method we want to test
    result = SourcesList._apt_cfg_file('some_file')

    # Assert that the fallback method `Config.FindFile` was called
    apt_pkg_mock.Config.FindFile.assert_called_once_with('some_file')

    # Assert that the result is what the fallback method returned
    assert result == apt_pkg_mock.Config.FindFile.return_value

    # Clean up by stopping the patcher
    mocker.stopall()
