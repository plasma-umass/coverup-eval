# file: lib/ansible/module_utils/facts/ansible_collector.py:49-54
# asked: {"lines": [49, 51, 52, 54], "branches": []}
# gained: {"lines": [49, 51, 52, 54], "branches": []}

import pytest
from ansible.module_utils.facts.ansible_collector import AnsibleFactCollector
from ansible.module_utils.facts.collector import BaseFactCollector

def test_ansible_fact_collector_init():
    collectors = [BaseFactCollector()]
    namespace = 'test_namespace'
    filter_spec = 'test_filter_spec'
    
    fact_collector = AnsibleFactCollector(collectors=collectors, namespace=namespace, filter_spec=filter_spec)
    
    assert fact_collector.collectors == collectors
    assert fact_collector.namespace == namespace
    assert fact_collector.filter_spec == filter_spec
