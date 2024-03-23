# file lib/ansible/module_utils/facts/system/distribution.py:102-108
# lines [102, 104, 105, 107, 108]
# branches ['104->105', '104->107']

import os
import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.system.distribution import DistributionFiles

# Mocking the _file_exists and _get_file_content methods
@pytest.fixture
def mock_distribution_files(mocker):
    module_mock = MagicMock()
    distribution_files = DistributionFiles(module=module_mock)
    mocker.patch('ansible.module_utils.facts.system.distribution._file_exists', return_value=True)
    mocker.patch('ansible.module_utils.facts.system.distribution.get_file_content', return_value='mocked content')
    return distribution_files

# Test to cover the case when the file exists and is not empty
def test_get_dist_file_content_when_file_exists(mock_distribution_files):
    exists, content = mock_distribution_files._get_dist_file_content('/fake/path')
    assert exists is True
    assert content == 'mocked content'

# Test to cover the case when the file does not exist or is empty
def test_get_dist_file_content_when_file_does_not_exist_or_empty(mock_distribution_files, mocker):
    mocker.patch('ansible.module_utils.facts.system.distribution._file_exists', return_value=False)
    exists, content = mock_distribution_files._get_dist_file_content('/fake/path')
    assert exists is False
    assert content is None
