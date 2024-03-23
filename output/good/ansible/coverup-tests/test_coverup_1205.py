# file lib/ansible/module_utils/facts/hardware/netbsd.py:101-112
# lines [102, 103, 104, 105, 106, 107, 108, 109, 110, 112]
# branches ['103->104', '103->105', '105->106', '105->112', '108->105', '108->109']

import os
import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.hardware.netbsd import NetBSDHardware

# Mocking the get_file_lines function
def mock_get_file_lines(file_path):
    return [
        "MemTotal:       16384 kB",
        "MemFree:         2048 kB",
        "SwapTotal:       8192 kB",
        "SwapFree:        8192 kB"
    ]

@pytest.fixture
def mock_os_access(mocker):
    mocker.patch('os.access', return_value=True)

@pytest.fixture
def mock_get_file_lines_fixture(mocker):
    mocker.patch('ansible.module_utils.facts.hardware.netbsd.get_file_lines', side_effect=mock_get_file_lines)

def test_get_memory_facts(mock_os_access, mock_get_file_lines_fixture):
    module_mock = MagicMock()
    netbsd_hardware = NetBSDHardware(module=module_mock)
    netbsd_hardware.MEMORY_FACTS = ['MemTotal', 'MemFree', 'SwapTotal', 'SwapFree']
    memory_facts = netbsd_hardware.get_memory_facts()

    assert memory_facts['memtotal_mb'] == 16
    assert memory_facts['memfree_mb'] == 2
    assert memory_facts['swaptotal_mb'] == 8
    assert memory_facts['swapfree_mb'] == 8
