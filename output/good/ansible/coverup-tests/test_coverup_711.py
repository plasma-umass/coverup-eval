# file lib/ansible/module_utils/facts/system/service_mgr.py:38-42
# lines [38, 39, 40, 41]
# branches []

import pytest
from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector
from ansible.module_utils.facts.collector import BaseFactCollector

# Mocking the BaseFactCollector to avoid side effects on the actual system
class MockBaseFactCollector(BaseFactCollector):
    def collect(self, module=None, collected_facts=None):
        return {}

@pytest.fixture
def service_mgr_fact_collector(mocker):
    mocker.patch('ansible.module_utils.facts.system.service_mgr.BaseFactCollector', new=MockBaseFactCollector)
    return ServiceMgrFactCollector()

def test_service_mgr_fact_collector(service_mgr_fact_collector):
    assert service_mgr_fact_collector.name == 'service_mgr'
    assert service_mgr_fact_collector._fact_ids == set()
    assert service_mgr_fact_collector.required_facts == set(['platform', 'distribution'])

    # Simulate collecting facts
    collected_facts = service_mgr_fact_collector.collect()
    assert isinstance(collected_facts, dict)
