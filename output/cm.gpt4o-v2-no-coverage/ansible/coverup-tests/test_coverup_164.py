# file: lib/ansible/utils/vars.py:213-232
# asked: {"lines": [213, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 227, 228, 229, 230, 232], "branches": [[215, 216], [215, 217], [227, 228], [227, 232], [229, 227], [229, 230]]}
# gained: {"lines": [213, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 227, 228, 229, 230, 232], "branches": [[215, 216], [215, 217], [227, 228], [227, 232], [229, 230]]}

import pytest
from ansible.utils.vars import load_options_vars
from ansible import context

@pytest.fixture
def mock_context(mocker):
    mocker.patch.object(context, 'CLIARGS', {
        'check': True,
        'diff': False,
        'forks': 5,
        'inventory': 'localhost',
        'skip_tags': 'tag1,tag2',
        'subset': 'all',
        'tags': 'tag3,tag4',
        'verbosity': 2
    })

def test_load_options_vars_with_version(mock_context):
    version = '2.9'
    expected = {
        'ansible_version': version,
        'ansible_check_mode': True,
        'ansible_diff_mode': False,
        'ansible_forks': 5,
        'ansible_inventory_sources': 'localhost',
        'ansible_skip_tags': 'tag1,tag2',
        'ansible_limit': 'all',
        'ansible_run_tags': 'tag3,tag4',
        'ansible_verbosity': 2
    }
    result = load_options_vars(version)
    assert result == expected

def test_load_options_vars_without_version(mock_context):
    version = None
    expected = {
        'ansible_version': 'Unknown',
        'ansible_check_mode': True,
        'ansible_diff_mode': False,
        'ansible_forks': 5,
        'ansible_inventory_sources': 'localhost',
        'ansible_skip_tags': 'tag1,tag2',
        'ansible_limit': 'all',
        'ansible_run_tags': 'tag3,tag4',
        'ansible_verbosity': 2
    }
    result = load_options_vars(version)
    assert result == expected
