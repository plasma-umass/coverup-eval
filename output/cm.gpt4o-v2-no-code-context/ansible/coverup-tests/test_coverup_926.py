# file: lib/ansible/module_utils/facts/hardware/darwin.py:92-132
# asked: {"lines": [93, 94, 95, 98, 99, 100, 101, 102, 103, 105, 106, 110, 113, 115, 116, 117, 118, 121, 123, 124, 125, 126, 127, 128, 130, 132], "branches": [[106, 110], [106, 132], [115, 116], [115, 123], [123, 124], [123, 125], [125, 126], [125, 127], [127, 128], [127, 130]]}
# gained: {"lines": [93, 94, 95, 98, 99, 100, 101, 102, 103, 105, 106, 110, 113, 115, 116, 117, 118, 121, 123, 124, 125, 126, 127, 128, 130, 132], "branches": [[106, 110], [106, 132], [115, 116], [115, 123], [123, 124], [125, 126], [127, 128]]}

import pytest
from unittest.mock import patch, MagicMock

# Assuming the DarwinHardware class is imported from the module
from ansible.module_utils.facts.hardware.darwin import DarwinHardware

@pytest.fixture
def darwin_hardware():
    module_mock = MagicMock()
    dh = DarwinHardware(module=module_mock)
    dh.sysctl = {'hw.memsize': '8589934592'}  # 8 GB in bytes
    return dh

def test_get_memory_facts_no_vm_stat(darwin_hardware):
    with patch('ansible.module_utils.facts.hardware.darwin.get_bin_path', side_effect=ValueError):
        memory_facts = darwin_hardware.get_memory_facts()
        assert memory_facts == {'memtotal_mb': 8192, 'memfree_mb': 0}

def test_get_memory_facts_vm_stat_failure(darwin_hardware):
    with patch('ansible.module_utils.facts.hardware.darwin.get_bin_path', return_value='/usr/bin/vm_stat'):
        darwin_hardware.module.run_command.return_value = (1, '', 'error')
        memory_facts = darwin_hardware.get_memory_facts()
        assert memory_facts == {'memtotal_mb': 8192, 'memfree_mb': 0}

def test_get_memory_facts_vm_stat_success(darwin_hardware):
    with patch('ansible.module_utils.facts.hardware.darwin.get_bin_path', return_value='/usr/bin/vm_stat'):
        vm_stat_output = (
            "Mach Virtual Memory Statistics: (page size of 4096 bytes)\n"
            "Pages free:                               1024.\n"
            "Pages active:                             2048.\n"
            "Pages inactive:                           4096.\n"
            "Pages speculative:                        512.\n"
            "Pages throttled:                          0.\n"
            "Pages wired down:                         1024.\n"
            "Pages purgeable:                          0.\n"
            "Translation faults:                       0.\n"
            "Pages copy-on-write:                      0.\n"
            "Pages zero filled:                        0.\n"
            "Pages reactivated:                        0.\n"
            "Pages purged:                             0.\n"
            "File-backed pages:                        0.\n"
            "Anonymous pages:                          0.\n"
            "Pages stored in compressor:               0.\n"
            "Pages occupied by compressor:             0.\n"
            "Decompressions:                           0.\n"
            "Compressions:                             0.\n"
            "Pageins:                                  0.\n"
            "Pageouts:                                 0.\n"
            "Swapins:                                  0.\n"
            "Swapouts:                                 0.\n"
        )
        darwin_hardware.module.run_command.return_value = (0, vm_stat_output, '')
        memory_facts = darwin_hardware.get_memory_facts()
        assert memory_facts['memtotal_mb'] == 8192
        assert memory_facts['memfree_mb'] == 8192 - ((1024 + 2048 + 4096) * 4096 // 1024 // 1024)
