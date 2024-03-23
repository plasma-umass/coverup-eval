# file lib/ansible/executor/play_iterator.py:499-509
# lines [503, 504, 505, 506, 507, 508, 509]
# branches ['503->504', '503->505', '505->506', '505->507', '507->508', '507->509']

import pytest
from ansible.executor.play_iterator import PlayIterator
from unittest.mock import MagicMock

class MockState:
    ITERATING_TASKS = 'ITERATING_TASKS'
    ITERATING_RESCUE = 'ITERATING_RESCUE'
    ITERATING_ALWAYS = 'ITERATING_ALWAYS'
    def __init__(self, run_state, tasks_child_state=None, rescue_child_state=None, always_child_state=None):
        self.run_state = run_state
        self.tasks_child_state = tasks_child_state
        self.rescue_child_state = rescue_child_state
        self.always_child_state = always_child_state

@pytest.fixture
def play_iterator(mocker):
    inventory = mocker.MagicMock()
    play = mocker.MagicMock()
    play_context = mocker.MagicMock()
    variable_manager = mocker.MagicMock()
    all_vars = mocker.MagicMock()
    pi = PlayIterator(inventory, play, play_context, variable_manager, all_vars)
    pi.ITERATING_TASKS = MockState.ITERATING_TASKS
    pi.ITERATING_RESCUE = MockState.ITERATING_RESCUE
    pi.ITERATING_ALWAYS = MockState.ITERATING_ALWAYS
    return pi

def test_get_active_state_with_tasks_child_state(play_iterator):
    child_state = MockState(MockState.ITERATING_TASKS)
    parent_state = MockState(MockState.ITERATING_TASKS, tasks_child_state=child_state)
    active_state = play_iterator.get_active_state(parent_state)
    assert active_state is child_state

def test_get_active_state_with_rescue_child_state(play_iterator):
    child_state = MockState(MockState.ITERATING_RESCUE)
    parent_state = MockState(MockState.ITERATING_RESCUE, rescue_child_state=child_state)
    active_state = play_iterator.get_active_state(parent_state)
    assert active_state is child_state

def test_get_active_state_with_always_child_state(play_iterator):
    child_state = MockState(MockState.ITERATING_ALWAYS)
    parent_state = MockState(MockState.ITERATING_ALWAYS, always_child_state=child_state)
    active_state = play_iterator.get_active_state(parent_state)
    assert active_state is child_state
