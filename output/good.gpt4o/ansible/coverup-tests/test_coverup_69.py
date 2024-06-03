# file lib/ansible/module_utils/facts/hardware/darwin.py:92-132
# lines [92, 93, 94, 95, 98, 99, 100, 101, 102, 103, 105, 106, 110, 113, 115, 116, 117, 118, 121, 123, 124, 125, 126, 127, 128, 130, 132]
# branches ['106->110', '106->132', '115->116', '115->123', '123->124', '123->125', '125->126', '125->127', '127->128', '127->130']

import pytest
from unittest.mock import patch, MagicMock

# Assuming the DarwinHardware class is imported from ansible.module_utils.facts.hardware.darwin
from ansible.module_utils.facts.hardware.darwin import DarwinHardware

@pytest.fixture
def mock_module():
    module = MagicMock()
    module.run_command = MagicMock(return_value=(0, "Pages wired down: 1000\nPages active: 2000\nPages inactive: 3000\n", ""))
    return module

@pytest.fixture
def darwin_hardware(mock_module):
    dh = DarwinHardware(module=mock_module)
    dh.sysctl = {'hw.memsize': '8589934592'}  # 8 GB in bytes
    return dh

@patch('ansible.module_utils.facts.hardware.darwin.get_bin_path', return_value='/usr/bin/vm_stat')
def test_get_memory_facts(mock_get_bin_path, darwin_hardware):
    memory_facts = darwin_hardware.get_memory_facts()
    
    assert memory_facts['memtotal_mb'] == 8192  # 8 GB in MB
    # Correct calculation: 8 GB - (1000 + 2000 + 3000) * 4096 bytes in MB
    expected_free_mb = 8192 - ((1000 + 2000 + 3000) * 4096) // (1024 * 1024)
    assert memory_facts['memfree_mb'] == expected_free_mb

@patch('ansible.module_utils.facts.hardware.darwin.get_bin_path', side_effect=ValueError)
def test_get_memory_facts_no_vm_stat(mock_get_bin_path, darwin_hardware):
    memory_facts = darwin_hardware.get_memory_facts()
    
    assert memory_facts['memtotal_mb'] == 8192  # 8 GB in MB
    assert memory_facts['memfree_mb'] == 0  # No vm_stat, so memfree_mb should be 0
