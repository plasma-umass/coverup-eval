# file lib/ansible/module_utils/facts/system/distribution.py:408-424
# lines [408, 409, 411, 413, 414, 417, 418, 419, 420, 422, 424]
# branches ['413->414', '413->422', '414->417', '414->418', '419->420', '419->424']

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.system.distribution import DistributionFiles
import re

@pytest.fixture
def mock_get_distribution():
    with patch('ansible.module_utils.facts.system.distribution.get_distribution') as mock:
        yield mock

class MockModule:
    def __init__(self):
        pass

@pytest.fixture
def distribution_files():
    return DistributionFiles(module=MockModule())

def test_parse_distribution_file_Coreos(distribution_files, mock_get_distribution):
    collected_facts = {}

    # Test for distro 'coreos' with empty data
    mock_get_distribution.return_value = 'coreos'
    success, coreos_facts = distribution_files.parse_distribution_file_Coreos('name', '', 'path', collected_facts)
    assert not success
    assert coreos_facts == {}

    # Test for distro 'coreos' with valid data
    data = 'GROUP="2023.3.0"'
    success, coreos_facts = distribution_files.parse_distribution_file_Coreos('name', data, 'path', collected_facts)
    assert success
    assert coreos_facts == {'distribution_release': '2023.3.0'}

    # Test for distro not 'coreos'
    mock_get_distribution.return_value = 'not_coreos'
    success, coreos_facts = distribution_files.parse_distribution_file_Coreos('name', data, 'path', collected_facts)
    assert not success
    assert coreos_facts == {}
