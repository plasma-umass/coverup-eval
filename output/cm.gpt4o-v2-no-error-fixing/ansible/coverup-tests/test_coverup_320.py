# file: lib/ansible/module_utils/facts/hardware/hpux.py:41-52
# asked: {"lines": [41, 42, 44, 45, 46, 48, 49, 50, 52], "branches": []}
# gained: {"lines": [41, 42, 44, 45, 46, 48, 49, 50, 52], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.hardware.hpux import HPUXHardware

@pytest.fixture
def hpux_hardware():
    return HPUXHardware(module=MagicMock())

def test_populate_all_branches(hpux_hardware, monkeypatch):
    # Mock the methods to return specific values
    def mock_get_cpu_facts(collected_facts=None):
        return {'processor_count': 4, 'processor_cores': 2, 'processor': 'Intel'}

    def mock_get_memory_facts(collected_facts=None):
        return {'memfree_mb': 1024, 'memtotal_mb': 8192, 'swapfree_mb': 2048, 'swaptotal_mb': 4096}

    def mock_get_hw_facts(collected_facts=None):
        return {'model': 'HP-UX', 'firmware_version': '1.0', 'product_serial': '12345'}

    monkeypatch.setattr(hpux_hardware, 'get_cpu_facts', mock_get_cpu_facts)
    monkeypatch.setattr(hpux_hardware, 'get_memory_facts', mock_get_memory_facts)
    monkeypatch.setattr(hpux_hardware, 'get_hw_facts', mock_get_hw_facts)

    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.31'}
    result = hpux_hardware.populate(collected_facts=collected_facts)

    expected_result = {
        'processor_count': 4,
        'processor_cores': 2,
        'processor': 'Intel',
        'memfree_mb': 1024,
        'memtotal_mb': 8192,
        'swapfree_mb': 2048,
        'swaptotal_mb': 4096,
        'model': 'HP-UX',
        'firmware_version': '1.0',
        'product_serial': '12345'
    }

    assert result == expected_result
