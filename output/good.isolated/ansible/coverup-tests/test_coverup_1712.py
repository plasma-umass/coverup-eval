# file lib/ansible/module_utils/facts/system/distribution.py:408-424
# lines []
# branches ['419->424']

import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils.facts.system.distribution import DistributionFiles, get_distribution
import re

@pytest.fixture
def mock_get_distribution():
    with patch('ansible.module_utils.facts.system.distribution.get_distribution') as mock:
        yield mock

class MockModule:
    def __init__(self):
        pass

def test_parse_distribution_file_Coreos_no_release(mock_get_distribution):
    mock_get_distribution.return_value = 'coreos'
    module = MockModule()
    distribution_files = DistributionFiles(module)
    data_without_release = "SOME_VAR=\"value\""
    path = "/fake/path"
    collected_facts = {}

    success, coreos_facts = distribution_files.parse_distribution_file_Coreos('coreos', data_without_release, path, collected_facts)

    assert success is True
    assert 'distribution_release' not in coreos_facts
    mock_get_distribution.assert_called_once()
