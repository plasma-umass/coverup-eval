# file lib/ansible/module_utils/facts/system/distribution.py:381-395
# lines []
# branches ['386->388', '389->391']

import re
import pytest
from unittest.mock import Mock

# Assuming the DistributionFiles class is part of a module named distribution
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def mock_collected_facts():
    return {}

@pytest.fixture
def distribution_files():
    mock_module = Mock()
    return DistributionFiles(mock_module)

def test_parse_distribution_file_Mandriva_with_version_and_release(distribution_files, mock_collected_facts):
    name = "Mandriva"
    data_with_version_and_release = """
    Mandriva
    DISTRIB_RELEASE="2021"
    DISTRIB_CODENAME="Final"
    """
    path = "/etc/mandriva-release"

    success, mandriva_facts = distribution_files.parse_distribution_file_Mandriva(name, data_with_version_and_release, path, mock_collected_facts)

    assert success is True
    assert mandriva_facts['distribution'] == name
    assert mandriva_facts['distribution_version'] == "2021"
    assert mandriva_facts['distribution_release'] == "Final"

def test_parse_distribution_file_Mandriva_without_version_and_release(distribution_files, mock_collected_facts):
    name = "Mandriva"
    data_without_version_and_release = "Mandriva"
    path = "/etc/mandriva-release"

    success, mandriva_facts = distribution_files.parse_distribution_file_Mandriva(name, data_without_version_and_release, path, mock_collected_facts)

    assert success is True
    assert mandriva_facts['distribution'] == name
    assert 'distribution_version' not in mandriva_facts
    assert 'distribution_release' not in mandriva_facts
