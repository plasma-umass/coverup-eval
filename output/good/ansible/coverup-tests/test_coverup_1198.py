# file lib/ansible/module_utils/facts/system/distribution.py:246-257
# lines [247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257]
# branches ['248->249', '248->250', '252->253', '252->254', '255->256', '255->257']

import re
import pytest
from unittest.mock import MagicMock

# Assuming the DistributionFiles class is part of a module named distribution
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def mock_openwrt_data():
    data = """
    DISTRIB_ID='OpenWrt'
    DISTRIB_RELEASE='19.07.3'
    DISTRIB_CODENAME='openwrt-19.07'
    DISTRIB_DESCRIPTION='OpenWrt 19.07.3 r11063-85e04e9f46'
    """
    return data.strip()

def test_parse_distribution_file_OpenWrt(mocker, mock_openwrt_data):
    mocker.patch('ansible.module_utils.facts.system.distribution.re.search')
    distribution_files = DistributionFiles(module=MagicMock())
    collected_facts = {}

    # Mock the re.search to return a match object with the expected groups
    re.search.side_effect = lambda pattern, data: MagicMock(groups=lambda: ('19.07.3',)) if 'DISTRIB_RELEASE' in pattern else MagicMock(groups=lambda: ('openwrt-19.07',)) if 'DISTRIB_CODENAME' in pattern else None

    success, openwrt_facts = distribution_files.parse_distribution_file_OpenWrt('OpenWrt', mock_openwrt_data, '/etc/openwrt_release', collected_facts)

    assert success is True
    assert openwrt_facts['distribution'] == 'OpenWrt'
    assert openwrt_facts['distribution_version'] == '19.07.3'
    assert openwrt_facts['distribution_release'] == 'openwrt-19.07'
    re.search.assert_any_call('DISTRIB_RELEASE="(.*)"', mock_openwrt_data)
    re.search.assert_any_call('DISTRIB_CODENAME="(.*)"', mock_openwrt_data)
