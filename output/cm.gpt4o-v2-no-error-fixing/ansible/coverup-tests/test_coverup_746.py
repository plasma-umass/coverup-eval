# file: lib/ansible/module_utils/facts/system/distribution.py:381-395
# asked: {"lines": [382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 393, 395], "branches": [[383, 384], [383, 393], [386, 387], [386, 388], [389, 390], [389, 391]]}
# gained: {"lines": [382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 393, 395], "branches": [[383, 384], [383, 393], [386, 387], [389, 390]]}

import pytest
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def distribution_files():
    return DistributionFiles(None)

def test_parse_distribution_file_Mandriva_with_mandriva_data(distribution_files):
    data = 'Mandriva\nDISTRIB_RELEASE="2021.1"\nDISTRIB_CODENAME="Cooker"'
    name = 'Mandriva'
    path = '/etc/lsb-release'
    collected_facts = {}

    result, facts = distribution_files.parse_distribution_file_Mandriva(name, data, path, collected_facts)

    assert result is True
    assert facts['distribution'] == 'Mandriva'
    assert facts['distribution_version'] == '2021.1'
    assert facts['distribution_release'] == 'Cooker'

def test_parse_distribution_file_Mandriva_without_mandriva_data(distribution_files):
    data = 'SomeOtherDistro\nDISTRIB_RELEASE="2021.1"\nDISTRIB_CODENAME="Cooker"'
    name = 'SomeOtherDistro'
    path = '/etc/lsb-release'
    collected_facts = {}

    result, facts = distribution_files.parse_distribution_file_Mandriva(name, data, path, collected_facts)

    assert result is False
    assert facts == {}
