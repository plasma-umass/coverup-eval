# file: lib/ansible/module_utils/facts/compat.py:49-87
# asked: {"lines": [49, 63, 64, 65, 67, 72, 75, 77, 78, 79, 80, 81, 82, 83, 85, 87], "branches": []}
# gained: {"lines": [49, 63, 64, 65, 67, 72, 75, 77, 78, 79, 80, 81, 82, 83, 85, 87], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils.facts.compat import ansible_facts
from ansible.module_utils.facts.namespace import PrefixFactNamespace
from ansible.module_utils.facts import default_collectors
from ansible.module_utils.facts.ansible_collector import get_ansible_collector

@pytest.fixture
def mock_module():
    module = MagicMock()
    module.params = {
        'gather_subset': ['all'],
        'gather_timeout': 10,
        'filter': '*'
    }
    return module

def test_ansible_facts_all(mock_module):
    with patch('ansible.module_utils.facts.ansible_collector.get_ansible_collector') as mock_get_collector:
        mock_collector = MagicMock()
        mock_collector.collect.return_value = {'fact1': 'value1'}
        mock_get_collector.return_value = mock_collector

        facts = ansible_facts(mock_module)

        assert facts == {'fact1': 'value1'}
        mock_get_collector.assert_called_once()
        mock_collector.collect.assert_called_once_with(module=mock_module)

def test_ansible_facts_custom_subset(mock_module):
    mock_module.params['gather_subset'] = ['custom']
    with patch('ansible.module_utils.facts.ansible_collector.get_ansible_collector') as mock_get_collector:
        mock_collector = MagicMock()
        mock_collector.collect.return_value = {'fact2': 'value2'}
        mock_get_collector.return_value = mock_collector

        facts = ansible_facts(mock_module, gather_subset=['custom'])

        assert facts == {'fact2': 'value2'}
        mock_get_collector.assert_called_once()
        mock_collector.collect.assert_called_once_with(module=mock_module)

def test_ansible_facts_no_subset(mock_module):
    mock_module.params.pop('gather_subset')
    with patch('ansible.module_utils.facts.ansible_collector.get_ansible_collector') as mock_get_collector:
        mock_collector = MagicMock()
        mock_collector.collect.return_value = {'fact3': 'value3'}
        mock_get_collector.return_value = mock_collector

        facts = ansible_facts(mock_module)

        assert facts == {'fact3': 'value3'}
        mock_get_collector.assert_called_once()
        mock_collector.collect.assert_called_once_with(module=mock_module)
