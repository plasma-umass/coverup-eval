# file: lib/ansible/module_utils/facts/hardware/aix.py:133-173
# asked: {"lines": [], "branches": [[153, 173], [155, 173], [162, 157]]}
# gained: {"lines": [], "branches": [[153, 173], [155, 173]]}

import pytest
from unittest.mock import Mock, patch
import re
from ansible.module_utils.facts.hardware.aix import AIXHardware

@pytest.fixture
def aix_hardware():
    module = Mock()
    return AIXHardware(module)

def test_get_vgs_facts_no_lsvg_path(aix_hardware):
    aix_hardware.module.get_bin_path = Mock(return_value=None)
    result = aix_hardware.get_vgs_facts()
    assert result == {}

def test_get_vgs_facts_no_xargs_path(aix_hardware):
    aix_hardware.module.get_bin_path = Mock(side_effect=lambda x: None if x == "xargs" else "/usr/bin/lsvg")
    result = aix_hardware.get_vgs_facts()
    assert result == {}

def test_get_vgs_facts_command_fails(aix_hardware):
    aix_hardware.module.get_bin_path = Mock(return_value="/usr/bin/lsvg")
    aix_hardware.module.run_command = Mock(return_value=(1, "", "error"))
    result = aix_hardware.get_vgs_facts()
    assert result == {}

def test_get_vgs_facts_no_output(aix_hardware):
    aix_hardware.module.get_bin_path = Mock(return_value="/usr/bin/lsvg")
    aix_hardware.module.run_command = Mock(return_value=(0, "", ""))
    result = aix_hardware.get_vgs_facts()
    assert result == {}

def test_get_vgs_facts_success(aix_hardware):
    aix_hardware.module.get_bin_path = Mock(return_value="/usr/bin/lsvg")
    aix_hardware.module.run_command = Mock(side_effect=[
        (0, "rootvg:\nPV_NAME           PV STATE          TOTAL PPs   FREE PPs    FREE DISTRIBUTION\nhdisk0            active            546         0           00..00..00..00..00\nhdisk1            active            546         113         00..00..00..21..92\n", ""),
        (0, "PP SIZE: 128 megabyte(s)\n", "")
    ])
    result = aix_hardware.get_vgs_facts()
    expected = {
        'vgs': {
            'rootvg': [
                {'pv_name': 'hdisk0', 'pv_state': 'active', 'total_pps': '546', 'free_pps': '0', 'pp_size': '128 megabyte(s)'},
                {'pv_name': 'hdisk1', 'pv_state': 'active', 'total_pps': '546', 'free_pps': '113', 'pp_size': '128 megabyte(s)'}
            ]
        }
    }
    assert result == expected
