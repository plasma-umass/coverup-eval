# file: lib/ansible/module_utils/facts/system/distribution.py:221-244
# asked: {"lines": [235], "branches": [[232, 235]]}
# gained: {"lines": [235], "branches": [[232, 235]]}

import pytest
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def distribution_files():
    return DistributionFiles(None)

def test_parse_distribution_file_Amazon_no_amazon(distribution_files):
    name = "Amazon"
    data = "Some random data"
    path = "/etc/os-release"
    collected_facts = {}
    
    result, facts = distribution_files.parse_distribution_file_Amazon(name, data, path, collected_facts)
    
    assert result is False
    assert facts == {}

def test_parse_distribution_file_Amazon_with_amazon_os_release(distribution_files):
    name = "Amazon"
    data = 'NAME="Amazon Linux"\nVERSION_ID="2.0"'
    path = "/etc/os-release"
    collected_facts = {}
    
    result, facts = distribution_files.parse_distribution_file_Amazon(name, data, path, collected_facts)
    
    assert result is True
    assert facts['distribution'] == 'Amazon'
    assert facts['distribution_version'] == '2.0'
    assert facts['distribution_major_version'] == '2'
    assert facts['distribution_minor_version'] == '0'

def test_parse_distribution_file_Amazon_with_amazon_os_release_no_minor(distribution_files):
    name = "Amazon"
    data = 'NAME="Amazon Linux"\nVERSION_ID="2"'
    path = "/etc/os-release"
    collected_facts = {}
    
    result, facts = distribution_files.parse_distribution_file_Amazon(name, data, path, collected_facts)
    
    assert result is True
    assert facts['distribution'] == 'Amazon'
    assert facts['distribution_version'] == '2'
    assert facts['distribution_major_version'] == '2'
    assert facts['distribution_minor_version'] == 'NA'

def test_parse_distribution_file_Amazon_with_amazon_other_path(distribution_files):
    name = "Amazon"
    data = 'Amazon Linux release 2'
    path = "/etc/system-release"
    collected_facts = {}
    
    result, facts = distribution_files.parse_distribution_file_Amazon(name, data, path, collected_facts)
    
    assert result is True
    assert facts['distribution'] == 'Amazon'
    assert facts['distribution_version'] == '2'
