# file: lib/ansible/module_utils/facts/hardware/hpux.py:41-52
# asked: {"lines": [41, 42, 44, 45, 46, 48, 49, 50, 52], "branches": []}
# gained: {"lines": [41, 42, 44, 45, 46, 48, 49, 50, 52], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.hardware.hpux import HPUXHardware

@pytest.fixture
def hpux_hardware():
    return HPUXHardware(module=MagicMock())

def test_populate(hpux_hardware, mocker):
    # Mock the methods get_cpu_facts, get_memory_facts, and get_hw_facts
    mocker.patch.object(hpux_hardware, 'get_cpu_facts', return_value={'cpu': 'test_cpu'})
    mocker.patch.object(hpux_hardware, 'get_memory_facts', return_value={'memory': 'test_memory'})
    mocker.patch.object(hpux_hardware, 'get_hw_facts', return_value={'hw': 'test_hw'})

    # Call the populate method
    result = hpux_hardware.populate()

    # Assertions to verify the results
    assert result == {'cpu': 'test_cpu', 'memory': 'test_memory', 'hw': 'test_hw'}
    hpux_hardware.get_cpu_facts.assert_called_once()
    hpux_hardware.get_memory_facts.assert_called_once()
    hpux_hardware.get_hw_facts.assert_called_once()
