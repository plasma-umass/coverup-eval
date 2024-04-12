# file lib/ansible/module_utils/facts/compat.py:49-87
# lines [49, 63, 64, 65, 67, 72, 75, 77, 78, 79, 80, 81, 82, 83, 85, 87]
# branches []

import pytest
from ansible.module_utils.facts import compat
from ansible.module_utils import basic
from ansible.module_utils.facts.namespace import PrefixFactNamespace
from ansible.module_utils.facts import default_collectors

@pytest.fixture
def mock_module(mocker):
    mock_module = mocker.MagicMock()
    mock_module.params = {
        'gather_subset': ['all'],
        'gather_timeout': 10,
        'filter': '*'
    }
    return mock_module

@pytest.fixture
def mock_fact_collector(mocker):
    fact_collector = mocker.MagicMock()
    fact_collector.collect = mocker.MagicMock(return_value={})
    mocker.patch('ansible.module_utils.facts.ansible_collector.get_ansible_collector', return_value=fact_collector)
    return fact_collector

def test_ansible_facts_with_gather_subset(mock_module, mock_fact_collector):
    facts = compat.ansible_facts(mock_module, gather_subset=['network'])
    mock_fact_collector.collect.assert_called_once_with(module=mock_module)
    assert isinstance(facts, dict)

def test_ansible_facts_without_gather_subset(mock_module, mock_fact_collector):
    facts = compat.ansible_facts(mock_module)
    mock_fact_collector.collect.assert_called_once_with(module=mock_module)
    assert isinstance(facts, dict)
