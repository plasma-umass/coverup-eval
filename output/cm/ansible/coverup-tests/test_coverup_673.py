# file lib/ansible/module_utils/facts/other/facter.py:30-34
# lines [30, 31, 32, 33, 34]
# branches []

import pytest
from ansible.module_utils.facts.other.facter import FacterFactCollector
from ansible.module_utils.facts.namespace import PrefixFactNamespace

# Mocking the BaseFactCollector since we only want to test the FacterFactCollector
class MockBaseFactCollector:
    def __init__(self, collectors=None, namespace=None):
        self.collectors = collectors
        self.namespace = namespace

@pytest.fixture
def mock_base_fact_collector(mocker):
    mocker.patch('ansible.module_utils.facts.other.facter.BaseFactCollector', new=MockBaseFactCollector)

def test_facter_fact_collector_initialization(mock_base_fact_collector):
    # Test the initialization of FacterFactCollector
    facter_fact_collector = FacterFactCollector()
    assert isinstance(facter_fact_collector.namespace, PrefixFactNamespace)
    assert facter_fact_collector.namespace.namespace_name == 'facter'
    assert facter_fact_collector.namespace.prefix == 'facter_'
