# file: lib/ansible/module_utils/facts/system/distribution.py:246-257
# asked: {"lines": [246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257], "branches": [[248, 249], [248, 250], [252, 253], [252, 254], [255, 256], [255, 257]]}
# gained: {"lines": [246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257], "branches": [[248, 249], [248, 250], [252, 253], [252, 254], [255, 256], [255, 257]]}

import pytest
import re
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def distribution_files(mocker):
    mock_module = mocker.Mock()
    return DistributionFiles(mock_module)

def test_parse_distribution_file_OpenWrt_no_openwrt(distribution_files):
    name = "OpenWrt"
    data = "Some random data"
    path = "/etc/openwrt_release"
    collected_facts = {}
    
    result, facts = distribution_files.parse_distribution_file_OpenWrt(name, data, path, collected_facts)
    
    assert result is False
    assert facts == {}

def test_parse_distribution_file_OpenWrt_with_openwrt(distribution_files):
    name = "OpenWrt"
    data = 'DISTRIB_ID="OpenWrt"\nDISTRIB_RELEASE="19.07.3"\nDISTRIB_CODENAME="Reboot"'
    path = "/etc/openwrt_release"
    collected_facts = {}
    
    result, facts = distribution_files.parse_distribution_file_OpenWrt(name, data, path, collected_facts)
    
    assert result is True
    assert facts['distribution'] == name
    assert facts['distribution_version'] == "19.07.3"
    assert facts['distribution_release'] == "Reboot"

def test_parse_distribution_file_OpenWrt_partial_data(distribution_files):
    name = "OpenWrt"
    data = 'DISTRIB_ID="OpenWrt"\nDISTRIB_RELEASE="19.07.3"'
    path = "/etc/openwrt_release"
    collected_facts = {}
    
    result, facts = distribution_files.parse_distribution_file_OpenWrt(name, data, path, collected_facts)
    
    assert result is True
    assert facts['distribution'] == name
    assert facts['distribution_version'] == "19.07.3"
    assert 'distribution_release' not in facts

def test_parse_distribution_file_OpenWrt_no_version(distribution_files):
    name = "OpenWrt"
    data = 'DISTRIB_ID="OpenWrt"\nDISTRIB_CODENAME="Reboot"'
    path = "/etc/openwrt_release"
    collected_facts = {}
    
    result, facts = distribution_files.parse_distribution_file_OpenWrt(name, data, path, collected_facts)
    
    assert result is True
    assert facts['distribution'] == name
    assert 'distribution_version' not in facts
    assert facts['distribution_release'] == "Reboot"
