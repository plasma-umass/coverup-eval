# file lib/ansible/module_utils/facts/system/distribution.py:110-145
# lines [111, 112, 113, 116, 118, 119, 122, 124, 126, 127, 128, 129, 130, 134, 136, 137, 138, 139, 140, 141, 143]
# branches ['113->116', '113->126', '116->118', '116->122', '126->127', '126->134', '127->128', '127->130']

import pytest
from unittest.mock import patch, MagicMock

# Assuming the DistributionFiles class is imported from ansible.module_utils.facts.system.distribution
from ansible.module_utils.facts.system.distribution import DistributionFiles

class TestDistributionFiles:
    @pytest.fixture
    def dist_files(self):
        class MockDistributionFiles(DistributionFiles):
            SEARCH_STRING = {'RedHat': 'Red Hat'}
            OS_RELEASE_ALIAS = {'CentOS': 'CentOS Linux'}
            STRIP_QUOTES = '"'

            def parse_distribution_file_test(self, name, dist_file_content, path, collected_facts):
                return True, {'distribution': 'TestDist'}

        return MockDistributionFiles(module=MagicMock())

    def test_parse_dist_file_search_string(self, dist_files):
        name = 'RedHat'
        dist_file_content = 'Red Hat Enterprise Linux'
        path = '/etc/redhat-release'
        collected_facts = {}

        parsed, dist_file_dict = dist_files._parse_dist_file(name, dist_file_content, path, collected_facts)
        assert parsed is True
        assert dist_file_dict['distribution'] == 'RedHat'
        assert dist_file_dict['distribution_file_search_string'] == 'Red Hat'

    def test_parse_dist_file_os_release_alias(self, dist_files):
        name = 'CentOS'
        dist_file_content = 'CentOS Linux release 7.9.2009 (Core)'
        path = '/etc/centos-release'
        collected_facts = {}

        parsed, dist_file_dict = dist_files._parse_dist_file(name, dist_file_content, path, collected_facts)
        assert parsed is True
        assert dist_file_dict['distribution'] == 'CentOS'

    def test_parse_dist_file_custom_parser(self, dist_files):
        name = 'test'
        dist_file_content = 'TestDist release 1.0'
        path = '/etc/test-release'
        collected_facts = {}

        parsed, dist_file_dict = dist_files._parse_dist_file(name, dist_file_content, path, collected_facts)
        assert parsed is True
        assert dist_file_dict['distribution'] == 'TestDist'

    def test_parse_dist_file_attribute_error(self, dist_files, mocker):
        name = 'NonExistent'
        dist_file_content = 'NonExistent release 1.0'
        path = '/etc/nonexistent-release'
        collected_facts = {}

        mocker.patch.object(dist_files, 'module', MagicMock())
        parsed, dist_file_dict = dist_files._parse_dist_file(name, dist_file_content, path, collected_facts)
        assert parsed is False
        assert dist_file_dict == {}
