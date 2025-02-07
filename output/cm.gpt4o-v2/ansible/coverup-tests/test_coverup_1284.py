# file: lib/ansible/module_utils/facts/system/distribution.py:381-395
# asked: {"lines": [], "branches": [[386, 388], [389, 391]]}
# gained: {"lines": [], "branches": [[386, 388], [389, 391]]}

import pytest
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def distribution_files():
    return DistributionFiles(None)

def test_parse_distribution_file_Mandriva_with_version_and_release(distribution_files):
    data = 'Mandriva\nDISTRIB_RELEASE="2021.1"\nDISTRIB_CODENAME="Cooker"'
    name = "Mandriva"
    path = "/etc/lsb-release"
    collected_facts = {}

    result, facts = distribution_files.parse_distribution_file_Mandriva(name, data, path, collected_facts)

    assert result is True
    assert facts['distribution'] == name
    assert facts['distribution_version'] == "2021.1"
    assert facts['distribution_release'] == "Cooker"

def test_parse_distribution_file_Mandriva_without_version(distribution_files):
    data = 'Mandriva\nDISTRIB_CODENAME="Cooker"'
    name = "Mandriva"
    path = "/etc/lsb-release"
    collected_facts = {}

    result, facts = distribution_files.parse_distribution_file_Mandriva(name, data, path, collected_facts)

    assert result is True
    assert facts['distribution'] == name
    assert 'distribution_version' not in facts
    assert facts['distribution_release'] == "Cooker"

def test_parse_distribution_file_Mandriva_without_release(distribution_files):
    data = 'Mandriva\nDISTRIB_RELEASE="2021.1"'
    name = "Mandriva"
    path = "/etc/lsb-release"
    collected_facts = {}

    result, facts = distribution_files.parse_distribution_file_Mandriva(name, data, path, collected_facts)

    assert result is True
    assert facts['distribution'] == name
    assert facts['distribution_version'] == "2021.1"
    assert 'distribution_release' not in facts

def test_parse_distribution_file_Mandriva_without_version_and_release(distribution_files):
    data = 'Mandriva'
    name = "Mandriva"
    path = "/etc/lsb-release"
    collected_facts = {}

    result, facts = distribution_files.parse_distribution_file_Mandriva(name, data, path, collected_facts)

    assert result is True
    assert facts['distribution'] == name
    assert 'distribution_version' not in facts
    assert 'distribution_release' not in facts

def test_parse_distribution_file_Mandriva_not_mandriva(distribution_files):
    data = 'NotMandriva\nDISTRIB_RELEASE="2021.1"\nDISTRIB_CODENAME="Cooker"'
    name = "NotMandriva"
    path = "/etc/lsb-release"
    collected_facts = {}

    result, facts = distribution_files.parse_distribution_file_Mandriva(name, data, path, collected_facts)

    assert result is True
    assert facts['distribution'] == name
    assert 'distribution_version' in facts
    assert facts['distribution_version'] == "2021.1"
    assert 'distribution_release' in facts
    assert facts['distribution_release'] == "Cooker"
