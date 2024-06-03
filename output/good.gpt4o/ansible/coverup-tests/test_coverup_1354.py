# file lib/ansible/module_utils/facts/system/distribution.py:211-219
# lines []
# branches ['217->219']

import pytest
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def distribution_files(mocker):
    module_mock = mocker.Mock()
    return DistributionFiles(module=module_mock)

def test_parse_distribution_file_Slackware_with_version(distribution_files):
    name = "Slackware"
    data = "Slackware 14.2+"
    path = "/etc/slackware-version"
    collected_facts = {}

    result, facts = distribution_files.parse_distribution_file_Slackware(name, data, path, collected_facts)

    assert result is True
    assert 'distribution' in facts
    assert facts['distribution'] == name
    assert 'distribution_version' in facts
    assert facts['distribution_version'] == "14.2+"

def test_parse_distribution_file_Slackware_without_version(distribution_files):
    name = "Slackware"
    data = "Slackware"
    path = "/etc/slackware-version"
    collected_facts = {}

    result, facts = distribution_files.parse_distribution_file_Slackware(name, data, path, collected_facts)

    assert result is True
    assert 'distribution' in facts
    assert facts['distribution'] == name
    assert 'distribution_version' not in facts
