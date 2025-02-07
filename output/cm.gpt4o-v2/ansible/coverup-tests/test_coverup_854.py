# file: lib/ansible/executor/play_iterator.py:470-471
# asked: {"lines": [470, 471], "branches": []}
# gained: {"lines": [470, 471], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.executor.play_iterator import PlayIterator

@pytest.fixture
def play_iterator():
    inventory = MagicMock()
    play = MagicMock()
    play_context = MagicMock()
    variable_manager = MagicMock()
    all_vars = MagicMock()
    
    iterator = PlayIterator(inventory, play, play_context, variable_manager, all_vars)
    
    iterator._host_states = {
        'host1': MagicMock(run_state='ITERATING_RESCUE', fail_state='FAILED_NONE', did_rescue=False, rescue_child_state=None),
        'host2': MagicMock(run_state='ITERATING_ALWAYS', fail_state='FAILED_NONE', did_rescue=False, always_child_state=None),
        'host3': MagicMock(run_state='ITERATING_TASKS', fail_state='FAILED_NONE', did_rescue=False, tasks_child_state=None, _blocks=[MagicMock(rescue=[])], cur_block=0),
        'host4': MagicMock(run_state='ITERATING_TASKS', fail_state='FAILED_NONE', did_rescue=False, tasks_child_state=None, _blocks=[MagicMock(rescue=[1])], cur_block=0),
        'host5': MagicMock(run_state='ITERATING_RESCUE', fail_state='FAILED_RESCUE', did_rescue=False, rescue_child_state=None),
    }
    iterator.ITERATING_RESCUE = 'ITERATING_RESCUE'
    iterator.ITERATING_ALWAYS = 'ITERATING_ALWAYS'
    iterator.ITERATING_TASKS = 'ITERATING_TASKS'
    iterator.FAILED_NONE = 'FAILED_NONE'
    iterator.FAILED_RESCUE = 'FAILED_RESCUE'
    iterator.FAILED_ALWAYS = 'FAILED_ALWAYS'
    return iterator

def test_get_failed_hosts(play_iterator):
    def mock_check_failed_state(state):
        if state.fail_state == 'FAILED_RESCUE':
            return True
        return False

    play_iterator._check_failed_state = mock_check_failed_state

    failed_hosts = play_iterator.get_failed_hosts()
    assert failed_hosts == {'host5': True}
