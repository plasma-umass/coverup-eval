# file: lib/ansible/module_utils/facts/compat.py:49-87
# asked: {"lines": [49, 63, 64, 65, 67, 72, 75, 77, 78, 79, 80, 81, 82, 83, 85, 87], "branches": []}
# gained: {"lines": [49, 63, 64, 65, 67, 72, 75, 77, 78, 79, 80, 81, 82, 83, 85, 87], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils.facts.compat import ansible_facts
from ansible.module_utils.basic import AnsibleModule

@pytest.fixture
def mock_module():
    module = MagicMock(spec=AnsibleModule)
    module.params = {
        'gather_subset': ['all'],
        'gather_timeout': 10,
        'filter': '*'
    }
    return module

@patch('ansible.module_utils.facts.ansible_collector.get_ansible_collector')
@patch('ansible.module_utils.facts.default_collectors.collectors', new_callable=list)
def test_ansible_facts(mock_collectors, mock_get_ansible_collector, mock_module):
    mock_fact_collector = MagicMock()
    mock_fact_collector.collect.return_value = {'test_fact': 'value'}
    mock_get_ansible_collector.return_value = mock_fact_collector

    result = ansible_facts(mock_module)

    mock_get_ansible_collector.assert_called_once()
    mock_fact_collector.collect.assert_called_once_with(module=mock_module)
    assert result == {'test_fact': 'value'}
