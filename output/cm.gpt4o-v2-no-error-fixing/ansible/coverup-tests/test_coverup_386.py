# file: lib/ansible/module_utils/facts/system/distribution.py:102-108
# asked: {"lines": [102, 104, 105, 107, 108], "branches": [[104, 105], [104, 107]]}
# gained: {"lines": [102, 104, 105, 107, 108], "branches": [[104, 105], [104, 107]]}

import os
import pytest
from unittest.mock import patch, mock_open
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def distribution_files():
    module = None  # Replace with actual module if needed
    return DistributionFiles(module)

def test_get_dist_file_content_file_not_exists(distribution_files):
    with patch('ansible.module_utils.facts.system.distribution._file_exists', return_value=False):
        result = distribution_files._get_dist_file_content('/non/existent/path')
        assert result == (False, None)

def test_get_dist_file_content_file_exists(distribution_files):
    with patch('ansible.module_utils.facts.system.distribution._file_exists', return_value=True), \
         patch('ansible.module_utils.facts.system.distribution.DistributionFiles._get_file_content', return_value='file content'):
        result = distribution_files._get_dist_file_content('/existent/path')
        assert result == (True, 'file content')

def test_get_dist_file_content_allow_empty(distribution_files):
    with patch('ansible.module_utils.facts.system.distribution._file_exists', return_value=True), \
         patch('ansible.module_utils.facts.system.distribution.DistributionFiles._get_file_content', return_value=''):
        result = distribution_files._get_dist_file_content('/empty/path', allow_empty=True)
        assert result == (True, '')

def test_get_dist_file_content_not_allow_empty(distribution_files):
    with patch('ansible.module_utils.facts.system.distribution._file_exists', return_value=False):
        result = distribution_files._get_dist_file_content('/empty/path', allow_empty=False)
        assert result == (False, None)
