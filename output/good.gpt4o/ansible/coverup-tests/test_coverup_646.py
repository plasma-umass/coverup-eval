# file lib/ansible/module_utils/facts/system/distribution.py:259-263
# lines [259, 260, 261, 262, 263]
# branches []

import pytest
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def distribution_files(mocker):
    mock_module = mocker.Mock()
    return DistributionFiles(mock_module)

def test_parse_distribution_file_Alpine(distribution_files):
    name = "alpine-release"
    data = "3.12.1"
    path = "/etc/alpine-release"
    collected_facts = {}

    result, facts = distribution_files.parse_distribution_file_Alpine(name, data, path, collected_facts)

    assert result is True
    assert facts['distribution'] == 'Alpine'
    assert facts['distribution_version'] == data
