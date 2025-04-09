# file: lib/ansible/module_utils/facts/hardware/openbsd.py:88-112
# asked: {"lines": [88, 89, 94, 95, 96, 97, 103, 104, 105, 106, 107, 108, 109, 110, 112], "branches": [[95, 96], [95, 103], [104, 105], [104, 112]]}
# gained: {"lines": [88, 89, 94, 95, 96, 97, 103, 104, 105, 106, 107, 108, 109, 110, 112], "branches": [[95, 96], [95, 103], [104, 105], [104, 112]]}

import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.facts.hardware.openbsd import OpenBSDHardware

@pytest.fixture
def module():
    return Mock()

@pytest.fixture
def openbsd_hardware(module):
    return OpenBSDHardware(module)

def test_get_memory_facts_vmstat_success(openbsd_hardware, module):
    vmstat_output = " procs    memory       page                    disks    traps          cpu\n r b w    avm     fre  flt  re  pi  po  fr  sr wd0 fd0  int   sys   cs us sy id\n 0 0 0  47512   28160   51   0   0   0   0   0   1   0  116    89   17  0  1 99"
    sysctl_output = {'hw.usermem': '104857600'}
    module.run_command.side_effect = [(0, vmstat_output, ''), (0, "total: 69268 1K-blocks allocated, 0 used, 69268 available", '')]
    openbsd_hardware.sysctl = sysctl_output

    memory_facts = openbsd_hardware.get_memory_facts()

    assert memory_facts['memfree_mb'] == 28160 // 1024
    assert memory_facts['memtotal_mb'] == 104857600 // 1024 // 1024
    assert memory_facts['swapfree_mb'] == 69268 // 1024
    assert memory_facts['swaptotal_mb'] == 69268 // 1024

def test_get_memory_facts_vmstat_failure(openbsd_hardware, module):
    module.run_command.side_effect = [(1, '', 'error'), (0, "total: 69268 1K-blocks allocated, 0 used, 69268 available", '')]

    memory_facts = openbsd_hardware.get_memory_facts()

    assert 'memfree_mb' not in memory_facts
    assert 'memtotal_mb' not in memory_facts
    assert memory_facts['swapfree_mb'] == 69268 // 1024
    assert memory_facts['swaptotal_mb'] == 69268 // 1024

def test_get_memory_facts_swapctl_failure(openbsd_hardware, module):
    vmstat_output = " procs    memory       page                    disks    traps          cpu\n r b w    avm     fre  flt  re  pi  po  fr  sr wd0 fd0  int   sys   cs us sy id\n 0 0 0  47512   28160   51   0   0   0   0   0   1   0  116    89   17  0  1 99"
    sysctl_output = {'hw.usermem': '104857600'}
    module.run_command.side_effect = [(0, vmstat_output, ''), (1, '', 'error')]
    openbsd_hardware.sysctl = sysctl_output

    memory_facts = openbsd_hardware.get_memory_facts()

    assert memory_facts['memfree_mb'] == 28160 // 1024
    assert memory_facts['memtotal_mb'] == 104857600 // 1024 // 1024
    assert 'swapfree_mb' not in memory_facts
    assert 'swaptotal_mb' not in memory_facts
