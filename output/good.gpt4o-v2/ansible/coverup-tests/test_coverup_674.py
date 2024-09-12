# file: lib/ansible/module_utils/facts/collector.py:65-76
# asked: {"lines": [65, 69, 73, 75, 76], "branches": []}
# gained: {"lines": [65, 69, 73, 75, 76], "branches": []}

import pytest
from ansible.module_utils.facts.collector import BaseFactCollector

def test_base_fact_collector_init_with_collectors():
    collectors = [BaseFactCollector(), BaseFactCollector()]
    collector = BaseFactCollector(collectors=collectors)
    assert collector.collectors == collectors
    assert collector.namespace is None
    assert collector.fact_ids == {None}

def test_base_fact_collector_init_with_namespace():
    class Namespace:
        def transform(self, name):
            return f"namespace_{name}"

    namespace = Namespace()
    collector = BaseFactCollector(namespace=namespace)
    assert collector.collectors == []
    assert collector.namespace == namespace
    assert collector.fact_ids == {None}

def test_base_fact_collector_init_with_fact_ids():
    class CustomFactCollector(BaseFactCollector):
        _fact_ids = {'custom_fact'}
        name = 'custom_collector'

    collector = CustomFactCollector()
    assert collector.collectors == []
    assert collector.namespace is None
    assert collector.fact_ids == {'custom_collector', 'custom_fact'}
