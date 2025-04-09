# file lib/ansible/module_utils/facts/system/distribution.py:381-395
# lines [381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 393, 395]
# branches ['383->384', '383->393', '386->387', '386->388', '389->390', '389->391']

import pytest
import re
from unittest.mock import patch

@pytest.fixture
def distribution_files():
    from ansible.module_utils.facts.system.distribution import DistributionFiles
    return DistributionFiles(None)

def test_parse_distribution_file_Mandriva(distribution_files):
    name = "Mandriva"
    data = 'DISTRIB_RELEASE="2021.1"\nDISTRIB_CODENAME="Mandriva2021"'
    path = "/etc/mandriva-release"
    collected_facts = {}

    success, facts = distribution_files.parse_distribution_file_Mandriva(name, data, path, collected_facts)

    assert success is True
    assert facts['distribution'] == 'Mandriva'
    assert facts['distribution_version'] == '2021.1'
    assert facts['distribution_release'] == 'Mandriva2021'

def test_parse_distribution_file_Mandriva_no_match(distribution_files):
    name = "Mandriva"
    data = 'Some other data'
    path = "/etc/mandriva-release"
    collected_facts = {}

    success, facts = distribution_files.parse_distribution_file_Mandriva(name, data, path, collected_facts)

    assert success is False
    assert facts == {}
