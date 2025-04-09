# file lib/ansible/module_utils/facts/compat.py:49-87
# lines [49, 63, 64, 65, 67, 72, 75, 77, 78, 79, 80, 81, 82, 83, 85, 87]
# branches []

import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils.facts.compat import ansible_facts, PrefixFactNamespace, ansible_collector, default_collectors

@pytest.fixture
def mock_module():
    module = MagicMock()
    module.params = {
        'gather_subset': ['all'],
        'gather_timeout': 10,
        'filter': '*'
    }
    return module

def test_ansible_facts_with_gather_subset(mock_module):
    with patch('ansible.module_utils.facts.compat.default_collectors') as mock_collectors, \
         patch('ansible.module_utils.facts.compat.ansible_collector') as mock_ansible_collector, \
         patch('ansible.module_utils.facts.compat.PrefixFactNamespace') as mock_PrefixFactNamespace:
        
        mock_collectors.collectors = []
        mock_PrefixFactNamespace.return_value = MagicMock()
        mock_fact_collector = MagicMock()
        mock_fact_collector.collect.return_value = {'some_fact': 'some_value'}
        mock_ansible_collector.get_ansible_collector.return_value = mock_fact_collector

        result = ansible_facts(mock_module, gather_subset=['all'])

        mock_ansible_collector.get_ansible_collector.assert_called_once_with(
            all_collector_classes=[],
            namespace=mock_PrefixFactNamespace.return_value,
            filter_spec='*',
            gather_subset=['all'],
            gather_timeout=10,
            minimal_gather_subset=frozenset(['apparmor', 'caps', 'cmdline', 'date_time',
                                             'distribution', 'dns', 'env', 'fips', 'local',
                                             'lsb', 'pkg_mgr', 'platform', 'python', 'selinux',
                                             'service_mgr', 'ssh_pub_keys', 'user'])
        )
        mock_fact_collector.collect.assert_called_once_with(module=mock_module)
        assert result == {'some_fact': 'some_value'}

def test_ansible_facts_without_gather_subset(mock_module):
    del mock_module.params['gather_subset']
    
    with patch('ansible.module_utils.facts.compat.default_collectors') as mock_collectors, \
         patch('ansible.module_utils.facts.compat.ansible_collector') as mock_ansible_collector, \
         patch('ansible.module_utils.facts.compat.PrefixFactNamespace') as mock_PrefixFactNamespace:
        
        mock_collectors.collectors = []
        mock_PrefixFactNamespace.return_value = MagicMock()
        mock_fact_collector = MagicMock()
        mock_fact_collector.collect.return_value = {'some_fact': 'some_value'}
        mock_ansible_collector.get_ansible_collector.return_value = mock_fact_collector

        result = ansible_facts(mock_module)

        mock_ansible_collector.get_ansible_collector.assert_called_once_with(
            all_collector_classes=[],
            namespace=mock_PrefixFactNamespace.return_value,
            filter_spec='*',
            gather_subset=['all'],
            gather_timeout=10,
            minimal_gather_subset=frozenset(['apparmor', 'caps', 'cmdline', 'date_time',
                                             'distribution', 'dns', 'env', 'fips', 'local',
                                             'lsb', 'pkg_mgr', 'platform', 'python', 'selinux',
                                             'service_mgr', 'ssh_pub_keys', 'user'])
        )
        mock_fact_collector.collect.assert_called_once_with(module=mock_module)
        assert result == {'some_fact': 'some_value'}
