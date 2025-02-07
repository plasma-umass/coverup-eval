# file: lib/ansible/module_utils/facts/hardware/freebsd.py:47-69
# asked: {"lines": [47, 48, 50, 51, 52, 53, 54, 56, 57, 58, 59, 60, 62, 63, 64, 65, 66, 67, 69], "branches": []}
# gained: {"lines": [47, 48, 50, 51, 52, 53, 54, 56, 57, 58, 59, 60, 62, 63, 64, 65, 66, 67, 69], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
from ansible.module_utils.facts.timeout import TimeoutError

@pytest.fixture
def hardware():
    return FreeBSDHardware(module=MagicMock())

def test_populate_all_facts(hardware):
    with patch.object(hardware, 'get_cpu_facts', return_value={'cpu': 'test_cpu'}), \
         patch.object(hardware, 'get_memory_facts', return_value={'memory': 'test_memory'}), \
         patch.object(hardware, 'get_uptime_facts', return_value={'uptime': 'test_uptime'}), \
         patch.object(hardware, 'get_dmi_facts', return_value={'dmi': 'test_dmi'}), \
         patch.object(hardware, 'get_device_facts', return_value={'device': 'test_device'}), \
         patch.object(hardware, 'get_mount_facts', return_value={'mount': 'test_mount'}):
        
        facts = hardware.populate()
        
        assert facts['cpu'] == 'test_cpu'
        assert facts['memory'] == 'test_memory'
        assert facts['uptime'] == 'test_uptime'
        assert facts['dmi'] == 'test_dmi'
        assert facts['device'] == 'test_device'
        assert facts['mount'] == 'test_mount'

def test_populate_mount_facts_timeout(hardware):
    with patch.object(hardware, 'get_cpu_facts', return_value={'cpu': 'test_cpu'}), \
         patch.object(hardware, 'get_memory_facts', return_value={'memory': 'test_memory'}), \
         patch.object(hardware, 'get_uptime_facts', return_value={'uptime': 'test_uptime'}), \
         patch.object(hardware, 'get_dmi_facts', return_value={'dmi': 'test_dmi'}), \
         patch.object(hardware, 'get_device_facts', return_value={'device': 'test_device'}), \
         patch.object(hardware, 'get_mount_facts', side_effect=TimeoutError):
        
        facts = hardware.populate()
        
        assert facts['cpu'] == 'test_cpu'
        assert facts['memory'] == 'test_memory'
        assert facts['uptime'] == 'test_uptime'
        assert facts['dmi'] == 'test_dmi'
        assert facts['device'] == 'test_device'
        assert 'mount' not in facts
