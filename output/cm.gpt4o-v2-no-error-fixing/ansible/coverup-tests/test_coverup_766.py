# file: lib/ansible/module_utils/facts/system/distribution.py:110-145
# asked: {"lines": [116, 118, 119, 122, 124, 128, 129, 140, 141, 143], "branches": [[113, 116], [116, 118], [116, 122], [127, 128]]}
# gained: {"lines": [116, 118, 119, 122, 124, 128, 129, 140, 141, 143], "branches": [[113, 116], [116, 118], [116, 122], [127, 128]]}

import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def distribution_files():
    module = Mock()
    return DistributionFiles(module)

def test_parse_dist_file_search_string_match(distribution_files):
    name = 'RedHat'
    dist_file_content = 'Red Hat Enterprise Linux'
    path = '/etc/redhat-release'
    collected_facts = {}

    result, dist_file_dict = distribution_files._parse_dist_file(name, dist_file_content, path, collected_facts)

    assert result is True
    assert dist_file_dict['distribution'] == 'RedHat'
    assert dist_file_dict['distribution_file_search_string'] == 'Red Hat'

def test_parse_dist_file_search_string_no_match(distribution_files):
    name = 'RedHat'
    dist_file_content = 'CentOS Linux'
    path = '/etc/redhat-release'
    collected_facts = {}

    result, dist_file_dict = distribution_files._parse_dist_file(name, dist_file_content, path, collected_facts)

    assert result is True
    assert dist_file_dict['distribution'] == 'CentOS'

def test_parse_dist_file_os_release_alias_match(distribution_files):
    name = 'Archlinux'
    dist_file_content = 'Arch Linux'
    path = '/etc/arch-release'
    collected_facts = {}

    result, dist_file_dict = distribution_files._parse_dist_file(name, dist_file_content, path, collected_facts)

    assert result is True
    assert dist_file_dict['distribution'] == 'Archlinux'

def test_parse_dist_file_os_release_alias_no_match(distribution_files):
    name = 'Archlinux'
    dist_file_content = 'Some Other Linux'
    path = '/etc/arch-release'
    collected_facts = {}

    result, dist_file_dict = distribution_files._parse_dist_file(name, dist_file_content, path, collected_facts)

    assert result is False

@patch.object(DistributionFiles, 'parse_distribution_file_Slackware')
def test_parse_dist_file_custom_parser(mock_parser, distribution_files):
    name = 'Slackware'
    dist_file_content = 'Slackware Linux'
    path = '/etc/slackware-version'
    collected_facts = {}
    mock_parser.return_value = (True, {'distribution': 'Slackware'})

    result, dist_file_dict = distribution_files._parse_dist_file(name, dist_file_content, path, collected_facts)

    assert result is True
    assert dist_file_dict['distribution'] == 'Slackware'
    mock_parser.assert_called_once_with(name, dist_file_content, path, collected_facts)

def test_parse_dist_file_attribute_error(distribution_files):
    name = 'NonExistent'
    dist_file_content = 'Non Existent Linux'
    path = '/etc/nonexistent-release'
    collected_facts = {}

    with patch.object(distribution_files.module, 'debug') as mock_debug:
        result, dist_file_dict = distribution_files._parse_dist_file(name, dist_file_content, path, collected_facts)

    assert result is False
    mock_debug.assert_called_once()
