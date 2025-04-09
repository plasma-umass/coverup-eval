# file: lib/ansible/module_utils/facts/system/distribution.py:397-406
# asked: {"lines": [397, 398, 399, 400, 401, 402, 403, 404, 405, 406], "branches": [[399, 400], [399, 406], [401, 402], [401, 403], [404, 399], [404, 405]]}
# gained: {"lines": [397, 398, 399, 400, 401, 402, 403, 404, 405, 406], "branches": [[399, 400], [399, 406], [401, 402], [401, 403], [404, 399], [404, 405]]}

import pytest
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def distribution_files(mocker):
    mock_module = mocker.Mock()
    return DistributionFiles(mock_module)

def test_parse_distribution_file_NA_name_match(distribution_files):
    name = 'NA'
    data = 'NAME="TestDistribution"\nVERSION="1.0"'
    path = '/fake/path'
    collected_facts = {'distribution_version': 'NA'}
    
    result, na_facts = distribution_files.parse_distribution_file_NA(name, data, path, collected_facts)
    
    assert result is True
    assert na_facts['distribution'] == 'TestDistribution'
    assert na_facts['distribution_version'] == '1.0'

def test_parse_distribution_file_NA_name_no_match(distribution_files):
    name = 'NotNA'
    data = 'NAME="TestDistribution"\nVERSION="1.0"'
    path = '/fake/path'
    collected_facts = {'distribution_version': 'NA'}
    
    result, na_facts = distribution_files.parse_distribution_file_NA(name, data, path, collected_facts)
    
    assert result is True
    assert 'distribution' not in na_facts
    assert na_facts['distribution_version'] == '1.0'

def test_parse_distribution_file_NA_version_no_match(distribution_files):
    name = 'NA'
    data = 'NAME="TestDistribution"\nVERSION="1.0"'
    path = '/fake/path'
    collected_facts = {'distribution_version': 'NotNA'}
    
    result, na_facts = distribution_files.parse_distribution_file_NA(name, data, path, collected_facts)
    
    assert result is True
    assert na_facts['distribution'] == 'TestDistribution'
    assert 'distribution_version' not in na_facts

def test_parse_distribution_file_NA_no_matches(distribution_files):
    name = 'NotNA'
    data = 'NAME="TestDistribution"\nVERSION="1.0"'
    path = '/fake/path'
    collected_facts = {'distribution_version': 'NotNA'}
    
    result, na_facts = distribution_files.parse_distribution_file_NA(name, data, path, collected_facts)
    
    assert result is True
    assert 'distribution' not in na_facts
    assert 'distribution_version' not in na_facts
