# file lib/ansible/module_utils/facts/system/distribution.py:426-439
# lines [426, 427, 428, 430, 431, 432, 433, 434, 435, 437, 439]
# branches ['430->431', '430->437', '431->432', '431->433', '434->435', '434->439']

import pytest
from unittest.mock import patch, MagicMock
import re

# Assuming the DistributionFiles class is imported from the module
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def distribution_files():
    module_mock = MagicMock()
    return DistributionFiles(module_mock)

@patch('ansible.module_utils.facts.system.distribution.get_distribution')
def test_parse_distribution_file_Flatcar_no_data(mock_get_distribution, distribution_files):
    mock_get_distribution.return_value = 'Flatcar'
    name = 'Flatcar'
    data = ''
    path = '/etc/os-release'
    collected_facts = {}

    result, facts = distribution_files.parse_distribution_file_Flatcar(name, data, path, collected_facts)

    assert result is False
    assert facts == {}

@patch('ansible.module_utils.facts.system.distribution.get_distribution')
def test_parse_distribution_file_Flatcar_with_data(mock_get_distribution, distribution_files):
    mock_get_distribution.return_value = 'Flatcar'
    name = 'Flatcar'
    data = 'GROUP="stable"'
    path = '/etc/os-release'
    collected_facts = {}

    result, facts = distribution_files.parse_distribution_file_Flatcar(name, data, path, collected_facts)

    assert result is True
    assert facts == {'distribution_release': 'stable'}

@patch('ansible.module_utils.facts.system.distribution.get_distribution')
def test_parse_distribution_file_non_Flatcar(mock_get_distribution, distribution_files):
    mock_get_distribution.return_value = 'Ubuntu'
    name = 'Flatcar'
    data = 'GROUP="stable"'
    path = '/etc/os-release'
    collected_facts = {}

    result, facts = distribution_files.parse_distribution_file_Flatcar(name, data, path, collected_facts)

    assert result is False
    assert facts == {}
