# file: lib/ansible/module_utils/facts/ansible_collector.py:49-54
# asked: {"lines": [49, 51, 52, 54], "branches": []}
# gained: {"lines": [49, 51, 52, 54], "branches": []}

import pytest
from ansible.module_utils.facts.ansible_collector import AnsibleFactCollector
from ansible.module_utils.facts.collector import BaseFactCollector

def test_ansible_fact_collector_init_with_params():
    collectors = ['collector1', 'collector2']
    namespace = 'test_namespace'
    filter_spec = 'test_filter_spec'
    
    collector = AnsibleFactCollector(collectors=collectors, namespace=namespace, filter_spec=filter_spec)
    
    assert collector.collectors == collectors
    assert collector.namespace == namespace
    assert collector.filter_spec == filter_spec

def test_ansible_fact_collector_init_without_params():
    collector = AnsibleFactCollector()
    
    assert collector.collectors == []
    assert collector.namespace is None
    assert collector.filter_spec is None
