# file: lib/ansible/module_utils/facts/system/distribution.py:221-244
# asked: {"lines": [221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 235, 237, 238, 240, 241, 242, 244], "branches": [[223, 224], [223, 225], [226, 227], [226, 240], [228, 229], [228, 244], [232, 233], [232, 235]]}
# gained: {"lines": [221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 237, 238, 240, 241, 242, 244], "branches": [[223, 224], [223, 225], [226, 227], [226, 240], [228, 229], [228, 244], [232, 233]]}

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
    
    assert result == False
    assert facts == {}

def test_parse_distribution_file_Amazon_os_release_with_version(distribution_files):
    name = "Amazon"
    data = 'NAME="Amazon Linux AMI"\nVERSION_ID="2018.03"'
    path = "/etc/os-release"
    collected_facts = {}
    
    result, facts = distribution_files.parse_distribution_file_Amazon(name, data, path, collected_facts)
    
    assert result == True
    assert facts['distribution'] == 'Amazon'
    assert facts['distribution_version'] == '2018.03'
    assert facts['distribution_major_version'] == '2018'
    assert facts['distribution_minor_version'] == '03'

def test_parse_distribution_file_Amazon_os_release_without_version(distribution_files):
    name = "Amazon"
    data = 'NAME="Amazon Linux AMI"'
    path = "/etc/os-release"
    collected_facts = {}
    
    result, facts = distribution_files.parse_distribution_file_Amazon(name, data, path, collected_facts)
    
    assert result == True
    assert facts['distribution'] == 'Amazon'
    assert 'distribution_version' not in facts
    assert 'distribution_major_version' not in facts
    assert 'distribution_minor_version' not in facts

def test_parse_distribution_file_Amazon_other_path_with_version(distribution_files):
    name = "Amazon"
    data = "Amazon Linux AMI release 2018"
    path = "/etc/system-release"
    collected_facts = {}
    
    result, facts = distribution_files.parse_distribution_file_Amazon(name, data, path, collected_facts)
    
    assert result == True
    assert facts['distribution'] == 'Amazon'
    assert facts['distribution_version'] == '2018'

def test_parse_distribution_file_Amazon_other_path_without_version(distribution_files):
    name = "Amazon"
    data = "Amazon Linux AMI release"
    path = "/etc/system-release"
    collected_facts = {}
    
    result, facts = distribution_files.parse_distribution_file_Amazon(name, data, path, collected_facts)
    
    assert result == True
    assert facts['distribution'] == 'Amazon'
    assert facts['distribution_version'] == 'NA'
