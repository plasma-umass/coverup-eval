# file lib/ansible/module_utils/facts/system/distribution.py:246-257
# lines [249]
# branches ['248->249', '252->254']

import pytest
from ansible.module_utils.facts.system.distribution import DistributionFiles

class MockModule:
    pass

@pytest.fixture
def dist_files():
    return DistributionFiles(module=MockModule())

def test_parse_distribution_file_OpenWrt_no_openwrt(dist_files):
    name = "OpenWrt"
    data = "Some other data"
    path = "/etc/openwrt_release"
    collected_facts = {}

    result, facts = dist_files.parse_distribution_file_OpenWrt(name, data, path, collected_facts)
    
    assert result is False
    assert facts == {}

def test_parse_distribution_file_OpenWrt_no_version(dist_files):
    name = "OpenWrt"
    data = 'OpenWrt\nDISTRIB_CODENAME="somecodename"'
    path = "/etc/openwrt_release"
    collected_facts = {}

    result, facts = dist_files.parse_distribution_file_OpenWrt(name, data, path, collected_facts)
    
    assert result is True
    assert facts == {
        'distribution': name,
        'distribution_release': 'somecodename'
    }
