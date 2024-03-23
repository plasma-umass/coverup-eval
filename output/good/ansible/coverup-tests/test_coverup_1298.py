# file lib/ansible/module_utils/facts/hardware/aix.py:133-173
# lines [149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 171, 173]
# branches ['153->154', '153->173', '155->156', '155->173', '157->158', '157->173', '162->157', '162->163', '164->157', '164->165']

import re
import pytest
from unittest.mock import MagicMock

# Assuming AIXHardware is part of a module named aix, and it's the only class in that module
from ansible.module_utils.facts.hardware import aix

@pytest.fixture
def mock_module(mocker):
    mock = MagicMock()
    mock.get_bin_path = MagicMock(side_effect=lambda x: "/usr/bin/" + x)
    mock.run_command = MagicMock()
    return mock

def test_get_vgs_facts(mock_module, mocker):
    # Create an instance of AIXHardware with the mock_module
    hardware = aix.AIXHardware(module=mock_module)

    # Mock the output of the `lsvg` and `lsvg <vg_name>` commands
    mock_module.run_command.side_effect = [
        (0, "rootvg:\nFREE DISTRIBUTION\nhdisk0 active 546 0 00..00..00..00..00\n", ""),
        (0, "PP SIZE: 128 megabyte", ""),
    ]

    expected_vgs_facts = {
        'vgs': {
            'rootvg': [
                {
                    'pv_name': 'hdisk0',
                    'pv_state': 'active',
                    'total_pps': '546',
                    'free_pps': '0',
                    'pp_size': '128 megabyte'
                }
            ]
        }
    }

    vgs_facts = hardware.get_vgs_facts()

    assert vgs_facts == expected_vgs_facts
    # Ensure the run_command was called with the expected commands
    mock_module.run_command.assert_any_call("/usr/bin/lsvg -o | /usr/bin/xargs /usr/bin/lsvg -p", use_unsafe_shell=True)
    # Correct the assertion to match the actual call without the 'use_unsafe_shell' parameter
    mock_module.run_command.assert_any_call("/usr/bin/lsvg rootvg")
