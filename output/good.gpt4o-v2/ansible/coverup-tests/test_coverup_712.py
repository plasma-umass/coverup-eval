# file: lib/ansible/module_utils/facts/other/facter.py:30-34
# asked: {"lines": [30, 31, 32, 33, 34], "branches": []}
# gained: {"lines": [30, 31, 32, 33, 34], "branches": []}

import pytest
from ansible.module_utils.facts.other.facter import FacterFactCollector
from ansible.module_utils.facts.namespace import PrefixFactNamespace
from ansible.module_utils.facts.collector import BaseFactCollector

def test_facter_fact_collector_init(monkeypatch):
    # Mock the PrefixFactNamespace to return the custom namespace when provided
    def mock_init(self, namespace_name, prefix=None):
        self.namespace_name = namespace_name
        self.prefix = prefix

    monkeypatch.setattr(PrefixFactNamespace, "__init__", mock_init)

    # Test with default parameters
    collector = FacterFactCollector()
    assert isinstance(collector.namespace, PrefixFactNamespace)
    assert collector.namespace.prefix == 'facter_'
    assert collector.namespace.namespace_name == 'facter'

    # Test with custom collectors
    custom_collectors = ['collector1', 'collector2']
    collector = FacterFactCollector(collectors=custom_collectors)
    assert collector.collectors == custom_collectors
    assert isinstance(collector.namespace, PrefixFactNamespace)
    assert collector.namespace.prefix == 'facter_'
    assert collector.namespace.namespace_name == 'facter'

    # Test with custom namespace
    custom_namespace = PrefixFactNamespace(namespace_name='custom', prefix='custom_')
    collector = FacterFactCollector(namespace=custom_namespace)
    assert collector.namespace.prefix == 'facter_'
    assert collector.namespace.namespace_name == 'facter'
