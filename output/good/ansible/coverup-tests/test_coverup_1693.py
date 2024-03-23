# file lib/ansible/module_utils/facts/hardware/aix.py:133-173
# lines []
# branches ['153->173', '155->173', '162->157']

import re
from unittest.mock import MagicMock

import pytest

from ansible.module_utils.facts.hardware.aix import AIXHardware


@pytest.fixture
def aix_hardware(mocker):
    module_mock = MagicMock()
    module_mock.get_bin_path.side_effect = lambda x: f"/usr/bin/{x}"
    hardware = AIXHardware(module=module_mock)
    return hardware


def test_get_vgs_facts_with_no_vgs(aix_hardware):
    aix_hardware.module.run_command.side_effect = [
        (0, "", ""),  # Simulate no volume groups
    ]
    vgs_facts = aix_hardware.get_vgs_facts()
    assert vgs_facts == {}


def test_get_vgs_facts_with_vgs_but_no_pvs(aix_hardware):
    aix_hardware.module.run_command.side_effect = [
        (0, "rootvg:\n", ""),  # Simulate volume group with no physical volumes
    ]
    vgs_facts = aix_hardware.get_vgs_facts()
    assert 'vgs' in vgs_facts
    assert 'rootvg' not in vgs_facts['vgs']


def test_get_vgs_facts_with_vgs_and_pvs(aix_hardware):
    aix_hardware.module.run_command.side_effect = [
        (0, "rootvg:\nPV_NAME           PV STATE          TOTAL PPs   FREE PPs    FREE DISTRIBUTION\nhdisk0            active            546         0           00..00..00..00..00\n", ""),
        (0, "PP SIZE: 128 megabyte\n", "")
    ]
    vgs_facts = aix_hardware.get_vgs_facts()
    assert 'vgs' in vgs_facts
    assert 'rootvg' in vgs_facts['vgs']
    assert vgs_facts['vgs']['rootvg'][0]['pv_name'] == 'hdisk0'
    assert vgs_facts['vgs']['rootvg'][0]['pv_state'] == 'active'
    assert vgs_facts['vgs']['rootvg'][0]['total_pps'] == '546'
    assert vgs_facts['vgs']['rootvg'][0]['free_pps'] == '0'
    assert vgs_facts['vgs']['rootvg'][0]['pp_size'] == '128 megabyte'
