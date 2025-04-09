# file: lib/ansible/module_utils/facts/hardware/freebsd.py:95-127
# asked: {"lines": [95, 96, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 112, 113, 118, 119, 120, 121, 122, 123, 124, 125, 127], "branches": [[99, 100], [99, 112], [101, 102], [101, 109], [103, 104], [103, 105], [105, 106], [105, 107], [107, 101], [107, 108], [113, 118], [113, 127], [120, 121], [120, 122], [123, 124], [123, 127]]}
# gained: {"lines": [95, 96, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 112, 113, 118, 119, 120, 122, 123, 124, 125, 127], "branches": [[99, 100], [99, 112], [101, 102], [101, 109], [103, 104], [103, 105], [105, 106], [105, 107], [107, 101], [107, 108], [113, 118], [113, 127], [120, 122], [123, 124]]}

import pytest
from unittest.mock import MagicMock

@pytest.fixture
def module_mock():
    return MagicMock()

@pytest.fixture
def freebsd_hardware(module_mock):
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    hardware = FreeBSDHardware(module_mock)
    return hardware

def test_get_memory_facts_sysctl_present(freebsd_hardware, module_mock):
    module_mock.get_bin_path.side_effect = lambda x: '/sbin/' + x if x == 'sysctl' else None
    module_mock.run_command.return_value = (0, 'vm.stats.vm.v_page_size 4096\nvm.stats.vm.v_page_count 1048576\nvm.stats.vm.v_free_count 524288\n', '')

    memory_facts = freebsd_hardware.get_memory_facts()

    assert memory_facts['memtotal_mb'] == 4096 * 1048576 // 1024 // 1024
    assert memory_facts['memfree_mb'] == 4096 * 524288 // 1024 // 1024

def test_get_memory_facts_swapinfo_present(freebsd_hardware, module_mock):
    module_mock.get_bin_path.side_effect = lambda x: '/sbin/' + x if x == 'swapinfo' else None
    module_mock.run_command.return_value = (0, 'Device          1M-blocks     Used    Avail Capacity\n/dev/ada0p3        314368        0   314368     0%\n', '')

    memory_facts = freebsd_hardware.get_memory_facts()

    assert memory_facts['swaptotal_mb'] == 314368 // 1024
    assert memory_facts['swapfree_mb'] == 314368 // 1024

def test_get_memory_facts_sysctl_and_swapinfo_present(freebsd_hardware, module_mock):
    module_mock.get_bin_path.side_effect = lambda x: '/sbin/' + x
    module_mock.run_command.side_effect = [
        (0, 'vm.stats.vm.v_page_size 4096\nvm.stats.vm.v_page_count 1048576\nvm.stats.vm.v_free_count 524288\n', ''),
        (0, 'Device          1M-blocks     Used    Avail Capacity\n/dev/ada0p3        314368        0   314368     0%\n', '')
    ]

    memory_facts = freebsd_hardware.get_memory_facts()

    assert memory_facts['memtotal_mb'] == 4096 * 1048576 // 1024 // 1024
    assert memory_facts['memfree_mb'] == 4096 * 524288 // 1024 // 1024
    assert memory_facts['swaptotal_mb'] == 314368 // 1024
    assert memory_facts['swapfree_mb'] == 314368 // 1024

def test_get_memory_facts_no_sysctl_no_swapinfo(freebsd_hardware, module_mock):
    module_mock.get_bin_path.return_value = None

    memory_facts = freebsd_hardware.get_memory_facts()

    assert memory_facts == {}
