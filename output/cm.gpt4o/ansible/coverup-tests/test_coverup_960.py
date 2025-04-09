# file lib/ansible/module_utils/facts/ansible_collector.py:40-48
# lines [40, 41]
# branches []

import pytest
from unittest import mock
from ansible.module_utils.facts.ansible_collector import AnsibleFactCollector
from ansible.module_utils.facts.collector import BaseFactCollector

def test_ansible_fact_collector_initialization():
    # Test initialization without namespace
    collector = AnsibleFactCollector()
    assert isinstance(collector, BaseFactCollector)
    assert collector.namespace is None

    # Test initialization with namespace
    mock_namespace = mock.Mock()
    collector_with_namespace = AnsibleFactCollector(namespace=mock_namespace)
    assert collector_with_namespace.namespace == mock_namespace

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Clean up any necessary state here
