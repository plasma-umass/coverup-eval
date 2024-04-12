# file lib/ansible/module_utils/facts/system/distribution.py:259-263
# lines [259, 260, 261, 262, 263]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def mock_module():
    return MagicMock()

def test_parse_distribution_file_Alpine(mock_module):
    distribution_files = DistributionFiles(mock_module)
    name = 'Alpine'
    data = '3.12.0'
    path = '/etc/alpine-release'
    collected_facts = {}

    success, alpine_facts = distribution_files.parse_distribution_file_Alpine(name, data, path, collected_facts)

    assert success is True
    assert alpine_facts['distribution'] == 'Alpine'
    assert alpine_facts['distribution_version'] == data
