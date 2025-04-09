# file: lib/ansible/module_utils/facts/system/distribution.py:319-379
# asked: {"lines": [320, 321, 322, 323, 324, 325, 328, 329, 330, 331, 332, 333, 334, 335, 336, 338, 339, 341, 342, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 367, 368, 369, 370, 371, 372, 373, 374, 375, 377, 379], "branches": [[321, 322], [321, 335], [324, 325], [324, 328], [328, 329], [328, 379], [330, 331], [330, 379], [333, 334], [333, 379], [335, 336], [335, 338], [338, 339], [338, 341], [341, 342], [341, 350], [342, 344], [342, 345], [345, 346], [345, 347], [348, 349], [348, 379], [350, 351], [350, 359], [353, 354], [353, 355], [356, 357], [356, 379], [359, 360], [359, 370], [362, 363], [362, 367], [368, 369], [368, 379], [370, 371], [370, 377], [373, 374], [373, 379]]}
# gained: {"lines": [320, 321, 322, 323, 324, 325, 328, 329, 330, 331, 332, 333, 334, 335, 336, 338, 339, 341, 342, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 367, 368, 369, 370, 371, 372, 373, 374, 375, 377, 379], "branches": [[321, 322], [321, 335], [324, 325], [328, 329], [330, 331], [333, 334], [335, 336], [335, 338], [338, 339], [338, 341], [341, 342], [341, 350], [342, 344], [342, 345], [345, 346], [348, 349], [350, 351], [350, 359], [353, 354], [356, 357], [359, 360], [359, 370], [362, 363], [368, 369], [370, 371], [370, 377], [373, 374]]}

import pytest
from unittest.mock import Mock
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def distribution_files():
    module = Mock()
    return DistributionFiles(module)

def test_parse_distribution_file_Debian_debian(distribution_files):
    data = "PRETTY_NAME=Debian GNU/Linux 10 (buster)"
    collected_facts = {'distribution_release': 'NA'}
    distribution_files.module.get_bin_path.return_value = "/usr/bin/dpkg"
    distribution_files.module.run_command.return_value = (0, "buster", "")
    
    result, facts = distribution_files.parse_distribution_file_Debian("Debian", data, "/etc/os-release", collected_facts)
    
    assert result is True
    assert facts['distribution'] == 'Debian'
    assert facts['distribution_release'] == 'buster'

def test_parse_distribution_file_Debian_ubuntu(distribution_files):
    data = "PRETTY_NAME=Ubuntu 20.04.1 LTS"
    collected_facts = {'distribution_release': 'NA'}
    
    result, facts = distribution_files.parse_distribution_file_Debian("Ubuntu", data, "/etc/os-release", collected_facts)
    
    assert result is True
    assert facts['distribution'] == 'Ubuntu'

def test_parse_distribution_file_Debian_steamos(distribution_files):
    data = "PRETTY_NAME=SteamOS 2.0"
    collected_facts = {'distribution_release': 'NA'}
    
    result, facts = distribution_files.parse_distribution_file_Debian("SteamOS", data, "/etc/os-release", collected_facts)
    
    assert result is True
    assert facts['distribution'] == 'SteamOS'

def test_parse_distribution_file_Debian_kali(distribution_files):
    data = "DISTRIB_ID=Kali\nDISTRIB_RELEASE=2020.4"
    collected_facts = {'distribution_release': 'NA'}
    
    result, facts = distribution_files.parse_distribution_file_Debian("Kali", data, "/etc/lsb-release", collected_facts)
    
    assert result is True
    assert facts['distribution'] == 'Kali'
    assert facts['distribution_release'] == '2020.4'

def test_parse_distribution_file_Debian_parrot(distribution_files):
    data = "DISTRIB_ID=Parrot\nDISTRIB_RELEASE=4.10"
    collected_facts = {'distribution_release': 'NA'}
    
    result, facts = distribution_files.parse_distribution_file_Debian("Parrot", data, "/etc/lsb-release", collected_facts)
    
    assert result is True
    assert facts['distribution'] == 'Parrot'
    assert facts['distribution_release'] == '4.10'

def test_parse_distribution_file_Debian_devuan(distribution_files):
    data = 'PRETTY_NAME="Devuan GNU/Linux 3 (beowulf)"\nVERSION_ID="3"'
    collected_facts = {'distribution_release': 'NA'}
    
    result, facts = distribution_files.parse_distribution_file_Debian("Devuan", data, "/etc/os-release", collected_facts)
    
    assert result is True
    assert facts['distribution'] == 'Devuan'
    assert facts['distribution_release'] == 'beowulf'
    assert facts['distribution_version'] == '3'
    assert facts['distribution_major_version'] == '3'

def test_parse_distribution_file_Debian_cumulus(distribution_files):
    data = 'VERSION_ID=3.7.5\nVERSION="Cumulus Linux 3.7.5"'
    collected_facts = {'distribution_release': 'NA'}
    
    result, facts = distribution_files.parse_distribution_file_Debian("Cumulus", data, "/etc/os-release", collected_facts)
    
    assert result is True
    assert facts['distribution'] == 'Cumulus Linux'
    assert facts['distribution_version'] == '3.7.5'
    assert facts['distribution_major_version'] == '3'
    assert facts['distribution_release'] == 'Cumulus Linux 3.7.5'

def test_parse_distribution_file_Debian_mint(distribution_files):
    data = 'PRETTY_NAME="Linux Mint 20.1 Ulyssa"\nVERSION_ID="20.1"'
    collected_facts = {'distribution_release': 'NA'}
    
    result, facts = distribution_files.parse_distribution_file_Debian("Mint", data, "/etc/os-release", collected_facts)
    
    assert result is True
    assert facts['distribution'] == 'Linux Mint'
    assert facts['distribution_version'] == '20.1'
    assert facts['distribution_major_version'] == '20'

def test_parse_distribution_file_Debian_unknown(distribution_files):
    data = 'PRETTY_NAME="Unknown Distro"'
    collected_facts = {'distribution_release': 'NA'}
    
    result, facts = distribution_files.parse_distribution_file_Debian("Unknown", data, "/etc/os-release", collected_facts)
    
    assert result is False
    assert facts == {}
