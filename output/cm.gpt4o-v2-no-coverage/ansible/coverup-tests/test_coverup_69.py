# file: lib/ansible/module_utils/facts/hardware/aix.py:133-173
# asked: {"lines": [133, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 171, 173], "branches": [[153, 154], [153, 173], [155, 156], [155, 173], [157, 158], [157, 173], [162, 157], [162, 163], [164, 157], [164, 165]]}
# gained: {"lines": [133, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 171, 173], "branches": [[153, 154], [153, 173], [155, 156], [155, 173], [157, 158], [157, 173], [162, 163], [164, 157], [164, 165]]}

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.hardware.aix import AIXHardware

@pytest.fixture
def mock_module():
    module = MagicMock()
    module.get_bin_path.side_effect = lambda x: f"/usr/bin/{x}"
    return module

def test_get_vgs_facts_no_paths(mock_module):
    hardware = AIXHardware(mock_module)
    mock_module.get_bin_path.side_effect = lambda x: None

    result = hardware.get_vgs_facts()
    assert result == {}

def test_get_vgs_facts_no_output(mock_module):
    hardware = AIXHardware(mock_module)
    mock_module.run_command.return_value = (0, "", "")

    result = hardware.get_vgs_facts()
    assert result == {}

def test_get_vgs_facts_with_data(mock_module):
    hardware = AIXHardware(mock_module)
    mock_module.run_command.side_effect = [
        (0, "rootvg:\nPV_NAME           PV STATE          TOTAL PPs   FREE PPs    FREE DISTRIBUTION\nhdisk0            active            546         0           00..00..00..00..00\nhdisk1            active            546         113         00..00..00..21..92\n", ""),
        (0, "PP SIZE: 128 megabyte(s)\n", "")
    ]

    result = hardware.get_vgs_facts()
    expected = {
        'vgs': {
            'rootvg': [
                {'pv_name': 'hdisk0', 'pv_state': 'active', 'total_pps': '546', 'free_pps': '0', 'pp_size': '128 megabyte(s)'},
                {'pv_name': 'hdisk1', 'pv_state': 'active', 'total_pps': '546', 'free_pps': '113', 'pp_size': '128 megabyte(s)'}
            ]
        }
    }
    assert result == expected
