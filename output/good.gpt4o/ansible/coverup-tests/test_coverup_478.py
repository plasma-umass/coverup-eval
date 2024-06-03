# file lib/ansible/module_utils/facts/hardware/hpux.py:41-52
# lines [41, 42, 44, 45, 46, 48, 49, 50, 52]
# branches []

import pytest
from unittest.mock import patch, MagicMock

# Assuming the HPUXHardware class is imported from ansible.module_utils.facts.hardware.hpux
from ansible.module_utils.facts.hardware.hpux import HPUXHardware
from ansible.module_utils.basic import AnsibleModule

@pytest.fixture
def mock_hardware_methods(mocker):
    mocker.patch.object(HPUXHardware, 'get_cpu_facts', return_value={'cpu': 'mock_cpu'})
    mocker.patch.object(HPUXHardware, 'get_memory_facts', return_value={'memory': 'mock_memory'})
    mocker.patch.object(HPUXHardware, 'get_hw_facts', return_value={'hw': 'mock_hw'})

def test_populate(mock_hardware_methods):
    module = MagicMock(spec=AnsibleModule)
    hpux_hardware = HPUXHardware(module)
    collected_facts = {'some_fact': 'some_value'}
    
    result = hpux_hardware.populate(collected_facts=collected_facts)
    
    assert result == {
        'cpu': 'mock_cpu',
        'memory': 'mock_memory',
        'hw': 'mock_hw'
    }
