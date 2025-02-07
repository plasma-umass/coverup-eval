# file: lib/ansible/module_utils/facts/hardware/aix.py:133-173
# asked: {"lines": [], "branches": [[162, 157]]}
# gained: {"lines": [], "branches": [[162, 157]]}

import pytest
from unittest.mock import Mock
import re
from ansible.module_utils.facts.hardware.aix import AIXHardware
from ansible.module_utils.basic import AnsibleModule

@pytest.fixture
def mock_module():
    module = Mock(spec=AnsibleModule)
    module.get_bin_path.side_effect = lambda x: f"/usr/bin/{x}"
    return module

def test_get_vgs_facts(mock_module):
    aix_hardware = AIXHardware(mock_module)
    
    # Mock the output of the run_command method
    mock_module.run_command.side_effect = [
        (0, "rootvg:\nPV_NAME           PV STATE          TOTAL PPs   FREE PPs    FREE DISTRIBUTION\nhdisk0            active            546         0           00..00..00..00..00\nhdisk1            active            546         113         00..00..00..21..92\n", ""),
        (0, "PP SIZE:        128 megabyte(s)\n", ""),
        (1, "", "Error")
    ]
    
    vgs_facts = aix_hardware.get_vgs_facts()
    
    expected_vgs_facts = {
        'vgs': {
            'rootvg': [
                {
                    'pv_name': 'hdisk0',
                    'pv_state': 'active',
                    'total_pps': '546',
                    'free_pps': '0',
                    'pp_size': '128 megabyte(s)'
                },
                {
                    'pv_name': 'hdisk1',
                    'pv_state': 'active',
                    'total_pps': '546',
                    'free_pps': '113',
                    'pp_size': '128 megabyte(s)'
                }
            ]
        }
    }
    
    assert vgs_facts == expected_vgs_facts
    mock_module.run_command.assert_any_call("/usr/bin/lsvg -o | /usr/bin/xargs /usr/bin/lsvg -p", use_unsafe_shell=True)
    mock_module.run_command.assert_any_call("/usr/bin/lsvg rootvg")

    # Test the branch where rc != 0
    mock_module.run_command.side_effect = [
        (0, "rootvg:\nPV_NAME           PV STATE          TOTAL PPs   FREE PPs    FREE DISTRIBUTION\nhdisk0            active            546         0           00..00..00..00..00\nhdisk1            active            546         113         00..00..00..21..92\n", ""),
        (1, "", "Error")
    ]
    
    vgs_facts = aix_hardware.get_vgs_facts()
    
    expected_vgs_facts = {
        'vgs': {
            'rootvg': []
        }
    }
    
    assert vgs_facts == expected_vgs_facts
    mock_module.run_command.assert_any_call("/usr/bin/lsvg rootvg")
