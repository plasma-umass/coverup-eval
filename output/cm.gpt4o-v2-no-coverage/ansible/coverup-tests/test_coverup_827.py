# file: lib/ansible/module_utils/facts/virtual/hpux.py:70-72
# asked: {"lines": [70, 71, 72], "branches": []}
# gained: {"lines": [70, 71, 72], "branches": []}

import pytest
from ansible.module_utils.facts.virtual.hpux import HPUXVirtualCollector
from ansible.module_utils.facts.virtual.base import VirtualCollector

class MockHPUXVirtual:
    pass

@pytest.fixture
def mock_hpux_virtual(monkeypatch):
    monkeypatch.setattr(HPUXVirtualCollector, '_fact_class', MockHPUXVirtual)

def test_hpux_virtual_collector_init(mock_hpux_virtual):
    collector = HPUXVirtualCollector()
    assert collector._fact_class == MockHPUXVirtual
    assert collector._platform == 'HP-UX'
    assert isinstance(collector, VirtualCollector)
