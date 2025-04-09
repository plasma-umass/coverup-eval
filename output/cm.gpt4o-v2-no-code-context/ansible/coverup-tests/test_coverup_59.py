# file: lib/ansible/module_utils/facts/hardware/aix.py:133-173
# asked: {"lines": [133, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 171, 173], "branches": [[153, 154], [153, 173], [155, 156], [155, 173], [157, 158], [157, 173], [162, 157], [162, 163], [164, 157], [164, 165]]}
# gained: {"lines": [133, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 171, 173], "branches": [[153, 154], [153, 173], [155, 156], [155, 173], [157, 158], [157, 173], [162, 157], [162, 163], [164, 157], [164, 165]]}

import pytest
import re
from unittest.mock import Mock

# Assuming the AIXHardware class is imported from the module
from ansible.module_utils.facts.hardware.aix import AIXHardware

@pytest.fixture
def mock_module():
    module = Mock()
    module.get_bin_path.side_effect = lambda x: f"/usr/bin/{x}"
    return module

@pytest.fixture
def aix_hardware(mock_module):
    return AIXHardware(module=mock_module)

def test_get_vgs_facts_no_lsvg(aix_hardware, mock_module):
    mock_module.get_bin_path.side_effect = lambda x: None if x == "lsvg" else f"/usr/bin/{x}"
    result = aix_hardware.get_vgs_facts()
    assert result == {}

def test_get_vgs_facts_no_xargs(aix_hardware, mock_module):
    mock_module.get_bin_path.side_effect = lambda x: None if x == "xargs" else f"/usr/bin/{x}"
    result = aix_hardware.get_vgs_facts()
    assert result == {}

def test_get_vgs_facts_command_fails(aix_hardware, mock_module):
    mock_module.run_command.return_value = (1, '', 'error')
    result = aix_hardware.get_vgs_facts()
    assert result == {}

def test_get_vgs_facts_no_output(aix_hardware, mock_module):
    mock_module.run_command.return_value = (0, '', '')
    result = aix_hardware.get_vgs_facts()
    assert result == {}

def test_get_vgs_facts_success(aix_hardware, mock_module):
    lsvg_output = (
        "rootvg:\n"
        "PV_NAME           PV STATE          TOTAL PPs   FREE PPs    FREE DISTRIBUTION\n"
        "hdisk0            active            546         0           00..00..00..00..00\n"
        "hdisk1            active            546         113         00..00..00..21..92\n"
    )
    lsvg_rootvg_output = "PP SIZE: 128 megabyte(s)\n"
    
    mock_module.run_command.side_effect = [
        (0, lsvg_output, ''),
        (0, lsvg_rootvg_output, '')
    ]
    
    result = aix_hardware.get_vgs_facts()
    
    expected = {
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
    
    assert result == expected

def test_get_vgs_facts_partial_success(aix_hardware, mock_module):
    lsvg_output = (
        "rootvg:\n"
        "PV_NAME           PV STATE          TOTAL PPs   FREE PPs    FREE DISTRIBUTION\n"
        "hdisk0            active            546         0           00..00..00..00..00\n"
    )
    lsvg_rootvg_output = "PP SIZE: 128 megabyte(s)\n"
    
    mock_module.run_command.side_effect = [
        (0, lsvg_output, ''),
        (1, '', 'error')
    ]
    
    result = aix_hardware.get_vgs_facts()
    
    expected = {
        'vgs': {
            'rootvg': []
        }
    }
    
    assert result == expected
