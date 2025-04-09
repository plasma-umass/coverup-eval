# file: lib/ansible/module_utils/facts/system/distribution.py:211-219
# asked: {"lines": [211, 212, 213, 214, 215, 216, 217, 218, 219], "branches": [[213, 214], [213, 215], [217, 218], [217, 219]]}
# gained: {"lines": [211, 212, 213, 214, 215, 216, 217, 218, 219], "branches": [[213, 214], [213, 215], [217, 218], [217, 219]]}

import pytest
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def distribution_files():
    return DistributionFiles(module=None)

def test_parse_distribution_file_Slackware_no_slackware(distribution_files):
    name = "Slackware"
    data = "Some random data"
    path = "/etc/slackware-version"
    collected_facts = {}

    result, facts = distribution_files.parse_distribution_file_Slackware(name, data, path, collected_facts)

    assert result is False
    assert facts == {}

def test_parse_distribution_file_Slackware_with_slackware(distribution_files):
    name = "Slackware"
    data = "Slackware 14.2+"
    path = "/etc/slackware-version"
    collected_facts = {}

    result, facts = distribution_files.parse_distribution_file_Slackware(name, data, path, collected_facts)

    assert result is True
    assert facts['distribution'] == name
    assert facts['distribution_version'] == "14.2+"

def test_parse_distribution_file_Slackware_with_slackware_no_version(distribution_files):
    name = "Slackware"
    data = "Slackware"
    path = "/etc/slackware-version"
    collected_facts = {}

    result, facts = distribution_files.parse_distribution_file_Slackware(name, data, path, collected_facts)

    assert result is True
    assert facts['distribution'] == name
    assert 'distribution_version' not in facts
