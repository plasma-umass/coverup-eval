# file: lib/ansible/utils/vars.py:213-232
# asked: {"lines": [213, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 227, 228, 229, 230, 232], "branches": [[215, 216], [215, 217], [227, 228], [227, 232], [229, 227], [229, 230]]}
# gained: {"lines": [213, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 227, 228, 229, 230, 232], "branches": [[215, 216], [215, 217], [227, 228], [227, 232], [229, 230]]}

import pytest
from ansible.utils.vars import load_options_vars
from ansible import context

@pytest.fixture
def reset_context():
    original_cliargs = context.CLIARGS
    context.CLIARGS = context.CLIArgs({
        'check': False,
        'diff': False,
        'forks': 5,
        'inventory': 'localhost',
        'skip_tags': 'tag1,tag2',
        'subset': 'all',
        'tags': 'tag3,tag4',
        'verbosity': 2
    })
    yield
    context.CLIARGS = original_cliargs

def test_load_options_vars_with_version_none(reset_context):
    context.CLIARGS = context.CLIArgs({
        'check': True,
        'diff': True,
        'forks': 5,
        'inventory': 'localhost',
        'skip_tags': 'tag1,tag2',
        'subset': 'all',
        'tags': 'tag3,tag4',
        'verbosity': 2
    })
    result = load_options_vars(None)
    assert result == {
        'ansible_version': 'Unknown',
        'ansible_check_mode': True,
        'ansible_diff_mode': True,
        'ansible_forks': 5,
        'ansible_inventory_sources': 'localhost',
        'ansible_skip_tags': 'tag1,tag2',
        'ansible_limit': 'all',
        'ansible_run_tags': 'tag3,tag4',
        'ansible_verbosity': 2
    }

def test_load_options_vars_with_specific_version(reset_context):
    context.CLIARGS = context.CLIArgs({
        'check': False,
        'diff': False,
        'forks': 10,
        'inventory': 'remotehost',
        'skip_tags': 'tag5,tag6',
        'subset': 'none',
        'tags': 'tag7,tag8',
        'verbosity': 3
    })
    result = load_options_vars('2.9.10')
    assert result == {
        'ansible_version': '2.9.10',
        'ansible_check_mode': False,
        'ansible_diff_mode': False,
        'ansible_forks': 10,
        'ansible_inventory_sources': 'remotehost',
        'ansible_skip_tags': 'tag5,tag6',
        'ansible_limit': 'none',
        'ansible_run_tags': 'tag7,tag8',
        'ansible_verbosity': 3
    }
