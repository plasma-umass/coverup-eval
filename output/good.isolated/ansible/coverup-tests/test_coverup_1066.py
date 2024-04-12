# file lib/ansible/module_utils/facts/system/distribution.py:99-100
# lines [99, 100]
# branches []

import pytest
from ansible.module_utils.facts.system.distribution import DistributionFiles
from unittest.mock import MagicMock

# Mock the get_file_content function
@pytest.fixture
def mock_get_file_content(mocker):
    return mocker.patch('ansible.module_utils.facts.system.distribution.get_file_content', return_value='mocked content')

# Test function to improve coverage
def test__get_file_content(mock_get_file_content):
    module_mock = MagicMock()
    distribution_files = DistributionFiles(module=module_mock)
    content = distribution_files._get_file_content('/fake/path')

    # Verify that the mocked get_file_content was called with the correct path
    mock_get_file_content.assert_called_once_with('/fake/path')

    # Verify that the content returned is the mocked content
    assert content == 'mocked content'
