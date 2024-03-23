# file lib/ansible/module_utils/facts/hardware/openbsd.py:88-112
# lines [88, 89, 94, 95, 96, 97, 103, 104, 105, 106, 107, 108, 109, 110, 112]
# branches ['95->96', '95->103', '104->105', '104->112']

import pytest
from ansible.module_utils.facts.hardware.openbsd import OpenBSDHardware
from ansible.module_utils._text import to_text

@pytest.fixture
def mock_module(mocker):
    mock_module = mocker.MagicMock()
    mock_module.run_command = mocker.MagicMock()
    return mock_module

@pytest.fixture
def openbsd_hardware(mock_module):
    hardware = OpenBSDHardware(module=mock_module)
    hardware.sysctl = {'hw.usermem': '2097152'}  # 2GB in bytes
    return hardware

def test_get_memory_facts_vmstat_success(openbsd_hardware, mock_module):
    # Mock vmstat output
    vmstat_output = (
        "procs    memory       page                    disks    traps          cpu\n"
        "r b w    avm     fre  flt  re  pi  po  fr  sr wd0 fd0  int   sys   cs us sy id\n"
        "0 0 0  47512   28160   51   0   0   0   0   0   1   0  116    89   17  0  1 99\n"
    )
    mock_module.run_command.side_effect = [
        (0, vmstat_output, ''),
        (0, "total: 69268 1K-blocks allocated, 0 used, 69268 available", '')
    ]

    memory_facts = openbsd_hardware.get_memory_facts()

    assert memory_facts['memfree_mb'] == 27  # 28160 // 1024
    assert memory_facts['memtotal_mb'] == 2  # 2097152 // 1024 // 1024
    assert memory_facts['swapfree_mb'] == 67  # 69268 // 1024
    assert memory_facts['swaptotal_mb'] == 67  # 69268 // 1024

def test_get_memory_facts_swapctl_success(openbsd_hardware, mock_module):
    # Mock swapctl output
    swapctl_output = (
        "total: 69268k bytes allocated = 0k used, 69268k available\n"
    )
    mock_module.run_command.side_effect = [
        (1, '', ''),  # Simulate vmstat failure
        (0, swapctl_output, '')
    ]

    memory_facts = openbsd_hardware.get_memory_facts()

    assert 'memfree_mb' not in memory_facts  # vmstat failed
    assert 'memtotal_mb' not in memory_facts  # vmstat failed
    assert memory_facts['swapfree_mb'] == 67  # 69268k // 1024
    assert memory_facts['swaptotal_mb'] == 67  # 69268k // 1024
