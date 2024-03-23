# file lib/ansible/module_utils/facts/namespace.py:32-41
# lines [32, 33, 34, 36, 38, 40, 41]
# branches []

import pytest
from ansible.module_utils.facts.namespace import FactNamespace

def test_fact_namespace_transform():
    ns = FactNamespace('test_ns')
    transformed_name = ns.transform('some-name')
    assert transformed_name == 'some-name', "The transform method should return the original name"

def test_fact_namespace_underscore():
    ns = FactNamespace('test_ns')
    underscored_name = ns._underscore('some-name')
    assert underscored_name == 'some_name', "The _underscore method should replace hyphens with underscores"
