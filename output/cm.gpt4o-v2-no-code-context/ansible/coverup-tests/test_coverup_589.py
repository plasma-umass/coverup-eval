# file: lib/ansible/module_utils/facts/collector.py:65-76
# asked: {"lines": [65, 69, 73, 75, 76], "branches": []}
# gained: {"lines": [65, 69, 73, 75, 76], "branches": []}

import pytest
from unittest.mock import Mock

# Assuming the BaseFactCollector class is defined in ansible/module_utils/facts/collector.py
from ansible.module_utils.facts.collector import BaseFactCollector

class TestBaseFactCollector:
    
    def test_init_with_collectors(self):
        mock_collector = Mock()
        collectors = [mock_collector]
        collector = BaseFactCollector(collectors=collectors)
        
        assert collector.collectors == collectors

    def test_init_without_collectors(self):
        collector = BaseFactCollector()
        
        assert collector.collectors == []

    def test_init_with_namespace(self):
        mock_namespace = Mock()
        collector = BaseFactCollector(namespace=mock_namespace)
        
        assert collector.namespace == mock_namespace

    def test_init_fact_ids(self, monkeypatch):
        mock_name = 'test_name'
        mock_fact_ids = {'fact1', 'fact2'}
        
        # Mocking the name and _fact_ids attributes
        monkeypatch.setattr(BaseFactCollector, 'name', mock_name)
        monkeypatch.setattr(BaseFactCollector, '_fact_ids', mock_fact_ids)
        
        collector = BaseFactCollector()
        
        assert collector.fact_ids == {mock_name, 'fact1', 'fact2'}
