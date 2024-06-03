# file lib/ansible/utils/vars.py:213-232
# lines [213, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 227, 228, 229, 230, 232]
# branches ['215->216', '215->217', '227->228', '227->232', '229->227', '229->230']

import pytest
from unittest import mock

# Assuming the function load_options_vars is imported from ansible.utils.vars
from ansible.utils.vars import load_options_vars

@pytest.fixture
def mock_context(mocker):
    context_mock = mocker.patch('ansible.utils.vars.context', autospec=True)
    return context_mock

def test_load_options_vars_with_version(mock_context):
    mock_context.CLIARGS = {'check': True, 'diff': False, 'forks': 5, 'verbosity': 2}
    version = '2.9.10'
    expected_result = {
        'ansible_version': version,
        'ansible_check_mode': True,
        'ansible_diff_mode': False,
        'ansible_forks': 5,
        'ansible_verbosity': 2
    }
    
    result = load_options_vars(version)
    assert result == expected_result

def test_load_options_vars_without_version(mock_context):
    mock_context.CLIARGS = {'inventory': 'hosts', 'skip_tags': 'test', 'subset': 'web'}
    expected_result = {
        'ansible_version': 'Unknown',
        'ansible_inventory_sources': 'hosts',
        'ansible_skip_tags': 'test',
        'ansible_limit': 'web'
    }
    
    result = load_options_vars(None)
    assert result == expected_result

def test_load_options_vars_empty_cliargs(mock_context):
    mock_context.CLIARGS = {}
    version = '2.9.10'
    expected_result = {
        'ansible_version': version
    }
    
    result = load_options_vars(version)
    assert result == expected_result
