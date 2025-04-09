# file lib/ansible/module_utils/facts/hardware/hpux.py:41-52
# lines [41, 42, 44, 45, 46, 48, 49, 50, 52]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.hardware.hpux import HPUXHardware

@pytest.fixture
def mock_cpu_facts(mocker):
    return mocker.patch.object(HPUXHardware, 'get_cpu_facts', return_value={'cpu': 'test_cpu'})

@pytest.fixture
def mock_memory_facts(mocker):
    return mocker.patch.object(HPUXHardware, 'get_memory_facts', return_value={'memory': 'test_memory'})

@pytest.fixture
def mock_hw_facts(mocker):
    return mocker.patch.object(HPUXHardware, 'get_hw_facts', return_value={'hardware': 'test_hardware'})

def test_hpux_hardware_populate(mock_cpu_facts, mock_memory_facts, mock_hw_facts):
    module_mock = MagicMock()
    hpux_hardware = HPUXHardware(module=module_mock)
    facts = hpux_hardware.populate()
    assert facts['cpu'] == 'test_cpu'
    assert facts['memory'] == 'test_memory'
    assert facts['hardware'] == 'test_hardware'
    mock_cpu_facts.assert_called_once()
    mock_memory_facts.assert_called_once()
    mock_hw_facts.assert_called_once()
