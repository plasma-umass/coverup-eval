# file lib/ansible/module_utils/facts/system/distribution.py:460-467
# lines [460, 461, 463, 464, 465, 467]
# branches ['463->464', '463->467']

import pytest
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def distribution_files(mocker):
    mock_module = mocker.Mock()
    return DistributionFiles(mock_module)

def test_parse_distribution_file_CentOS_stream(distribution_files):
    name = "CentOS"
    data = "CentOS Stream release 8"
    path = "/etc/centos-release"
    collected_facts = {}

    result, facts = distribution_files.parse_distribution_file_CentOS(name, data, path, collected_facts)

    assert result is True
    assert facts == {'distribution_release': 'Stream'}

def test_parse_distribution_file_CentOS_non_stream(distribution_files):
    name = "CentOS"
    data = "CentOS Linux release 7.9.2009 (Core)"
    path = "/etc/centos-release"
    collected_facts = {}

    result, facts = distribution_files.parse_distribution_file_CentOS(name, data, path, collected_facts)

    assert result is False
    assert facts == {}
