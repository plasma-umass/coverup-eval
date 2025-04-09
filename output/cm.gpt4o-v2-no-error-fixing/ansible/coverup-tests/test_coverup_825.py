# file: lib/ansible/module_utils/facts/hardware/freebsd.py:95-127
# asked: {"lines": [121], "branches": [[120, 121], [123, 127]]}
# gained: {"lines": [121], "branches": [[120, 121], [123, 127]]}

import pytest
from unittest.mock import MagicMock

# Assuming the FreeBSDHardware class is imported from ansible.module_utils.facts.hardware.freebsd
from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware

@pytest.fixture
def module_mock():
    return MagicMock()

@pytest.fixture
def freebsd_hardware(module_mock):
    return FreeBSDHardware(module_mock)

def test_get_memory_facts_swapinfo_empty_line(freebsd_hardware, module_mock):
    # Mocking get_bin_path to return a valid path
    module_mock.get_bin_path.side_effect = lambda x: '/usr/sbin/' + x if x in ['sysctl', 'swapinfo'] else None
    
    # Mocking run_command for sysctl
    module_mock.run_command.side_effect = [
        (0, "vm.stats.vm.v_page_size 4096\nvm.stats.vm.v_page_count 1048576\nvm.stats.vm.v_free_count 524288\n", ""),
        (0, "Device          1K-blocks     Used    Avail Capacity\n/dev/ada0p3        314368000        0   314368000     0%\n\n", "")
    ]
    
    memory_facts = freebsd_hardware.get_memory_facts()
    
    assert memory_facts['memtotal_mb'] == 4096 * 1048576 // 1024 // 1024
    assert memory_facts['memfree_mb'] == 4096 * 524288 // 1024 // 1024
    assert memory_facts['swaptotal_mb'] == 314368000 // 1024
    assert memory_facts['swapfree_mb'] == 314368000 // 1024

def test_get_memory_facts_swapinfo_no_device(freebsd_hardware, module_mock):
    # Mocking get_bin_path to return a valid path
    module_mock.get_bin_path.side_effect = lambda x: '/usr/sbin/' + x if x in ['sysctl', 'swapinfo'] else None
    
    # Mocking run_command for sysctl
    module_mock.run_command.side_effect = [
        (0, "vm.stats.vm.v_page_size 4096\nvm.stats.vm.v_page_count 1048576\nvm.stats.vm.v_free_count 524288\n", ""),
        (0, "/dev/ada0p3        314368000        0   314368000     0%\n", "")
    ]
    
    memory_facts = freebsd_hardware.get_memory_facts()
    
    assert memory_facts['memtotal_mb'] == 4096 * 1048576 // 1024 // 1024
    assert memory_facts['memfree_mb'] == 4096 * 524288 // 1024 // 1024
    assert memory_facts['swaptotal_mb'] == 314368000 // 1024
    assert memory_facts['swapfree_mb'] == 314368000 // 1024

def test_get_memory_facts_swapinfo_device_line(freebsd_hardware, module_mock):
    # Mocking get_bin_path to return a valid path
    module_mock.get_bin_path.side_effect = lambda x: '/usr/sbin/' + x if x in ['sysctl', 'swapinfo'] else None
    
    # Mocking run_command for sysctl
    module_mock.run_command.side_effect = [
        (0, "vm.stats.vm.v_page_size 4096\nvm.stats.vm.v_page_count 1048576\nvm.stats.vm.v_free_count 524288\n", ""),
        (0, "Device          1K-blocks     Used    Avail Capacity\n", "")
    ]
    
    memory_facts = freebsd_hardware.get_memory_facts()
    
    assert memory_facts['memtotal_mb'] == 4096 * 1048576 // 1024 // 1024
    assert memory_facts['memfree_mb'] == 4096 * 524288 // 1024 // 1024
    assert 'swaptotal_mb' not in memory_facts
    assert 'swapfree_mb' not in memory_facts
