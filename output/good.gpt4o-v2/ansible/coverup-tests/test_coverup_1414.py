# file: lib/ansible/executor/playbook_executor.py:50-76
# asked: {"lines": [60], "branches": [[58, 60]]}
# gained: {"lines": [60], "branches": [[58, 60]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible import context

@pytest.fixture
def mock_context_cliargs():
    original_cliargs = context.CLIARGS
    context.CLIARGS = MagicMock()
    context.CLIARGS.get = MagicMock(side_effect=lambda key: {'listhosts': False, 'listtasks': False, 'listtags': False, 'syntax': False, 'forks': 5}.get(key))
    yield
    context.CLIARGS = original_cliargs

def test_playbook_executor_tqm_none_listhosts(mock_context_cliargs):
    context.CLIARGS.get = MagicMock(side_effect=lambda key: {'listhosts': True}.get(key, False))
    executor = PlaybookExecutor([], None, None, None, None)
    assert executor._tqm is None

def test_playbook_executor_tqm_none_listtasks(mock_context_cliargs):
    context.CLIARGS.get = MagicMock(side_effect=lambda key: {'listtasks': True}.get(key, False))
    executor = PlaybookExecutor([], None, None, None, None)
    assert executor._tqm is None

def test_playbook_executor_tqm_none_listtags(mock_context_cliargs):
    context.CLIARGS.get = MagicMock(side_effect=lambda key: {'listtags': True}.get(key, False))
    executor = PlaybookExecutor([], None, None, None, None)
    assert executor._tqm is None

def test_playbook_executor_tqm_none_syntax(mock_context_cliargs):
    context.CLIARGS.get = MagicMock(side_effect=lambda key: {'syntax': True}.get(key, False))
    executor = PlaybookExecutor([], None, None, None, None)
    assert executor._tqm is None

def test_playbook_executor_tqm_created(mock_context_cliargs):
    with patch('ansible.executor.playbook_executor.TaskQueueManager') as MockTQM:
        executor = PlaybookExecutor([], 'inventory', 'variable_manager', 'loader', 'passwords')
        MockTQM.assert_called_once_with(inventory='inventory', variable_manager='variable_manager', loader='loader', passwords='passwords', forks=5)
        assert executor._tqm == MockTQM()
