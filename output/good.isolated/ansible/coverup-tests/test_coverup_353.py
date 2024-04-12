# file lib/ansible/module_utils/facts/system/distribution.py:211-219
# lines [211, 212, 213, 214, 215, 216, 217, 218, 219]
# branches ['213->214', '213->215', '217->218', '217->219']

import re
import pytest
from unittest.mock import MagicMock

# Assuming the DistributionFiles class is part of a module named distribution
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def distribution_files(mocker):
    module_mock = MagicMock()
    return DistributionFiles(module=module_mock)

def test_parse_distribution_file_Slackware_found(distribution_files):
    collected_facts = {}
    name = "Slackware"
    data = "Slackware 14.2+"

    found, slackware_facts = distribution_files.parse_distribution_file_Slackware(name, data, '', collected_facts)

    assert found is True
    assert slackware_facts['distribution'] == "Slackware"
    assert slackware_facts['distribution_version'] == "14.2+"

def test_parse_distribution_file_Slackware_not_found(distribution_files):
    collected_facts = {}
    name = "Slackware"
    data = "Some other distro"

    found, slackware_facts = distribution_files.parse_distribution_file_Slackware(name, data, '', collected_facts)

    assert found is False
    assert slackware_facts == {}
