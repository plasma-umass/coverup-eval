# file: lib/ansible/module_utils/facts/hardware/freebsd.py:95-127
# asked: {"lines": [121], "branches": [[120, 121], [123, 127]]}
# gained: {"lines": [121], "branches": [[120, 121]]}

import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
from ansible.module_utils.basic import AnsibleModule

@pytest.fixture
def module():
    return Mock(spec=AnsibleModule)

@pytest.fixture
def hardware(module):
    return FreeBSDHardware(module)

def test_get_memory_facts_with_empty_last_line(hardware, module):
    module.get_bin_path.side_effect = lambda x: '/usr/sbin/' + x
    module.run_command.side_effect = [
        (0, "vm.stats.vm.v_page_size: 4096\nvm.stats.vm.v_page_count: 1048576\nvm.stats.vm.v_free_count: 524288\n", ""),
        (0, "Device          1K-blocks     Used    Avail Capacity\n/dev/ada0p3        314368000        0   314368000     0%\n\n", "")
    ]

    memory_facts = hardware.get_memory_facts()

    assert memory_facts['memtotal_mb'] == 4096 * 1048576 // 1024 // 1024
    assert memory_facts['memfree_mb'] == 4096 * 524288 // 1024 // 1024
    assert memory_facts['swaptotal_mb'] == 314368000 // 1024
    assert memory_facts['swapfree_mb'] == 314368000 // 1024

def test_get_memory_facts_with_non_device_line(hardware, module):
    module.get_bin_path.side_effect = lambda x: '/usr/sbin/' + x
    module.run_command.side_effect = [
        (0, "vm.stats.vm.v_page_size: 4096\nvm.stats.vm.v_page_count: 1048576\nvm.stats.vm.v_free_count: 524288\n", ""),
        (0, "swap_device        314368000        0   314368000     0%\n", "")
    ]

    memory_facts = hardware.get_memory_facts()

    assert memory_facts['memtotal_mb'] == 4096 * 1048576 // 1024 // 1024
    assert memory_facts['memfree_mb'] == 4096 * 524288 // 1024 // 1024
    assert memory_facts['swaptotal_mb'] == 314368000 // 1024
    assert memory_facts['swapfree_mb'] == 314368000 // 1024
