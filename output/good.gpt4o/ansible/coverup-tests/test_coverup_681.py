# file lib/ansible/module_utils/facts/hardware/netbsd.py:31-45
# lines [31, 32, 43, 44]
# branches []

import pytest
from unittest.mock import patch, MagicMock

# Assuming the NetBSDHardware class is imported from the module
from ansible.module_utils.facts.hardware.netbsd import NetBSDHardware

@pytest.fixture
def mock_hardware():
    with patch('ansible.module_utils.facts.hardware.netbsd.Hardware', autospec=True) as mock_hardware:
        yield mock_hardware

def test_netbsd_hardware_initialization(mock_hardware):
    mock_module = MagicMock()
    netbsd_hardware = NetBSDHardware(mock_module)
    assert netbsd_hardware.platform == 'NetBSD'
    assert netbsd_hardware.MEMORY_FACTS == ['MemTotal', 'SwapTotal', 'MemFree', 'SwapFree']

def test_netbsd_hardware_memory_facts(mock_hardware):
    mock_module = MagicMock()
    netbsd_hardware = NetBSDHardware(mock_module)
    memory_facts = netbsd_hardware.MEMORY_FACTS
    assert 'MemTotal' in memory_facts
    assert 'SwapTotal' in memory_facts
    assert 'MemFree' in memory_facts
    assert 'SwapFree' in memory_facts

def test_netbsd_hardware_platform(mock_hardware):
    mock_module = MagicMock()
    netbsd_hardware = NetBSDHardware(mock_module)
    assert netbsd_hardware.platform == 'NetBSD'
