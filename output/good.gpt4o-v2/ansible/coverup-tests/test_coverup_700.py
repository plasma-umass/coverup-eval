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
    
    afc = AnsibleFactCollector(collectors=collectors, namespace=namespace, filter_spec=filter_spec)
    
    assert afc.collectors == collectors
    assert afc.namespace == namespace
    assert afc.filter_spec == filter_spec
