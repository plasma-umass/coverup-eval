# file: lib/ansible/module_utils/facts/ansible_collector.py:121-156
# asked: {"lines": [128, 129, 130, 131, 133, 134, 135, 136, 137, 138, 140, 141, 142, 143, 146, 147, 148, 149, 151, 152, 153, 154, 156], "branches": [[141, 142], [141, 146]]}
# gained: {"lines": [128, 129, 130, 131, 133, 134, 135, 136, 137, 138, 140, 141, 142, 143, 146, 147, 148, 149, 151, 152, 153, 154, 156], "branches": [[141, 142], [141, 146]]}

import pytest
from unittest.mock import MagicMock, patch

# Assuming the following classes and methods are defined in the module
# from ansible.module_utils.facts.ansible_collector import (
#     get_ansible_collector, CollectorMetaDataCollector, AnsibleFactCollector, collector, timeout
# )

class MockCollector:
    def __init__(self, namespace=None):
        self.namespace = namespace

class MockCollectorMetaDataCollector:
    def __init__(self, gather_subset, module_setup):
        self.gather_subset = gather_subset
        self.module_setup = module_setup

class MockAnsibleFactCollector:
    def __init__(self, collectors, filter_spec, namespace):
        self.collectors = collectors
        self.filter_spec = filter_spec
        self.namespace = namespace

@pytest.fixture
def mock_collector_classes():
    return [MockCollector]

@pytest.fixture
def mock_collector_meta_data_collector(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.facts.ansible_collector.CollectorMetaDataCollector', MockCollectorMetaDataCollector)

@pytest.fixture
def mock_ansible_fact_collector(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.facts.ansible_collector.AnsibleFactCollector', MockAnsibleFactCollector)

@pytest.fixture
def mock_collector(monkeypatch):
    mock_collector_classes_from_gather_subset = MagicMock(return_value=[MockCollector])
    monkeypatch.setattr('ansible.module_utils.facts.ansible_collector.collector.collector_classes_from_gather_subset', mock_collector_classes_from_gather_subset)
    return mock_collector_classes_from_gather_subset

@pytest.fixture
def mock_timeout(monkeypatch):
    mock_default_gather_timeout = 10
    monkeypatch.setattr('ansible.module_utils.facts.ansible_collector.timeout.DEFAULT_GATHER_TIMEOUT', mock_default_gather_timeout)
    return mock_default_gather_timeout

def test_get_ansible_collector_defaults(mock_collector_classes, mock_collector_meta_data_collector, mock_ansible_fact_collector, mock_collector, mock_timeout):
    from ansible.module_utils.facts.ansible_collector import get_ansible_collector

    fact_collector = get_ansible_collector(mock_collector_classes)

    assert isinstance(fact_collector, MockAnsibleFactCollector)
    assert len(fact_collector.collectors) == 2
    assert isinstance(fact_collector.collectors[0], MockCollector)
    assert isinstance(fact_collector.collectors[1], MockCollectorMetaDataCollector)
    assert fact_collector.collectors[1].gather_subset == ['all']
    assert fact_collector.collectors[1].module_setup is True
    assert fact_collector.filter_spec == []
    assert fact_collector.namespace is None

def test_get_ansible_collector_custom_params(mock_collector_classes, mock_collector_meta_data_collector, mock_ansible_fact_collector, mock_collector, mock_timeout):
    from ansible.module_utils.facts.ansible_collector import get_ansible_collector

    fact_collector = get_ansible_collector(
        mock_collector_classes,
        namespace='test_namespace',
        filter_spec=['test_filter'],
        gather_subset=['test_subset'],
        gather_timeout=5,
        minimal_gather_subset=frozenset(['test_minimal'])
    )

    assert isinstance(fact_collector, MockAnsibleFactCollector)
    assert len(fact_collector.collectors) == 2
    assert isinstance(fact_collector.collectors[0], MockCollector)
    assert isinstance(fact_collector.collectors[1], MockCollectorMetaDataCollector)
    assert fact_collector.collectors[1].gather_subset == ['test_subset']
    assert fact_collector.collectors[1].module_setup is True
    assert fact_collector.filter_spec == ['test_filter']
    assert fact_collector.namespace == 'test_namespace'
