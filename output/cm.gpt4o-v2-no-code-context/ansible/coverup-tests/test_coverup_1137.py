# file: lib/ansible/module_utils/facts/system/distribution.py:221-244
# asked: {"lines": [222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 235, 237, 238, 240, 241, 242, 244], "branches": [[223, 224], [223, 225], [226, 227], [226, 240], [228, 229], [228, 244], [232, 233], [232, 235]]}
# gained: {"lines": [222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 235, 237, 238, 240, 241, 242, 244], "branches": [[223, 224], [223, 225], [226, 227], [226, 240], [228, 229], [228, 244], [232, 233], [232, 235]]}

import pytest
import re
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def distribution_files(mocker):
    mock_module = mocker.Mock()
    return DistributionFiles(mock_module)

def test_parse_distribution_file_Amazon_no_amazon_in_data(distribution_files):
    name = "test"
    data = "Some random data"
    path = "/etc/os-release"
    collected_facts = {}
    result, facts = distribution_files.parse_distribution_file_Amazon(name, data, path, collected_facts)
    assert result is False
    assert facts == {}

def test_parse_distribution_file_Amazon_with_amazon_in_data(distribution_files):
    name = "test"
    data = "Amazon Linux"
    path = "/etc/os-release"
    collected_facts = {}
    result, facts = distribution_files.parse_distribution_file_Amazon(name, data, path, collected_facts)
    assert result is True
    assert facts['distribution'] == 'Amazon'

def test_parse_distribution_file_Amazon_with_version_id(distribution_files):
    name = "test"
    data = 'Amazon Linux\nVERSION_ID="2.0"'
    path = "/etc/os-release"
    collected_facts = {}
    result, facts = distribution_files.parse_distribution_file_Amazon(name, data, path, collected_facts)
    assert result is True
    assert facts['distribution'] == 'Amazon'
    assert facts['distribution_version'] == '2.0'
    assert facts['distribution_major_version'] == '2'
    assert facts['distribution_minor_version'] == '0'

def test_parse_distribution_file_Amazon_without_version_id(distribution_files):
    name = "test"
    data = 'Amazon Linux'
    path = "/etc/os-release"
    collected_facts = {}
    result, facts = distribution_files.parse_distribution_file_Amazon(name, data, path, collected_facts)
    assert result is True
    assert facts['distribution'] == 'Amazon'
    assert 'distribution_version' not in facts

def test_parse_distribution_file_Amazon_with_version_id_single_value(distribution_files):
    name = "test"
    data = 'Amazon Linux\nVERSION_ID="2"'
    path = "/etc/os-release"
    collected_facts = {}
    result, facts = distribution_files.parse_distribution_file_Amazon(name, data, path, collected_facts)
    assert result is True
    assert facts['distribution'] == 'Amazon'
    assert facts['distribution_version'] == '2'
    assert facts['distribution_major_version'] == '2'
    assert facts['distribution_minor_version'] == 'NA'

def test_parse_distribution_file_Amazon_non_os_release_path(distribution_files):
    name = "test"
    data = 'Amazon Linux 2'
    path = "/etc/other-release"
    collected_facts = {}
    result, facts = distribution_files.parse_distribution_file_Amazon(name, data, path, collected_facts)
    assert result is True
    assert facts['distribution'] == 'Amazon'
    assert facts['distribution_version'] == '2'
