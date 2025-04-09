# file lib/ansible/module_utils/facts/system/distribution.py:426-439
# lines [426, 427, 428, 430, 431, 432, 433, 434, 435, 437, 439]
# branches ['430->431', '430->437', '431->432', '431->433', '434->435', '434->439']

import pytest
import re
from unittest.mock import Mock, patch

# Assuming the get_distribution function is part of the same module
from ansible.module_utils.facts.system.distribution import DistributionFiles, get_distribution

@pytest.fixture
def mock_get_distribution(mocker):
    return mocker.patch('ansible.module_utils.facts.system.distribution.get_distribution')

@pytest.fixture
def distribution_files():
    module_mock = Mock()
    return DistributionFiles(module=module_mock)

def test_parse_distribution_file_Flatcar_not_flatcar(mock_get_distribution, distribution_files):
    mock_get_distribution.return_value = 'not_flatcar'
    name = 'some_name'
    data = 'some_data'
    path = 'some_path'
    collected_facts = {}

    success, flatcar_facts = distribution_files.parse_distribution_file_Flatcar(name, data, path, collected_facts)

    assert not success
    assert flatcar_facts == {}

def test_parse_distribution_file_Flatcar_no_data(mock_get_distribution, distribution_files):
    mock_get_distribution.return_value = 'flatcar'
    name = 'some_name'
    data = ''
    path = 'some_path'
    collected_facts = {}

    success, flatcar_facts = distribution_files.parse_distribution_file_Flatcar(name, data, path, collected_facts)

    assert not success
    assert flatcar_facts == {}

def test_parse_distribution_file_Flatcar_with_release(mock_get_distribution, distribution_files):
    mock_get_distribution.return_value = 'flatcar'
    name = 'some_name'
    data = 'GROUP="1.0"'
    path = 'some_path'
    collected_facts = {}

    success, flatcar_facts = distribution_files.parse_distribution_file_Flatcar(name, data, path, collected_facts)

    assert success
    assert flatcar_facts == {'distribution_release': '1.0'}

def test_parse_distribution_file_Flatcar_without_release(mock_get_distribution, distribution_files):
    mock_get_distribution.return_value = 'flatcar'
    name = 'some_name'
    data = 'SOME_OTHER_LINE="value"'
    path = 'some_path'
    collected_facts = {}

    success, flatcar_facts = distribution_files.parse_distribution_file_Flatcar(name, data, path, collected_facts)

    assert success
    assert flatcar_facts == {}
