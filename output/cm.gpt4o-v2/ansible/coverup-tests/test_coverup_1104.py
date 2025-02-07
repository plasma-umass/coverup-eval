# file: lib/ansible/module_utils/facts/system/distribution.py:110-145
# asked: {"lines": [111, 112, 113, 116, 118, 119, 122, 124, 126, 127, 128, 129, 130, 134, 136, 137, 138, 139, 140, 141, 143], "branches": [[113, 116], [113, 126], [116, 118], [116, 122], [126, 127], [126, 134], [127, 128], [127, 130]]}
# gained: {"lines": [111, 112, 113, 116, 118, 119, 122, 124, 126, 127, 128, 129, 130, 134, 136, 137, 138, 139, 140, 141, 143], "branches": [[113, 116], [113, 126], [116, 118], [116, 122], [126, 127], [126, 134], [127, 128], [127, 130]]}

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
    path = '/etc/os-release'
    collected_facts = {}

    result, dist_file_dict = distribution_files._parse_dist_file(name, dist_file_content, path, collected_facts)

    assert result is True
    assert dist_file_dict['distribution'] == 'Archlinux'

def test_parse_dist_file_os_release_alias_no_match(distribution_files):
    name = 'Archlinux'
    dist_file_content = 'Some Other Linux'
    path = '/etc/os-release'
    collected_facts = {}

    result, dist_file_dict = distribution_files._parse_dist_file(name, dist_file_content, path, collected_facts)

    assert result is False
    assert 'distribution' not in dist_file_dict

def test_parse_dist_file_with_distfunc(distribution_files):
    name = 'Debian'
    dist_file_content = 'Debian GNU/Linux'
    path = '/etc/debian_version'
    collected_facts = {}

    with patch.object(distribution_files, 'parse_distribution_file_Debian', return_value=(True, {'distribution': 'Debian'})) as mock_method:
        result, dist_file_dict = distribution_files._parse_dist_file(name, dist_file_content, path, collected_facts)

    mock_method.assert_called_once_with(name, dist_file_content, path, collected_facts)
    assert result is True
    assert dist_file_dict['distribution'] == 'Debian'

def test_parse_dist_file_with_distfunc_attribute_error(distribution_files):
    name = 'NonExistentDistro'
    dist_file_content = 'Non Existent Linux'
    path = '/etc/nonexistent-release'
    collected_facts = {}

    result, dist_file_dict = distribution_files._parse_dist_file(name, dist_file_content, path, collected_facts)

    assert result is False
    assert 'distribution' not in dist_file_dict
