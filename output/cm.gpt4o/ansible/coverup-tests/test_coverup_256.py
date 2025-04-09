# file lib/ansible/module_utils/facts/system/distribution.py:408-424
# lines [408, 409, 411, 413, 414, 417, 418, 419, 420, 422, 424]
# branches ['413->414', '413->422', '414->417', '414->418', '419->420', '419->424']

import pytest
from unittest.mock import patch

# Assuming the DistributionFiles class is imported from the module
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def distribution_files(mocker):
    mocker.patch('ansible.module_utils.facts.system.distribution.get_distribution', return_value='coreos')
    return DistributionFiles(module=None)

def test_parse_distribution_file_Coreos_no_data(distribution_files, mocker):
    mocker.patch('ansible.module_utils.facts.system.distribution.get_distribution', return_value='coreos')
    name = "test_name"
    data = ""
    path = "test_path"
    collected_facts = {}

    result, facts = distribution_files.parse_distribution_file_Coreos(name, data, path, collected_facts)
    
    assert result is False
    assert facts == {}

def test_parse_distribution_file_Coreos_with_data(distribution_files, mocker):
    mocker.patch('ansible.module_utils.facts.system.distribution.get_distribution', return_value='coreos')
    name = "test_name"
    data = 'GROUP="test_release"'
    path = "test_path"
    collected_facts = {}

    result, facts = distribution_files.parse_distribution_file_Coreos(name, data, path, collected_facts)
    
    assert result is True
    assert facts == {'distribution_release': 'test_release'}

def test_parse_distribution_file_non_Coreos(distribution_files, mocker):
    mocker.patch('ansible.module_utils.facts.system.distribution.get_distribution', return_value='not_coreos')
    name = "test_name"
    data = 'GROUP="test_release"'
    path = "test_path"
    collected_facts = {}

    result, facts = distribution_files.parse_distribution_file_Coreos(name, data, path, collected_facts)
    
    assert result is False
    assert facts == {}
