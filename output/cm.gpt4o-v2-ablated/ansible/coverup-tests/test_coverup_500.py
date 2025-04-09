# file: lib/ansible/module_utils/facts/compat.py:49-87
# asked: {"lines": [63, 64, 65, 67, 72, 75, 77, 78, 79, 80, 81, 82, 83, 85, 87], "branches": []}
# gained: {"lines": [63, 64, 65, 67, 72, 75, 77, 78, 79, 80, 81, 82, 83, 85, 87], "branches": []}

import pytest
from unittest.mock import MagicMock, patch

# Assuming the necessary imports from ansible.module_utils.facts.compat
# from ansible.module_utils.facts.compat import ansible_facts
# from ansible.module_utils.facts.collector import default_collectors, ansible_collector, PrefixFactNamespace

@pytest.fixture
def mock_module():
    module = MagicMock()
    module.params = {
        'gather_subset': ['all'],
        'gather_timeout': 10,
        'filter': '*'
    }
    return module

@pytest.fixture
def mock_collectors():
    with patch('ansible.module_utils.facts.compat.default_collectors') as mock_default_collectors:
        mock_default_collectors.collectors = ['collector1', 'collector2']
        yield mock_default_collectors

@pytest.fixture
def mock_ansible_collector():
    with patch('ansible.module_utils.facts.compat.ansible_collector') as mock_ansible_collector:
        mock_collector_instance = MagicMock()
        mock_collector_instance.collect.return_value = {'fact1': 'value1', 'fact2': 'value2'}
        mock_ansible_collector.get_ansible_collector.return_value = mock_collector_instance
        yield mock_ansible_collector

def test_ansible_facts_default(mock_module, mock_collectors, mock_ansible_collector):
    from ansible.module_utils.facts.compat import ansible_facts

    result = ansible_facts(mock_module)
    assert result == {'fact1': 'value1', 'fact2': 'value2'}
    mock_ansible_collector.get_ansible_collector.assert_called_once()
    mock_ansible_collector.get_ansible_collector.return_value.collect.assert_called_once_with(module=mock_module)

def test_ansible_facts_custom_gather_subset(mock_module, mock_collectors, mock_ansible_collector):
    from ansible.module_utils.facts.compat import ansible_facts

    mock_module.params['gather_subset'] = ['custom']
    result = ansible_facts(mock_module)
    assert result == {'fact1': 'value1', 'fact2': 'value2'}
    mock_ansible_collector.get_ansible_collector.assert_called_once()
    mock_ansible_collector.get_ansible_collector.return_value.collect.assert_called_once_with(module=mock_module)

def test_ansible_facts_no_gather_subset(mock_module, mock_collectors, mock_ansible_collector):
    from ansible.module_utils.facts.compat import ansible_facts

    del mock_module.params['gather_subset']
    result = ansible_facts(mock_module)
    assert result == {'fact1': 'value1', 'fact2': 'value2'}
    mock_ansible_collector.get_ansible_collector.assert_called_once()
    mock_ansible_collector.get_ansible_collector.return_value.collect.assert_called_once_with(module=mock_module)

def test_ansible_facts_custom_filter(mock_module, mock_collectors, mock_ansible_collector):
    from ansible.module_utils.facts.compat import ansible_facts

    mock_module.params['filter'] = 'custom_filter'
    result = ansible_facts(mock_module)
    assert result == {'fact1': 'value1', 'fact2': 'value2'}
    mock_ansible_collector.get_ansible_collector.assert_called_once()
    mock_ansible_collector.get_ansible_collector.return_value.collect.assert_called_once_with(module=mock_module)

def test_ansible_facts_custom_timeout(mock_module, mock_collectors, mock_ansible_collector):
    from ansible.module_utils.facts.compat import ansible_facts

    mock_module.params['gather_timeout'] = 20
    result = ansible_facts(mock_module)
    assert result == {'fact1': 'value1', 'fact2': 'value2'}
    mock_ansible_collector.get_ansible_collector.assert_called_once()
    mock_ansible_collector.get_ansible_collector.return_value.collect.assert_called_once_with(module=mock_module)
