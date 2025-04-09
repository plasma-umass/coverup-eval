# file: lib/ansible/module_utils/facts/collector.py:84-87
# asked: {"lines": [85, 86, 87], "branches": [[85, 86], [85, 87]]}
# gained: {"lines": [85, 86, 87], "branches": [[85, 86], [85, 87]]}

import pytest

class MockNamespace:
    def transform(self, key_name):
        return f"transformed_{key_name}"

@pytest.fixture
def base_fact_collector_with_namespace():
    from ansible.module_utils.facts.collector import BaseFactCollector
    return BaseFactCollector(namespace=MockNamespace())

@pytest.fixture
def base_fact_collector_without_namespace():
    from ansible.module_utils.facts.collector import BaseFactCollector
    return BaseFactCollector(namespace=None)

def test_transform_name_with_namespace(base_fact_collector_with_namespace):
    result = base_fact_collector_with_namespace._transform_name("test_key")
    assert result == "transformed_test_key"

def test_transform_name_without_namespace(base_fact_collector_without_namespace):
    result = base_fact_collector_without_namespace._transform_name("test_key")
    assert result == "test_key"
