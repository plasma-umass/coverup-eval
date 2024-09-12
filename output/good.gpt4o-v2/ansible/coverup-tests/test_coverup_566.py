# file: lib/ansible/module_utils/facts/collector.py:99-104
# asked: {"lines": [99, 101, 102, 103, 104], "branches": [[102, 103], [102, 104]]}
# gained: {"lines": [99, 101, 102, 103, 104], "branches": [[102, 103], [102, 104]]}

import pytest
from ansible.module_utils.facts.collector import BaseFactCollector

class TestBaseFactCollector:
    
    @pytest.fixture
    def collector(self):
        class TestCollector(BaseFactCollector):
            def __init__(self, namespace=None):
                self.namespace = namespace
            
            def collect(self, module=None, collected_facts=None):
                return {'old_key': 'value'}
            
            def _transform_name(self, name):
                return f'new_{name}'
        
        return TestCollector()
    
    def test_collect_with_namespace_no_namespace(self, collector):
        result = collector.collect_with_namespace()
        assert result == {'old_key': 'value'}
    
    def test_collect_with_namespace_with_namespace(self, collector):
        collector.namespace = True
        result = collector.collect_with_namespace()
        assert result == {'new_old_key': 'value'}
