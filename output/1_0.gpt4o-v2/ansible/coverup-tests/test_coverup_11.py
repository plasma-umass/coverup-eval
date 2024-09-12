# file: lib/ansible/module_utils/facts/namespace.py:44-51
# asked: {"lines": [44, 45, 46, 47, 49, 50, 51], "branches": []}
# gained: {"lines": [44, 45, 46, 47, 49, 50, 51], "branches": []}

import pytest
from ansible.module_utils.facts.namespace import PrefixFactNamespace, FactNamespace

class MockFactNamespace(FactNamespace):
    def _underscore(self, name):
        return name.replace(' ', '_')

@pytest.fixture
def mock_fact_namespace(monkeypatch):
    monkeypatch.setattr(PrefixFactNamespace, '_underscore', MockFactNamespace._underscore)

def test_prefix_fact_namespace_init():
    namespace = PrefixFactNamespace('test_namespace', 'prefix_')
    assert namespace.namespace_name == 'test_namespace'
    assert namespace.prefix == 'prefix_'

def test_prefix_fact_namespace_transform(mock_fact_namespace):
    namespace = PrefixFactNamespace('test_namespace', 'prefix_')
    transformed_name = namespace.transform('test name')
    assert transformed_name == 'prefix_test_name'
