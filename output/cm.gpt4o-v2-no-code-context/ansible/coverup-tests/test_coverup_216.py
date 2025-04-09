# file: lib/ansible/module_utils/facts/compat.py:49-87
# asked: {"lines": [49, 63, 64, 65, 67, 72, 75, 77, 78, 79, 80, 81, 82, 83, 85, 87], "branches": []}
# gained: {"lines": [49, 63, 64, 65, 67, 72, 75, 77, 78, 79, 80, 81, 82, 83, 85, 87], "branches": []}

import pytest
from unittest.mock import MagicMock, patch

# Assuming the ansible_facts function is imported from ansible/module_utils/facts/compat.py
from ansible.module_utils.facts.compat import ansible_facts

@pytest.fixture
def mock_module():
    module = MagicMock()
    module.params = {
        'gather_subset': ['all'],
        'gather_timeout': 10,
        'filter': '*'
    }
    return module

@patch('ansible.module_utils.facts.compat.default_collectors')
@patch('ansible.module_utils.facts.compat.ansible_collector')
@patch('ansible.module_utils.facts.compat.PrefixFactNamespace')
def test_ansible_facts(mock_prefix_fact_namespace, mock_ansible_collector, mock_default_collectors, mock_module):
    # Mock the necessary components
    mock_prefix_fact_namespace.return_value = MagicMock()
    mock_fact_collector = MagicMock()
    mock_fact_collector.collect.return_value = {'some_fact': 'some_value'}
    mock_ansible_collector.get_ansible_collector.return_value = mock_fact_collector
    mock_default_collectors.collectors = ['collector1', 'collector2']

    # Call the function
    result = ansible_facts(mock_module)

    # Assertions to verify the function behavior
    assert result == {'some_fact': 'some_value'}
    mock_prefix_fact_namespace.assert_called_once_with(namespace_name='ansible', prefix='')
    mock_ansible_collector.get_ansible_collector.assert_called_once_with(
        all_collector_classes=['collector1', 'collector2'],
        namespace=mock_prefix_fact_namespace.return_value,
        filter_spec='*',
        gather_subset=['all'],
        gather_timeout=10,
        minimal_gather_subset=frozenset(['apparmor', 'caps', 'cmdline', 'date_time',
                                         'distribution', 'dns', 'env', 'fips', 'local',
                                         'lsb', 'pkg_mgr', 'platform', 'python', 'selinux',
                                         'service_mgr', 'ssh_pub_keys', 'user'])
    )
    mock_fact_collector.collect.assert_called_once_with(module=mock_module)

def test_ansible_facts_with_no_gather_subset(mock_module):
    # Remove gather_subset to test the default behavior
    del mock_module.params['gather_subset']

    with patch('ansible.module_utils.facts.compat.default_collectors') as mock_default_collectors, \
         patch('ansible.module_utils.facts.compat.ansible_collector') as mock_ansible_collector, \
         patch('ansible.module_utils.facts.compat.PrefixFactNamespace') as mock_prefix_fact_namespace:
        
        # Mock the necessary components
        mock_prefix_fact_namespace.return_value = MagicMock()
        mock_fact_collector = MagicMock()
        mock_fact_collector.collect.return_value = {'some_fact': 'some_value'}
        mock_ansible_collector.get_ansible_collector.return_value = mock_fact_collector
        mock_default_collectors.collectors = ['collector1', 'collector2']

        # Call the function
        result = ansible_facts(mock_module)

        # Assertions to verify the function behavior
        assert result == {'some_fact': 'some_value'}
        mock_prefix_fact_namespace.assert_called_once_with(namespace_name='ansible', prefix='')
        mock_ansible_collector.get_ansible_collector.assert_called_once_with(
            all_collector_classes=['collector1', 'collector2'],
            namespace=mock_prefix_fact_namespace.return_value,
            filter_spec='*',
            gather_subset=['all'],
            gather_timeout=10,
            minimal_gather_subset=frozenset(['apparmor', 'caps', 'cmdline', 'date_time',
                                             'distribution', 'dns', 'env', 'fips', 'local',
                                             'lsb', 'pkg_mgr', 'platform', 'python', 'selinux',
                                             'service_mgr', 'ssh_pub_keys', 'user'])
        )
        mock_fact_collector.collect.assert_called_once_with(module=mock_module)
