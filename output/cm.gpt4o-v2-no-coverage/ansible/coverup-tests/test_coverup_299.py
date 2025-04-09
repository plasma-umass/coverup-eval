# file: lib/ansible/module_utils/facts/hardware/hurd.py:24-48
# asked: {"lines": [24, 25, 31, 33, 34, 35, 36, 38, 39, 40, 41, 42, 44, 45, 46, 48], "branches": []}
# gained: {"lines": [24, 25, 31, 33, 34, 35, 36, 38, 39, 40, 41, 42, 44, 45, 46, 48], "branches": []}

import pytest
from unittest.mock import patch
from ansible.module_utils.facts.hardware.hurd import HurdHardware
from ansible.module_utils.facts.timeout import TimeoutError

@pytest.fixture
def hurd_hardware():
    module = None  # Replace with an appropriate mock or instance if needed
    return HurdHardware(module)

def test_populate_success(hurd_hardware):
    with patch.object(hurd_hardware, 'get_uptime_facts', return_value={'uptime': '100 days'}), \
         patch.object(hurd_hardware, 'get_memory_facts', return_value={'memtotal_mb': 1024}), \
         patch.object(hurd_hardware, 'get_mount_facts', return_value={'mounts': []}):
        result = hurd_hardware.populate()
        assert result == {'uptime': '100 days', 'memtotal_mb': 1024, 'mounts': []}

def test_populate_timeout_error(hurd_hardware):
    with patch.object(hurd_hardware, 'get_uptime_facts', return_value={'uptime': '100 days'}), \
         patch.object(hurd_hardware, 'get_memory_facts', return_value={'memtotal_mb': 1024}), \
         patch.object(hurd_hardware, 'get_mount_facts', side_effect=TimeoutError):
        result = hurd_hardware.populate()
        assert result == {'uptime': '100 days', 'memtotal_mb': 1024}
