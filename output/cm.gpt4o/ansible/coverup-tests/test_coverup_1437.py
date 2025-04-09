# file lib/ansible/module_utils/facts/hardware/darwin.py:92-132
# lines [118, 121]
# branches ['106->132', '123->125', '125->127', '127->130']

import pytest
from unittest.mock import patch, MagicMock

# Assuming the DarwinHardware class is imported from ansible.module_utils.facts.hardware.darwin
from ansible.module_utils.facts.hardware.darwin import DarwinHardware

@pytest.fixture
def darwin_hardware():
    module_mock = MagicMock()
    dh = DarwinHardware(module=module_mock)
    dh.sysctl = {'hw.memsize': '8589934592'}  # 8 GB
    return dh

@patch('ansible.module_utils.facts.hardware.darwin.get_bin_path')
def test_get_memory_facts_full_coverage(mock_get_bin_path, darwin_hardware):
    mock_get_bin_path.return_value = '/usr/bin/vm_stat'
    
    # Mocking the output of the vm_stat command
    darwin_hardware.module.run_command.return_value = (0, 
        "Mach Virtual Memory Statistics: (page size of 4096 bytes)\n"
        "Pages free:                               1024.\n"
        "Pages active:                             2048.\n"
        "Pages inactive:                           4096.\n"
        "Pages speculative:                        512.\n"
        "Pages throttled:                          0.\n"
        "Pages wired down:                         1024.\n"
        "Pages purgeable:                          256.\n"
        "Translation faults:                       123456.\n"
        "Pages copy-on-write:                      7890.\n"
        "Pages zero filled:                        1234567.\n"
        "Pages reactivated:                        890.\n"
        "Pages purged:                             1234.\n"
        "File-backed pages:                        5678.\n"
        "Anonymous pages:                          91011.\n"
        "Pages stored in compressor:               1213.\n"
        "Pages occupied by compressor:             1415.\n"
        "Decompressions:                           1617.\n"
        "Compressions:                             1819.\n"
        "Pageins:                                  2021.\n"
        "Pageouts:                                 2223.\n"
        "Swapins:                                  2425.\n"
        "Swapouts:                                 2627.\n", 
        ''
    )
    
    memory_facts = darwin_hardware.get_memory_facts()
    
    assert memory_facts['memtotal_mb'] == 8192
    # Corrected calculation for memfree_mb
    expected_memfree_mb = 8192 - ((1024 + 2048 + 4096) * 4096 // 1024 // 1024)
    assert memory_facts['memfree_mb'] == expected_memfree_mb

    # Ensure the run_command was called with the correct command
    darwin_hardware.module.run_command.assert_called_once_with('/usr/bin/vm_stat')
