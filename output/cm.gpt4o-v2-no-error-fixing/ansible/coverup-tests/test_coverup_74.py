# file: lib/ansible/utils/vars.py:213-232
# asked: {"lines": [213, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 227, 228, 229, 230, 232], "branches": [[215, 216], [215, 217], [227, 228], [227, 232], [229, 227], [229, 230]]}
# gained: {"lines": [213, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 227, 228, 229, 230, 232], "branches": [[215, 216], [215, 217], [227, 228], [227, 232], [229, 230]]}

import pytest
from ansible.utils.vars import load_options_vars
from ansible import context

@pytest.fixture
def mock_context_cliargs(monkeypatch):
    class MockCLIArgs:
        def __init__(self, args):
            self.args = args

        def get(self, attr):
            return self.args.get(attr)

    monkeypatch.setattr(context, 'CLIARGS', MockCLIArgs({
        'check': True,
        'diff': False,
        'forks': 5,
        'inventory': 'localhost',
        'skip_tags': 'test',
        'subset': 'all',
        'tags': 'deploy',
        'verbosity': 2
    }))

def test_load_options_vars_with_version(mock_context_cliargs):
    version = '2.9'
    expected_result = {
        'ansible_version': '2.9',
        'ansible_check_mode': True,
        'ansible_diff_mode': False,
        'ansible_forks': 5,
        'ansible_inventory_sources': 'localhost',
        'ansible_skip_tags': 'test',
        'ansible_limit': 'all',
        'ansible_run_tags': 'deploy',
        'ansible_verbosity': 2
    }
    result = load_options_vars(version)
    assert result == expected_result

def test_load_options_vars_without_version(mock_context_cliargs):
    version = None
    expected_result = {
        'ansible_version': 'Unknown',
        'ansible_check_mode': True,
        'ansible_diff_mode': False,
        'ansible_forks': 5,
        'ansible_inventory_sources': 'localhost',
        'ansible_skip_tags': 'test',
        'ansible_limit': 'all',
        'ansible_run_tags': 'deploy',
        'ansible_verbosity': 2
    }
    result = load_options_vars(version)
    assert result == expected_result
