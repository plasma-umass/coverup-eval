# file: lib/ansible/module_utils/facts/hardware/base.py:46-66
# asked: {"lines": [46, 47, 48, 54, 56, 57, 58, 59, 62, 64, 66], "branches": [[58, 59], [58, 62]]}
# gained: {"lines": [46, 47, 48, 54, 56, 57, 58, 59, 62, 64, 66], "branches": [[58, 59], [58, 62]]}

import pytest
from ansible.module_utils.facts.hardware.base import HardwareCollector, Hardware
from ansible.module_utils.facts.collector import BaseFactCollector

class MockModule:
    pass

class MockHardware(Hardware):
    def populate(self, collected_facts=None):
        collected_facts = collected_facts or {}
        collected_facts.update({
            'processor': 'Intel',
            'processor_cores': 4,
            'processor_count': 1,
            'mounts': '/mnt',
            'devices': '/dev/sda'
        })
        return collected_facts

@pytest.fixture
def mock_hardware(monkeypatch):
    def mock_init(self, module, load_on_init=False):
        self.module = module

    monkeypatch.setattr(Hardware, '__init__', mock_init)
    monkeypatch.setattr(Hardware, 'populate', MockHardware.populate)

def test_hardware_collector_collect(mock_hardware):
    collector = HardwareCollector()
    module = MockModule()
    collected_facts = {'existing_fact': 'value'}

    result = collector.collect(module=module, collected_facts=collected_facts)

    assert 'processor' in result
    assert result['processor'] == 'Intel'
    assert 'processor_cores' in result
    assert result['processor_cores'] == 4
    assert 'processor_count' in result
    assert result['processor_count'] == 1
    assert 'mounts' in result
    assert result['mounts'] == '/mnt'
    assert 'devices' in result
    assert result['devices'] == '/dev/sda'
    assert 'existing_fact' in result
    assert result['existing_fact'] == 'value'

def test_hardware_collector_collect_no_module(mock_hardware):
    collector = HardwareCollector()
    result = collector.collect(module=None, collected_facts={'existing_fact': 'value'})

    assert result == {}
