# file lib/ansible/module_utils/facts/system/distribution.py:47-95
# lines [47, 48, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 80, 81, 82, 83, 84, 90, 91, 94]
# branches []

import os
import pytest
from unittest.mock import MagicMock

# Assuming the DistributionFiles class is part of a module named distribution
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def mock_os_path_exists(mocker):
    return mocker.patch('os.path.exists')

@pytest.fixture
def mock_open(mocker):
    return mocker.patch('builtins.open', mocker.mock_open(read_data='Oracle Linux'))

@pytest.fixture
def mock_module():
    module = MagicMock()
    return module

def test_distribution_files_oraclelinux(mock_os_path_exists, mock_open, mock_module):
    # Mock os.path.exists to only return True for /etc/oracle-release
    mock_os_path_exists.side_effect = lambda x: x == '/etc/oracle-release'

    # Instantiate the DistributionFiles class with a mock module
    dist_files = DistributionFiles(mock_module)

    # Find the OracleLinux entry
    oracle_entry = next((entry for entry in dist_files.OSDIST_LIST if entry['name'] == 'OracleLinux'), None)
    assert oracle_entry is not None

    # Check if the file exists
    assert os.path.exists(oracle_entry['path'])

    # Open the file and read its content
    with open(oracle_entry['path'], 'r') as f:
        content = f.read()

    # Assert that the content matches the expected search string
    assert dist_files.SEARCH_STRING['OracleLinux'] in content
