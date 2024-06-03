# file lib/ansible/module_utils/facts/system/distribution.py:99-100
# lines [99, 100]
# branches []

import pytest
from unittest.mock import patch

# Assuming the DistributionFiles class is imported from the module
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def mock_get_file_content(mocker):
    return mocker.patch('ansible.module_utils.facts.system.distribution.get_file_content')

def test_get_file_content(mock_get_file_content):
    # Arrange
    mock_get_file_content.return_value = "test content"
    dist_files = DistributionFiles(module=None)  # Pass a dummy value for the required argument
    test_path = "/fake/path"

    # Act
    result = dist_files._get_file_content(test_path)

    # Assert
    mock_get_file_content.assert_called_once_with(test_path)
    assert result == "test content"
