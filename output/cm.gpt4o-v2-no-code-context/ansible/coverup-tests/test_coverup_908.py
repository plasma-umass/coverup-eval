# file: lib/ansible/plugins/strategy/linear.py:83-199
# asked: {"lines": [90, 91, 92, 93, 94, 96, 97, 98, 99, 100, 102, 103, 104, 105, 107, 108, 109, 110, 112, 113, 114, 115, 116, 117, 118, 122, 124, 125, 127, 128, 130, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 145, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 168, 169, 170, 174, 175, 176, 180, 181, 182, 186, 187, 188, 192, 193, 194, 198, 199], "branches": [[98, 99], [98, 100], [112, 113], [112, 122], [124, 125], [124, 140], [128, 130], [128, 132], [132, 133], [132, 134], [134, 135], [134, 136], [136, 137], [136, 138], [138, 124], [138, 139], [156, 157], [156, 169], [158, 159], [158, 160], [162, 163], [162, 164], [164, 165], [164, 168], [174, 175], [174, 180], [180, 181], [180, 186], [186, 187], [186, 192], [192, 193], [192, 198]]}
# gained: {"lines": [90, 91, 92, 93, 94, 96, 97, 98, 99, 100, 102, 103, 104, 105, 107, 108, 109, 110, 112, 113, 114, 115, 116, 124, 125, 127, 128, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 145, 154, 155, 156, 157, 158, 160, 161, 162, 164, 165, 166, 169, 170, 174, 175, 176, 180, 181, 182, 186, 187, 188, 192, 193, 194, 198, 199], "branches": [[98, 99], [98, 100], [112, 113], [124, 125], [124, 140], [128, 132], [132, 133], [132, 134], [134, 135], [134, 136], [136, 137], [136, 138], [138, 124], [138, 139], [156, 157], [156, 169], [158, 160], [162, 164], [164, 165], [174, 175], [174, 180], [180, 181], [180, 186], [186, 187], [186, 192], [192, 193], [192, 198]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.strategy.linear import StrategyModule
from ansible.playbook.task import Task
from ansible.executor.play_iterator import PlayIterator
from ansible.utils.display import Display

@pytest.fixture
def mock_iterator():
    iterator = MagicMock(spec=PlayIterator)
    iterator.get_next_task_for_host = MagicMock()
    iterator.get_active_state = MagicMock()
    iterator._play = MagicMock()
    iterator._play._loader = MagicMock()
    return iterator

@pytest.fixture
def mock_display():
    with patch('ansible.plugins.strategy.linear.display', autospec=True) as mock_display:
        yield mock_display

@pytest.fixture
def mock_host():
    host = MagicMock()
    host.name = 'test_host'
    return host

@pytest.fixture
def strategy_module():
    tqm = MagicMock()
    return StrategyModule(tqm)

def test_get_next_task_lockstep_noop_task(strategy_module, mock_iterator, mock_display, mock_host):
    hosts = [mock_host]
    mock_iterator.get_next_task_for_host.return_value = (MagicMock(), MagicMock())
    mock_iterator.get_active_state.return_value = MagicMock(cur_block=0, run_state=PlayIterator.ITERATING_COMPLETE)

    result = strategy_module._get_next_task_lockstep(hosts, mock_iterator)

    assert result == [(mock_host, None)]
    mock_display.debug.assert_called()

def test_get_next_task_lockstep_iterating_setup(strategy_module, mock_iterator, mock_display, mock_host):
    hosts = [mock_host]
    state = MagicMock(cur_block=0, run_state=PlayIterator.ITERATING_SETUP)
    task = MagicMock()
    mock_iterator.get_next_task_for_host.return_value = (state, task)
    mock_iterator.get_active_state.return_value = state

    result = strategy_module._get_next_task_lockstep(hosts, mock_iterator)

    assert result == [(mock_host, task)]
    mock_display.debug.assert_called()

def test_get_next_task_lockstep_iterating_tasks(strategy_module, mock_iterator, mock_display, mock_host):
    hosts = [mock_host]
    state = MagicMock(cur_block=0, run_state=PlayIterator.ITERATING_TASKS)
    task = MagicMock()
    mock_iterator.get_next_task_for_host.return_value = (state, task)
    mock_iterator.get_active_state.return_value = state

    result = strategy_module._get_next_task_lockstep(hosts, mock_iterator)

    assert result == [(mock_host, task)]
    mock_display.debug.assert_called()

def test_get_next_task_lockstep_iterating_rescue(strategy_module, mock_iterator, mock_display, mock_host):
    hosts = [mock_host]
    state = MagicMock(cur_block=0, run_state=PlayIterator.ITERATING_RESCUE)
    task = MagicMock()
    mock_iterator.get_next_task_for_host.return_value = (state, task)
    mock_iterator.get_active_state.return_value = state

    result = strategy_module._get_next_task_lockstep(hosts, mock_iterator)

    assert result == [(mock_host, task)]
    mock_display.debug.assert_called()

def test_get_next_task_lockstep_iterating_always(strategy_module, mock_iterator, mock_display, mock_host):
    hosts = [mock_host]
    state = MagicMock(cur_block=0, run_state=PlayIterator.ITERATING_ALWAYS)
    task = MagicMock()
    mock_iterator.get_next_task_for_host.return_value = (state, task)
    mock_iterator.get_active_state.return_value = state

    result = strategy_module._get_next_task_lockstep(hosts, mock_iterator)

    assert result == [(mock_host, task)]
    mock_display.debug.assert_called()
