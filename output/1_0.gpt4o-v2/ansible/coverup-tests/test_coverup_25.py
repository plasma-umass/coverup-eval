# file: lib/ansible/module_utils/facts/namespace.py:32-41
# asked: {"lines": [32, 33, 34, 36, 38, 40, 41], "branches": []}
# gained: {"lines": [32, 33, 34, 36, 38, 40, 41], "branches": []}

import pytest
from ansible.module_utils.facts.namespace import FactNamespace

@pytest.fixture
def fact_namespace():
    return FactNamespace("test_namespace")

def test_transform(fact_namespace):
    name = "example"
    transformed_name = fact_namespace.transform(name)
    assert transformed_name == name

def test_underscore(fact_namespace):
    name = "example-name"
    underscored_name = fact_namespace._underscore(name)
    assert underscored_name == "example_name"
