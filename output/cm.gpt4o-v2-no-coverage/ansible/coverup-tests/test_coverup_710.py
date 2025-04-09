# file: lib/ansible/module_utils/facts/collector.py:65-76
# asked: {"lines": [65, 69, 73, 75, 76], "branches": []}
# gained: {"lines": [65, 69, 73, 75, 76], "branches": []}

import pytest
from ansible.module_utils.facts.collector import BaseFactCollector

class MockNamespace:
    def transform(self, name):
        return f"namespace_{name}"

class TestBaseFactCollector:
    def test_init_no_collectors_no_namespace(self):
        collector = BaseFactCollector()
        assert collector.collectors == []
        assert collector.namespace is None
        assert collector.fact_ids == {None}

    def test_init_with_collectors(self):
        mock_collectors = [BaseFactCollector(), BaseFactCollector()]
        collector = BaseFactCollector(collectors=mock_collectors)
        assert collector.collectors == mock_collectors
        assert collector.namespace is None
        assert collector.fact_ids == {None}

    def test_init_with_namespace(self):
        mock_namespace = MockNamespace()
        collector = BaseFactCollector(namespace=mock_namespace)
        assert collector.collectors == []
        assert collector.namespace == mock_namespace
        assert collector.fact_ids == {None}

    def test_init_with_collectors_and_namespace(self):
        mock_collectors = [BaseFactCollector(), BaseFactCollector()]
        mock_namespace = MockNamespace()
        collector = BaseFactCollector(collectors=mock_collectors, namespace=mock_namespace)
        assert collector.collectors == mock_collectors
        assert collector.namespace == mock_namespace
        assert collector.fact_ids == {None}
