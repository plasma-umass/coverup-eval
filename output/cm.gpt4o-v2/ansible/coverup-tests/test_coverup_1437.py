# file: lib/ansible/module_utils/facts/hardware/freebsd.py:95-127
# asked: {"lines": [], "branches": [[123, 127]]}
# gained: {"lines": [], "branches": [[123, 127]]}

import pytest
from unittest.mock import MagicMock

@pytest.fixture
def module_mock():
    module = MagicMock()
    module.get_bin_path = MagicMock(side_effect=lambda x: '/usr/sbin/' + x if x in ['sysctl', 'swapinfo'] else None)
    return module

@pytest.fixture
def freebsd_hardware(module_mock):
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    hardware = FreeBSDHardware(module_mock)
    return hardware

def test_get_memory_facts_with_swapinfo(freebsd_hardware, module_mock):
    sysctl_output = "vm.stats.vm.v_page_size 4096\nvm.stats.vm.v_page_count 1048576\nvm.stats.vm.v_free_count 524288\n"
    swapinfo_output = "Device          1K-blocks     Used    Avail Capacity\n/dev/ada0p3     314368000        0   314368000     0%\n"
    
    module_mock.run_command = MagicMock(side_effect=[
        (0, sysctl_output, ''),
        (0, swapinfo_output, '')
    ])
    
    memory_facts = freebsd_hardware.get_memory_facts()
    
    assert memory_facts['memtotal_mb'] == 4096 * 1048576 // 1024 // 1024
    assert memory_facts['memfree_mb'] == 4096 * 524288 // 1024 // 1024
    assert memory_facts['swaptotal_mb'] == 314368000 // 1024
    assert memory_facts['swapfree_mb'] == 314368000 // 1024

def test_get_memory_facts_without_swapinfo(freebsd_hardware, module_mock):
    sysctl_output = "vm.stats.vm.v_page_size 4096\nvm.stats.vm.v_page_count 1048576\nvm.stats.vm.v_free_count 524288\n"
    swapinfo_output = "Device          1K-blocks     Used    Avail Capacity\n"
    
    module_mock.run_command = MagicMock(side_effect=[
        (0, sysctl_output, ''),
        (0, swapinfo_output, '')
    ])
    
    memory_facts = freebsd_hardware.get_memory_facts()
    
    assert memory_facts['memtotal_mb'] == 4096 * 1048576 // 1024 // 1024
    assert memory_facts['memfree_mb'] == 4096 * 524288 // 1024 // 1024
    assert 'swaptotal_mb' not in memory_facts
    assert 'swapfree_mb' not in memory_facts
