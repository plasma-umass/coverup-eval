# file: lib/ansible/module_utils/facts/ansible_collector.py:49-54
# asked: {"lines": [49, 51, 52, 54], "branches": []}
# gained: {"lines": [49, 51, 52, 54], "branches": []}

import pytest
from ansible.module_utils.facts.ansible_collector import AnsibleFactCollector
from ansible.module_utils.facts.collector import BaseFactCollector

def test_ansible_fact_collector_init():
    # Test with no parameters
    afc = AnsibleFactCollector()
    assert afc.collectors == []
    assert afc.namespace is None
    assert afc.filter_spec is None

    # Test with collectors parameter
    collectors = [BaseFactCollector()]
    afc = AnsibleFactCollector(collectors=collectors)
    assert afc.collectors == collectors
    assert afc.namespace is None
    assert afc.filter_spec is None

    # Test with namespace parameter
    namespace = 'test_namespace'
    afc = AnsibleFactCollector(namespace=namespace)
    assert afc.collectors == []
    assert afc.namespace == namespace
    assert afc.filter_spec is None

    # Test with filter_spec parameter
    filter_spec = 'test_filter'
    afc = AnsibleFactCollector(filter_spec=filter_spec)
    assert afc.collectors == []
    assert afc.namespace is None
    assert afc.filter_spec == filter_spec

    # Test with all parameters
    afc = AnsibleFactCollector(collectors=collectors, namespace=namespace, filter_spec=filter_spec)
    assert afc.collectors == collectors
    assert afc.namespace == namespace
    assert afc.filter_spec == filter_spec
