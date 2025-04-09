# file lib/ansible/module_utils/facts/system/distribution.py:381-395
# lines []
# branches ['386->388', '389->391']

import pytest
from ansible.module_utils.facts.system.distribution import DistributionFiles

class MockModule:
    def __init__(self):
        self.params = {}

@pytest.fixture
def mock_module():
    return MockModule()

def test_parse_distribution_file_Mandriva_version_and_release(mock_module):
    df = DistributionFiles(mock_module)
    name = "Mandriva"
    data = 'Mandriva\nDISTRIB_RELEASE="2021.1"\nDISTRIB_CODENAME="Mandrake"'
    path = "/etc/mandriva-release"
    collected_facts = {}

    result, facts = df.parse_distribution_file_Mandriva(name, data, path, collected_facts)

    assert result is True
    assert facts['distribution'] == 'Mandriva'
    assert facts['distribution_version'] == '2021.1'
    assert facts['distribution_release'] == 'Mandrake'

def test_parse_distribution_file_Mandriva_no_version(mock_module):
    df = DistributionFiles(mock_module)
    name = "Mandriva"
    data = 'Mandriva\nDISTRIB_CODENAME="Mandrake"'
    path = "/etc/mandriva-release"
    collected_facts = {}

    result, facts = df.parse_distribution_file_Mandriva(name, data, path, collected_facts)

    assert result is True
    assert facts['distribution'] == 'Mandriva'
    assert 'distribution_version' not in facts
    assert facts['distribution_release'] == 'Mandrake'

def test_parse_distribution_file_Mandriva_no_release(mock_module):
    df = DistributionFiles(mock_module)
    name = "Mandriva"
    data = 'Mandriva\nDISTRIB_RELEASE="2021.1"'
    path = "/etc/mandriva-release"
    collected_facts = {}

    result, facts = df.parse_distribution_file_Mandriva(name, data, path, collected_facts)

    assert result is True
    assert facts['distribution'] == 'Mandriva'
    assert facts['distribution_version'] == '2021.1'
    assert 'distribution_release' not in facts

def test_parse_distribution_file_Mandriva_no_version_no_release(mock_module):
    df = DistributionFiles(mock_module)
    name = "Mandriva"
    data = 'Mandriva'
    path = "/etc/mandriva-release"
    collected_facts = {}

    result, facts = df.parse_distribution_file_Mandriva(name, data, path, collected_facts)

    assert result is True
    assert facts['distribution'] == 'Mandriva'
    assert 'distribution_version' not in facts
    assert 'distribution_release' not in facts
