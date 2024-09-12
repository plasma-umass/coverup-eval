# file: lib/ansible/module_utils/facts/other/facter.py:30-34
# asked: {"lines": [30, 31, 32, 33, 34], "branches": []}
# gained: {"lines": [30, 31, 32, 33, 34], "branches": []}

import pytest
from ansible.module_utils.facts.other.facter import FacterFactCollector
from ansible.module_utils.facts.collector import BaseFactCollector
from ansible.module_utils.facts.namespace import PrefixFactNamespace

def test_facter_fact_collector_initialization(monkeypatch):
    class MockBaseFactCollector:
        def __init__(self, collectors=None, namespace=None):
            self.collectors = collectors
            self.namespace = namespace

    monkeypatch.setattr('ansible.module_utils.facts.other.facter.BaseFactCollector', MockBaseFactCollector)
    monkeypatch.setattr('ansible.module_utils.facts.other.facter.PrefixFactNamespace', PrefixFactNamespace)

    collectors = ['collector1', 'collector2']
    namespace_name = 'custom_namespace'
    facter_collector = FacterFactCollector(collectors=collectors, namespace=namespace_name)

    assert facter_collector.collectors == collectors
    assert isinstance(facter_collector.namespace, PrefixFactNamespace)
    assert facter_collector.namespace.namespace_name == 'facter'
    assert facter_collector.namespace.prefix == 'facter_'
