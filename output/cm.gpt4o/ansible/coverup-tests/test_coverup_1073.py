# file lib/ansible/module_utils/facts/ansible_collector.py:121-156
# lines [128, 129, 130, 131, 133, 134, 135, 136, 137, 138, 140, 141, 142, 143, 146, 147, 148, 149, 151, 152, 153, 154, 156]
# branches ['141->142', '141->146']

import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils.facts.ansible_collector import get_ansible_collector

@pytest.fixture
def mock_collector_classes():
    class MockCollector:
        def __init__(self, namespace=None):
            self.namespace = namespace

    return [MockCollector]

@pytest.fixture
def mock_collector_meta_data_collector():
    class MockCollectorMetaDataCollector:
        def __init__(self, gather_subset, module_setup):
            self.gather_subset = gather_subset
            self.module_setup = module_setup

    return MockCollectorMetaDataCollector

@pytest.fixture
def mock_ansible_fact_collector():
    class MockAnsibleFactCollector:
        def __init__(self, collectors, filter_spec, namespace):
            self.collectors = collectors
            self.filter_spec = filter_spec
            self.namespace = namespace

    return MockAnsibleFactCollector

@patch('ansible.module_utils.facts.ansible_collector.collector.collector_classes_from_gather_subset')
def test_get_ansible_collector(mock_collector_classes_from_gather_subset, mock_collector_classes, mock_collector_meta_data_collector, mock_ansible_fact_collector):
    mock_collector_classes_from_gather_subset.return_value = mock_collector_classes

    filter_spec = ['some_filter']
    namespace = 'some_namespace'
    gather_subset = ['some_subset']
    gather_timeout = 10
    minimal_gather_subset = frozenset(['some_minimal_subset'])

    with patch('ansible.module_utils.facts.ansible_collector.CollectorMetaDataCollector', mock_collector_meta_data_collector), \
         patch('ansible.module_utils.facts.ansible_collector.AnsibleFactCollector', mock_ansible_fact_collector):

        fact_collector = get_ansible_collector(
            all_collector_classes=mock_collector_classes,
            namespace=namespace,
            filter_spec=filter_spec,
            gather_subset=gather_subset,
            gather_timeout=gather_timeout,
            minimal_gather_subset=minimal_gather_subset
        )

        assert fact_collector.collectors[0].namespace == namespace
        assert fact_collector.collectors[1].gather_subset == gather_subset
        assert fact_collector.collectors[1].module_setup is True
        assert fact_collector.filter_spec == filter_spec
        assert fact_collector.namespace == namespace
