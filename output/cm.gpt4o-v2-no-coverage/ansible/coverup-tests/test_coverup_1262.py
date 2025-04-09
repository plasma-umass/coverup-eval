# file: lib/ansible/cli/adhoc.py:66-81
# asked: {"lines": [67, 69, 70, 73, 74, 75, 77, 78, 79, 80, 81], "branches": [[73, 74], [73, 77]]}
# gained: {"lines": [67, 69, 70, 73, 74, 75, 77, 78, 79, 80, 81], "branches": [[73, 74], [73, 77]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.adhoc import AdHocCLI
from ansible.parsing.splitter import parse_kv

@pytest.fixture
def mock_context():
    with patch('ansible.cli.adhoc.context') as mock_context:
        yield mock_context

@pytest.fixture
def mock_constants():
    with patch('ansible.cli.adhoc.C') as mock_constants:
        yield mock_constants

def test_play_ds_full_coverage(mock_context, mock_constants):
    # Setup mock values
    mock_context.CLIARGS = {
        'module_name': 'test_module',
        'module_args': 'arg1=val1 arg2=val2',
        'task_timeout': 30
    }
    mock_constants.MODULE_REQUIRE_ARGS = ['test_module']
    mock_constants._ACTION_ALL_INCLUDE_ROLE_TASKS = []

    adhoc_cli = AdHocCLI(MagicMock())

    # Test when module_name is in MODULE_REQUIRE_ARGS
    result = adhoc_cli._play_ds('all', 10, 5)
    assert result == {
        'name': 'Ansible Ad-Hoc',
        'hosts': 'all',
        'gather_facts': 'no',
        'tasks': [{
            'action': {
                'module': 'test_module',
                'args': parse_kv('arg1=val1 arg2=val2', check_raw=True)
            },
            'timeout': 30,
            'async_val': 10,
            'poll': 5
        }]
    }

    # Test when module_name is not in MODULE_REQUIRE_ARGS
    mock_context.CLIARGS['module_name'] = 'another_module'
    result = adhoc_cli._play_ds('all', 0, 0)
    assert result == {
        'name': 'Ansible Ad-Hoc',
        'hosts': 'all',
        'gather_facts': 'no',
        'tasks': [{
            'action': {
                'module': 'another_module',
                'args': parse_kv('arg1=val1 arg2=val2', check_raw=False)
            },
            'timeout': 30
        }]
    }
