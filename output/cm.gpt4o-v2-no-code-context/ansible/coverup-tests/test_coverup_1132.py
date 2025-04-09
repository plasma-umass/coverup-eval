# file: lib/ansible/module_utils/facts/system/distribution.py:110-145
# asked: {"lines": [111, 112, 113, 116, 118, 119, 122, 124, 126, 127, 128, 129, 130, 134, 136, 137, 138, 139, 140, 141, 143], "branches": [[113, 116], [113, 126], [116, 118], [116, 122], [126, 127], [126, 134], [127, 128], [127, 130]]}
# gained: {"lines": [111, 112, 113, 116, 118, 119, 122, 124, 126, 127, 128, 129, 130, 134, 136, 137, 138, 139, 140, 141, 143], "branches": [[113, 116], [113, 126], [116, 118], [116, 122], [126, 127], [126, 134], [127, 128], [127, 130]]}

import pytest
from ansible.module_utils.facts.system.distribution import DistributionFiles

class TestDistributionFiles:
    @pytest.fixture
    def dist_files(self):
        class MockModule:
            def debug(self, msg):
                pass

        class MockDistributionFiles(DistributionFiles):
            SEARCH_STRING = {'RedHat': 'Red Hat'}
            OS_RELEASE_ALIAS = {'CentOS': 'CentOS Linux'}
            STRIP_QUOTES = '"'

            def __init__(self, module):
                self.module = module

            def parse_distribution_file_test(self, name, dist_file_content, path, collected_facts):
                return True, {'distribution': 'TestDist'}

        return MockDistributionFiles(MockModule())

    def test_parse_dist_file_search_string_match(self, dist_files):
        name = 'RedHat'
        dist_file_content = 'Red Hat Enterprise Linux'
        path = '/etc/redhat-release'
        collected_facts = {}

        parsed, dist_file_dict = dist_files._parse_dist_file(name, dist_file_content, path, collected_facts)
        assert parsed is True
        assert dist_file_dict['distribution'] == 'RedHat'
        assert dist_file_dict['distribution_file_search_string'] == 'Red Hat'

    def test_parse_dist_file_search_string_no_match(self, dist_files):
        name = 'RedHat'
        dist_file_content = 'CentOS Linux'
        path = '/etc/redhat-release'
        collected_facts = {}

        parsed, dist_file_dict = dist_files._parse_dist_file(name, dist_file_content, path, collected_facts)
        assert parsed is True
        assert dist_file_dict['distribution'] == 'CentOS'

    def test_parse_dist_file_os_release_alias_match(self, dist_files):
        name = 'CentOS'
        dist_file_content = 'CentOS Linux release 7.9.2009 (Core)'
        path = '/etc/os-release'
        collected_facts = {}

        parsed, dist_file_dict = dist_files._parse_dist_file(name, dist_file_content, path, collected_facts)
        assert parsed is True
        assert dist_file_dict['distribution'] == 'CentOS'

    def test_parse_dist_file_os_release_alias_no_match(self, dist_files):
        name = 'CentOS'
        dist_file_content = 'Red Hat Enterprise Linux'
        path = '/etc/os-release'
        collected_facts = {}

        parsed, dist_file_dict = dist_files._parse_dist_file(name, dist_file_content, path, collected_facts)
        assert parsed is False
        assert 'distribution' not in dist_file_dict

    def test_parse_dist_file_custom_parser(self, dist_files):
        name = 'test'
        dist_file_content = 'TestDist'
        path = '/etc/test-release'
        collected_facts = {}

        parsed, dist_file_dict = dist_files._parse_dist_file(name, dist_file_content, path, collected_facts)
        assert parsed is True
        assert dist_file_dict['distribution'] == 'TestDist'

    def test_parse_dist_file_custom_parser_not_found(self, dist_files, mocker):
        name = 'nonexistent'
        dist_file_content = 'NonexistentDist'
        path = '/etc/nonexistent-release'
        collected_facts = {}

        mocker.patch.object(dist_files.module, 'debug')

        parsed, dist_file_dict = dist_files._parse_dist_file(name, dist_file_content, path, collected_facts)
        assert parsed is False
        assert 'distribution' not in dist_file_dict
        dist_files.module.debug.assert_called_once()
