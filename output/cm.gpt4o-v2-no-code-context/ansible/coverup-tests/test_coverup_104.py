# file: lib/ansible/utils/vars.py:213-232
# asked: {"lines": [213, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 227, 228, 229, 230, 232], "branches": [[215, 216], [215, 217], [227, 228], [227, 232], [229, 227], [229, 230]]}
# gained: {"lines": [213, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 227, 228, 229, 230, 232], "branches": [[215, 216], [215, 217], [227, 228], [227, 232], [229, 227], [229, 230]]}

import pytest
from unittest.mock import patch

# Assuming the function load_options_vars is imported from ansible/utils/vars.py
from ansible.utils.vars import load_options_vars

@pytest.fixture
def mock_context_cliargs():
    with patch('ansible.utils.vars.context.CLIARGS', {
        'check': True,
        'diff': False,
        'forks': 5,
        'inventory': 'inventory_file',
        'skip_tags': 'tag1,tag2',
        'subset': 'subset_value',
        'tags': 'tag3,tag4',
        'verbosity': 2
    }) as mock_cliargs:
        yield mock_cliargs

def test_load_options_vars_with_version(mock_context_cliargs):
    version = '2.9.10'
    result = load_options_vars(version)
    expected = {
        'ansible_version': '2.9.10',
        'ansible_check_mode': True,
        'ansible_diff_mode': False,
        'ansible_forks': 5,
        'ansible_inventory_sources': 'inventory_file',
        'ansible_skip_tags': 'tag1,tag2',
        'ansible_limit': 'subset_value',
        'ansible_run_tags': 'tag3,tag4',
        'ansible_verbosity': 2
    }
    assert result == expected

def test_load_options_vars_without_version(mock_context_cliargs):
    result = load_options_vars(None)
    expected = {
        'ansible_version': 'Unknown',
        'ansible_check_mode': True,
        'ansible_diff_mode': False,
        'ansible_forks': 5,
        'ansible_inventory_sources': 'inventory_file',
        'ansible_skip_tags': 'tag1,tag2',
        'ansible_limit': 'subset_value',
        'ansible_run_tags': 'tag3,tag4',
        'ansible_verbosity': 2
    }
    assert result == expected

def test_load_options_vars_with_partial_cliargs():
    with patch('ansible.utils.vars.context.CLIARGS', {
        'check': True,
        'verbosity': 2
    }):
        result = load_options_vars('2.9.10')
        expected = {
            'ansible_version': '2.9.10',
            'ansible_check_mode': True,
            'ansible_verbosity': 2
        }
        assert result == expected

def test_load_options_vars_with_no_cliargs():
    with patch('ansible.utils.vars.context.CLIARGS', {}):
        result = load_options_vars('2.9.10')
        expected = {
            'ansible_version': '2.9.10'
        }
        assert result == expected
