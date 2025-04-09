# file: lib/ansible/module_utils/facts/system/distribution.py:259-263
# asked: {"lines": [259, 260, 261, 262, 263], "branches": []}
# gained: {"lines": [259, 260, 261, 262, 263], "branches": []}

import pytest
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def distribution_files():
    class MockModule:
        pass

    return DistributionFiles(MockModule())

def test_parse_distribution_file_Alpine(distribution_files):
    name = "Alpine"
    data = "3.14.0"
    path = "/etc/alpine-release"
    collected_facts = {}

    result, facts = distribution_files.parse_distribution_file_Alpine(name, data, path, collected_facts)

    assert result is True
    assert facts['distribution'] == 'Alpine'
    assert facts['distribution_version'] == data
