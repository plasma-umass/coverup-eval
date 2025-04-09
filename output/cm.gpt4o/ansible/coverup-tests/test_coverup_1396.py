# file lib/ansible/module_utils/facts/hardware/openbsd.py:88-112
# lines [89, 94, 95, 96, 97, 103, 104, 105, 106, 107, 108, 109, 110, 112]
# branches ['95->96', '95->103', '104->105', '104->112']

import pytest
from unittest.mock import MagicMock

@pytest.fixture
def mock_module(mocker):
    module = MagicMock()
    module.run_command = MagicMock()
    return module

@pytest.fixture
def openbsd_hardware(mock_module):
    from ansible.module_utils.facts.hardware.openbsd import OpenBSDHardware
    hardware = OpenBSDHardware(module=mock_module)
    hardware.sysctl = {'hw.usermem': '104857600'}  # 100 MB for testing
    return hardware

def test_get_memory_facts(openbsd_hardware, mock_module):
    # Mock the output of vmstat command
    mock_module.run_command.side_effect = [
        (0, " procs    memory       page                    disks    traps          cpu\n"
            " r b w    avm     fre  flt  re  pi  po  fr  sr wd0 fd0  int   sys   cs us sy id\n"
            " 0 0 0  47512   28160   51   0   0   0   0   0   1   0  116    89   17  0  1 99", ""),
        (0, "total: 69268 1K-blocks allocated, 0 used, 69268 available", "")
    ]

    memory_facts = openbsd_hardware.get_memory_facts()

    assert memory_facts['memfree_mb'] == 28160 // 1024
    assert memory_facts['memtotal_mb'] == 100
    assert memory_facts['swapfree_mb'] == 69268 // 1024
    assert memory_facts['swaptotal_mb'] == 69268 // 1024

    # Ensure the run_command was called with the expected commands
    mock_module.run_command.assert_any_call("/usr/bin/vmstat")
    mock_module.run_command.assert_any_call("/sbin/swapctl -sk")
