# file lib/ansible/module_utils/facts/system/distribution.py:154-165
# lines [154, 156, 157, 158, 159, 161, 164, 165]
# branches []

import pytest
from unittest.mock import patch

# Assuming the DistributionFiles class is imported from the module
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def mock_get_distribution_functions(mocker):
    mock_get_distribution = mocker.patch('ansible.module_utils.facts.system.distribution.get_distribution')
    mock_get_distribution_version = mocker.patch('ansible.module_utils.facts.system.distribution.get_distribution_version')
    mock_get_distribution_codename = mocker.patch('ansible.module_utils.facts.system.distribution.get_distribution_codename')
    return mock_get_distribution, mock_get_distribution_version, mock_get_distribution_codename

def test_guess_distribution_all_none(mock_get_distribution_functions):
    mock_get_distribution, mock_get_distribution_version, mock_get_distribution_codename = mock_get_distribution_functions
    mock_get_distribution.return_value = None
    mock_get_distribution_version.return_value = None
    mock_get_distribution_codename.return_value = None

    dist_files = DistributionFiles(module=None)
    result = dist_files._guess_distribution()

    assert result['distribution'] == 'NA'
    assert result['distribution_version'] == 'NA'
    assert result['distribution_release'] == 'NA'
    assert result['distribution_major_version'] == 'NA'

def test_guess_distribution_partial_values(mock_get_distribution_functions):
    mock_get_distribution, mock_get_distribution_version, mock_get_distribution_codename = mock_get_distribution_functions
    mock_get_distribution.return_value = 'Ubuntu'
    mock_get_distribution_version.return_value = '20.04'
    mock_get_distribution_codename.return_value = None

    dist_files = DistributionFiles(module=None)
    result = dist_files._guess_distribution()

    assert result['distribution'] == 'Ubuntu'
    assert result['distribution_version'] == '20.04'
    assert result['distribution_release'] == 'NA'
    assert result['distribution_major_version'] == '20'

def test_guess_distribution_empty_codename(mock_get_distribution_functions):
    mock_get_distribution, mock_get_distribution_version, mock_get_distribution_codename = mock_get_distribution_functions
    mock_get_distribution.return_value = 'Ubuntu'
    mock_get_distribution_version.return_value = '20.04'
    mock_get_distribution_codename.return_value = ''

    dist_files = DistributionFiles(module=None)
    result = dist_files._guess_distribution()

    assert result['distribution'] == 'Ubuntu'
    assert result['distribution_version'] == '20.04'
    assert result['distribution_release'] == ''
    assert result['distribution_major_version'] == '20'
