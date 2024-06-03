# file lib/ansible/module_utils/facts/system/distribution.py:408-424
# lines []
# branches ['419->424']

import pytest
from unittest import mock
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def mock_get_distribution(mocker):
    return mocker.patch('ansible.module_utils.facts.system.distribution.get_distribution')

@pytest.fixture
def dist_files(mocker):
    module_mock = mocker.Mock()
    return DistributionFiles(module_mock)

def test_parse_distribution_file_Coreos_no_release(mock_get_distribution, dist_files):
    mock_get_distribution.return_value = 'coreos'
    name = 'some_name'
    data = 'SOME_OTHER_DATA=some_value'
    path = 'some_path'
    collected_facts = {}

    result, facts = dist_files.parse_distribution_file_Coreos(name, data, path, collected_facts)

    assert result is True
    assert 'distribution_release' not in facts

def test_parse_distribution_file_Coreos_with_release(mock_get_distribution, dist_files):
    mock_get_distribution.return_value = 'coreos'
    name = 'some_name'
    data = 'GROUP="stable"'
    path = 'some_path'
    collected_facts = {}

    result, facts = dist_files.parse_distribution_file_Coreos(name, data, path, collected_facts)

    assert result is True
    assert facts['distribution_release'] == 'stable'

def test_parse_distribution_file_not_Coreos(mock_get_distribution, dist_files):
    mock_get_distribution.return_value = 'not_coreos'
    name = 'some_name'
    data = 'GROUP="stable"'
    path = 'some_path'
    collected_facts = {}

    result, facts = dist_files.parse_distribution_file_Coreos(name, data, path, collected_facts)

    assert result is False
    assert facts == {}
