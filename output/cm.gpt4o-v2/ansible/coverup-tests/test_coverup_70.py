# file: lib/ansible/module_utils/facts/hardware/aix.py:133-173
# asked: {"lines": [133, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 171, 173], "branches": [[153, 154], [153, 173], [155, 156], [155, 173], [157, 158], [157, 173], [162, 157], [162, 163], [164, 157], [164, 165]]}
# gained: {"lines": [133, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 171, 173], "branches": [[153, 154], [155, 156], [157, 158], [157, 173], [162, 163], [164, 157], [164, 165]]}

import pytest
from unittest.mock import MagicMock

@pytest.fixture
def aix_hardware():
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    module = MagicMock()
    return AIXHardware(module)

def test_get_vgs_facts(aix_hardware):
    # Mocking the module methods
    aix_hardware.module.get_bin_path = MagicMock(side_effect=lambda x: f"/usr/bin/{x}")
    aix_hardware.module.run_command = MagicMock(side_effect=[
        (0, "rootvg:\nPV_NAME           PV STATE          TOTAL PPs   FREE PPs    FREE DISTRIBUTION\nhdisk0            active            546         0           00..00..00..00..00\nhdisk1            active            546         113         00..00..00..21..92\n", ""),
        (0, "PP SIZE: 128 megabyte(s)\n", "")
    ])

    expected_vgs_facts = {
        'vgs': {
            'rootvg': [
                {'pv_name': 'hdisk0', 'pv_state': 'active', 'total_pps': '546', 'free_pps': '0', 'pp_size': '128 megabyte(s)'},
                {'pv_name': 'hdisk1', 'pv_state': 'active', 'total_pps': '546', 'free_pps': '113', 'pp_size': '128 megabyte(s)'}
            ]
        }
    }

    vgs_facts = aix_hardware.get_vgs_facts()
    assert vgs_facts == expected_vgs_facts

    # Ensure the commands were called as expected
    aix_hardware.module.get_bin_path.assert_any_call("lsvg")
    aix_hardware.module.get_bin_path.assert_any_call("xargs")
    aix_hardware.module.run_command.assert_any_call("/usr/bin/lsvg -o | /usr/bin/xargs /usr/bin/lsvg -p", use_unsafe_shell=True)
    aix_hardware.module.run_command.assert_any_call("/usr/bin/lsvg rootvg")
