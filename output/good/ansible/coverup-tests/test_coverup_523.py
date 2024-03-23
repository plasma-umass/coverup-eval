# file lib/ansible/module_utils/facts/system/distribution.py:154-165
# lines [154, 156, 157, 158, 159, 161, 164, 165]
# branches []

import pytest
from unittest.mock import Mock
from ansible.module_utils.facts.system.distribution import DistributionFiles

# Mock functions to be used in the test
def mock_get_distribution():
    return None

def mock_get_distribution_version():
    return None

def mock_get_distribution_codename():
    return None

@pytest.fixture
def distribution_files(mocker):
    mocker.patch('ansible.module_utils.facts.system.distribution.get_distribution', mock_get_distribution)
    mocker.patch('ansible.module_utils.facts.system.distribution.get_distribution_version', mock_get_distribution_version)
    mocker.patch('ansible.module_utils.facts.system.distribution.get_distribution_codename', mock_get_distribution_codename)
    mock_module = Mock()
    return DistributionFiles(module=mock_module)

def test_guess_distribution_with_na_values(distribution_files):
    expected_distribution_guess = {
        'distribution': 'NA',
        'distribution_version': 'NA',
        'distribution_release': 'NA',
        'distribution_major_version': 'NA'
    }
    distribution_guess = distribution_files._guess_distribution()
    assert distribution_guess == expected_distribution_guess
