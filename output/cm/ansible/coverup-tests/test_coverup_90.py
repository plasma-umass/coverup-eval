# file lib/ansible/module_utils/facts/system/distribution.py:110-145
# lines [110, 111, 112, 113, 116, 118, 119, 122, 124, 126, 127, 128, 129, 130, 134, 136, 137, 138, 139, 140, 141, 143]
# branches ['113->116', '113->126', '116->118', '116->122', '126->127', '126->134', '127->128', '127->130']

import pytest
from unittest.mock import MagicMock

# Assuming the DistributionFiles class is part of a module named distribution
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def distribution_files():
    module_mock = MagicMock()
    df = DistributionFiles(module=module_mock)
    df.SEARCH_STRING = {'RedHat': 'Red Hat'}
    df.OS_RELEASE_ALIAS = {'CentOS': 'CentOS Linux'}
    return df

def test_parse_dist_file_search_string(distribution_files):
    name = 'RedHat'
    dist_file_content = 'Red Hat Enterprise Linux Server release 7.5 (Maipo)'
    path = '/etc/redhat-release'
    collected_facts = {}

    parsed, dist_file_dict = distribution_files._parse_dist_file(name, dist_file_content, path, collected_facts)

    assert parsed is True
    assert dist_file_dict['distribution'] == name
    assert dist_file_dict['distribution_file_search_string'] == distribution_files.SEARCH_STRING[name]

def test_parse_dist_file_no_search_string(distribution_files):
    name = 'RedHat'
    dist_file_content = 'CentOS Linux release 7.5.1804 (Core)'
    path = '/etc/redhat-release'
    collected_facts = {}

    parsed, dist_file_dict = distribution_files._parse_dist_file(name, dist_file_content, path, collected_facts)

    assert parsed is True
    assert dist_file_dict['distribution'] == 'CentOS'

def test_parse_dist_file_os_release_alias(distribution_files):
    name = 'CentOS'
    dist_file_content = 'CentOS Linux release 7.5.1804 (Core)'
    path = '/etc/os-release'
    collected_facts = {}

    parsed, dist_file_dict = distribution_files._parse_dist_file(name, dist_file_content, path, collected_facts)

    assert parsed is True
    assert dist_file_dict['distribution'] == name

def test_parse_dist_file_no_os_release_alias(distribution_files):
    name = 'CentOS'
    dist_file_content = 'Red Hat Enterprise Linux Server release 7.5 (Maipo)'
    path = '/etc/os-release'
    collected_facts = {}

    parsed, dist_file_dict = distribution_files._parse_dist_file(name, dist_file_content, path, collected_facts)

    assert parsed is False
    assert dist_file_dict == {}

def test_parse_dist_file_attribute_error(distribution_files):
    name = 'NonExistent'
    dist_file_content = 'Some content'
    path = '/etc/nonexistent-release'
    collected_facts = {}

    parsed, dist_file_dict = distribution_files._parse_dist_file(name, dist_file_content, path, collected_facts)

    assert parsed is False
    assert dist_file_dict == {}
    distribution_files.module.debug.assert_called_once()
