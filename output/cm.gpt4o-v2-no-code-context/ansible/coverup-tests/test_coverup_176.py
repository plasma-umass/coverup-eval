# file: lib/ansible/module_utils/facts/system/distribution.py:381-395
# asked: {"lines": [381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 393, 395], "branches": [[383, 384], [383, 393], [386, 387], [386, 388], [389, 390], [389, 391]]}
# gained: {"lines": [381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 393, 395], "branches": [[383, 384], [383, 393], [386, 387], [386, 388], [389, 390], [389, 391]]}

import pytest
import re
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def distribution_files(mocker):
    module_mock = mocker.Mock()
    return DistributionFiles(module_mock)

def test_parse_distribution_file_Mandriva_with_mandriva_data(distribution_files):
    name = "Mandriva"
    data = 'Mandriva\nDISTRIB_RELEASE="2021.1"\nDISTRIB_CODENAME="Cooker"'
    path = "/etc/mandriva-release"
    collected_facts = {}

    result, facts = distribution_files.parse_distribution_file_Mandriva(name, data, path, collected_facts)

    assert result is True
    assert facts['distribution'] == 'Mandriva'
    assert facts['distribution_version'] == '2021.1'
    assert facts['distribution_release'] == 'Cooker'

def test_parse_distribution_file_Mandriva_without_mandriva_data(distribution_files):
    name = "Mandriva"
    data = 'Some other data'
    path = "/etc/mandriva-release"
    collected_facts = {}

    result, facts = distribution_files.parse_distribution_file_Mandriva(name, data, path, collected_facts)

    assert result is False
    assert facts == {}

def test_parse_distribution_file_Mandriva_partial_data(distribution_files):
    name = "Mandriva"
    data = 'Mandriva\nDISTRIB_RELEASE="2021.1"'
    path = "/etc/mandriva-release"
    collected_facts = {}

    result, facts = distribution_files.parse_distribution_file_Mandriva(name, data, path, collected_facts)

    assert result is True
    assert facts['distribution'] == 'Mandriva'
    assert facts['distribution_version'] == '2021.1'
    assert 'distribution_release' not in facts

def test_parse_distribution_file_Mandriva_no_release(distribution_files):
    name = "Mandriva"
    data = 'Mandriva\nDISTRIB_CODENAME="Cooker"'
    path = "/etc/mandriva-release"
    collected_facts = {}

    result, facts = distribution_files.parse_distribution_file_Mandriva(name, data, path, collected_facts)

    assert result is True
    assert facts['distribution'] == 'Mandriva'
    assert 'distribution_version' not in facts
    assert facts['distribution_release'] == 'Cooker'
