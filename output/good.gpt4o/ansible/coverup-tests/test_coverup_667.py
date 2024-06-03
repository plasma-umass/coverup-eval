# file lib/ansible/module_utils/facts/system/service_mgr.py:38-42
# lines [38, 39, 40, 41]
# branches []

import pytest
from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector
from ansible.module_utils.facts.collector import BaseFactCollector

def test_service_mgr_fact_collector_initialization():
    collector = ServiceMgrFactCollector()
    assert collector.name == 'service_mgr'
    assert collector._fact_ids == set()
    assert collector.required_facts == set(['platform', 'distribution'])

def test_service_mgr_fact_collector_inheritance():
    collector = ServiceMgrFactCollector()
    assert isinstance(collector, BaseFactCollector)
