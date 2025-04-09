# file: lib/ansible/module_utils/facts/system/distribution.py:110-145
# asked: {"lines": [110, 111, 112, 113, 116, 118, 119, 122, 124, 126, 127, 128, 129, 130, 134, 136, 137, 138, 139, 140, 141, 143], "branches": [[113, 116], [113, 126], [116, 118], [116, 122], [126, 127], [126, 134], [127, 128], [127, 130]]}
# gained: {"lines": [110, 111, 112, 113, 116, 118, 119, 122, 124, 126, 127, 128, 129, 130, 134, 136, 137, 138, 139, 140, 141, 143], "branches": [[113, 116], [113, 126], [116, 118], [116, 122], [126, 127], [126, 134], [127, 128], [127, 130]]}

import pytest
from unittest.mock import Mock

class TestDistributionFiles:
    @pytest.fixture
    def distribution_files(self):
        from ansible.module_utils.facts.system.distribution import DistributionFiles
        module = Mock()
        return DistributionFiles(module)

    def test_parse_dist_file_search_string_match(self, distribution_files):
        name = 'RedHat'
        dist_file_content = 'Red Hat Enterprise Linux'
        path = '/etc/redhat-release'
        collected_facts = {}

        parsed, dist_file_dict = distribution_files._parse_dist_file(name, dist_file_content, path, collected_facts)

        assert parsed is True
        assert dist_file_dict['distribution'] == name
        assert dist_file_dict['distribution_file_search_string'] == 'Red Hat'

    def test_parse_dist_file_search_string_no_match(self, distribution_files):
        name = 'RedHat'
        dist_file_content = 'CentOS Linux'
        path = '/etc/redhat-release'
        collected_facts = {}

        parsed, dist_file_dict = distribution_files._parse_dist_file(name, dist_file_content, path, collected_facts)

        assert parsed is True
        assert dist_file_dict['distribution'] == 'CentOS'

    def test_parse_dist_file_os_release_alias_match(self, distribution_files):
        name = 'Archlinux'
        dist_file_content = 'Arch Linux'
        path = '/etc/arch-release'
        collected_facts = {}

        parsed, dist_file_dict = distribution_files._parse_dist_file(name, dist_file_content, path, collected_facts)

        assert parsed is True
        assert dist_file_dict['distribution'] == name

    def test_parse_dist_file_os_release_alias_no_match(self, distribution_files):
        name = 'Archlinux'
        dist_file_content = 'Some Other Linux'
        path = '/etc/arch-release'
        collected_facts = {}

        parsed, dist_file_dict = distribution_files._parse_dist_file(name, dist_file_content, path, collected_facts)

        assert parsed is False
        assert 'distribution' not in dist_file_dict

    def test_parse_dist_file_custom_parser(self, distribution_files, monkeypatch):
        name = 'Slackware'
        dist_file_content = 'Slackware Linux'
        path = '/etc/slackware-version'
        collected_facts = {}

        def mock_parse_distribution_file_Slackware(name, data, path, collected_facts):
            return True, {'distribution': 'Slackware'}

        monkeypatch.setattr(distribution_files, 'parse_distribution_file_Slackware', mock_parse_distribution_file_Slackware)

        parsed, dist_file_dict = distribution_files._parse_dist_file(name, dist_file_content, path, collected_facts)

        assert parsed is True
        assert dist_file_dict['distribution'] == 'Slackware'

    def test_parse_dist_file_attribute_error(self, distribution_files):
        name = 'NonExistent'
        dist_file_content = 'NonExistent Linux'
        path = '/etc/nonexistent-release'
        collected_facts = {}

        parsed, dist_file_dict = distribution_files._parse_dist_file(name, dist_file_content, path, collected_facts)

        assert parsed is False
        assert 'distribution' not in dist_file_dict
