# file lib/ansible/module_utils/facts/system/distribution.py:102-108
# lines [102, 104, 105, 107, 108]
# branches ['104->105', '104->107']

import pytest
from unittest import mock

# Assuming the DistributionFiles class is imported from the module
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def distribution_files(mocker):
    mock_module = mocker.Mock()
    return DistributionFiles(mock_module)

def test_get_dist_file_content_file_not_exists(mocker, distribution_files):
    mocker.patch('ansible.module_utils.facts.system.distribution._file_exists', return_value=False)
    result, data = distribution_files._get_dist_file_content('/non/existent/path')
    assert result is False
    assert data is None

def test_get_dist_file_content_file_exists(mocker, distribution_files):
    mocker.patch('ansible.module_utils.facts.system.distribution._file_exists', return_value=True)
    mocker.patch.object(distribution_files, '_get_file_content', return_value='file content')
    result, data = distribution_files._get_dist_file_content('/existent/path')
    assert result is True
    assert data == 'file content'
