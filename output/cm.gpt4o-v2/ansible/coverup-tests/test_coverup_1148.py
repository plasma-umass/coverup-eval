# file: lib/ansible/module_utils/facts/hardware/openbsd.py:88-112
# asked: {"lines": [89, 94, 95, 96, 97, 103, 104, 105, 106, 107, 108, 109, 110, 112], "branches": [[95, 96], [95, 103], [104, 105], [104, 112]]}
# gained: {"lines": [89, 94, 95, 96, 97, 103, 104, 105, 106, 107, 108, 109, 110, 112], "branches": [[95, 96], [95, 103], [104, 105], [104, 112]]}

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.hardware.openbsd import OpenBSDHardware

@pytest.fixture
def module_mock():
    return MagicMock()

@pytest.fixture
def openbsd_hardware(module_mock):
    hardware = OpenBSDHardware(module_mock)
    hardware.sysctl = {'hw.usermem': '1048576'}  # 1 GB in KB
    return hardware

def test_get_memory_facts_vmstat_success(openbsd_hardware, module_mock):
    vmstat_output = " procs    memory       page                    disks    traps          cpu\n" \
                    " r b w    avm     fre  flt  re  pi  po  fr  sr wd0 fd0  int   sys   cs us sy id\n" \
                    " 0 0 0  47512   28160   51   0   0   0   0   0   1   0  116    89   17  0  1 99"
    module_mock.run_command.side_effect = [
        (0, vmstat_output, ''),  # vmstat command
        (0, "total: 69268 1K-blocks allocated, 0 used, 69268 available", '')  # swapctl command
    ]

    memory_facts = openbsd_hardware.get_memory_facts()

    assert memory_facts['memfree_mb'] == 28160 // 1024
    assert memory_facts['memtotal_mb'] == 1048576 // 1024 // 1024
    assert memory_facts['swapfree_mb'] == 69268 // 1024
    assert memory_facts['swaptotal_mb'] == 69268 // 1024

def test_get_memory_facts_vmstat_failure(openbsd_hardware, module_mock):
    module_mock.run_command.side_effect = [
        (1, '', 'error'),  # vmstat command fails
        (0, "total: 69268 1K-blocks allocated, 0 used, 69268 available", '')  # swapctl command
    ]

    memory_facts = openbsd_hardware.get_memory_facts()

    assert 'memfree_mb' not in memory_facts
    assert 'memtotal_mb' not in memory_facts
    assert memory_facts['swapfree_mb'] == 69268 // 1024
    assert memory_facts['swaptotal_mb'] == 69268 // 1024

def test_get_memory_facts_swapctl_failure(openbsd_hardware, module_mock):
    vmstat_output = " procs    memory       page                    disks    traps          cpu\n" \
                    " r b w    avm     fre  flt  re  pi  po  fr  sr wd0 fd0  int   sys   cs us sy id\n" \
                    " 0 0 0  47512   28160   51   0   0   0   0   0   1   0  116    89   17  0  1 99"
    module_mock.run_command.side_effect = [
        (0, vmstat_output, ''),  # vmstat command
        (1, '', 'error')  # swapctl command fails
    ]

    memory_facts = openbsd_hardware.get_memory_facts()

    assert memory_facts['memfree_mb'] == 28160 // 1024
    assert memory_facts['memtotal_mb'] == 1048576 // 1024 // 1024
    assert 'swapfree_mb' not in memory_facts
    assert 'swaptotal_mb' not in memory_facts
