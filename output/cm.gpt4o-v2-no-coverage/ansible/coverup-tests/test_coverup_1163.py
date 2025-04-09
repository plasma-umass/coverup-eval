# file: lib/ansible/module_utils/facts/hardware/hpux.py:41-52
# asked: {"lines": [42, 44, 45, 46, 48, 49, 50, 52], "branches": []}
# gained: {"lines": [42, 44, 45, 46, 48, 49, 50, 52], "branches": []}

import pytest
from unittest.mock import patch, MagicMock

from ansible.module_utils.facts.hardware.hpux import HPUXHardware

@pytest.fixture
def hpux_hardware():
    module = MagicMock()
    return HPUXHardware(module)

def test_populate(hpux_hardware):
    with patch.object(hpux_hardware, 'get_cpu_facts', return_value={'cpu': 'test_cpu'}) as mock_get_cpu_facts, \
         patch.object(hpux_hardware, 'get_memory_facts', return_value={'memory': 'test_memory'}) as mock_get_memory_facts, \
         patch.object(hpux_hardware, 'get_hw_facts', return_value={'hw': 'test_hw'}) as mock_get_hw_facts:
        
        result = hpux_hardware.populate()
        
        assert result == {
            'cpu': 'test_cpu',
            'memory': 'test_memory',
            'hw': 'test_hw'
        }
        
        mock_get_cpu_facts.assert_called_once_with(collected_facts=None)
        mock_get_memory_facts.assert_called_once()
        mock_get_hw_facts.assert_called_once()
