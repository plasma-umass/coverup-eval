# file lib/ansible/executor/play_iterator.py:511-520
# lines [511, 516, 517, 518, 519, 520]
# branches ['516->517', '516->518', '518->519', '518->520']

import pytest
from ansible.executor.play_iterator import PlayIterator, HostState
from unittest.mock import MagicMock

# Mocking the HostState class to test the PlayIterator.is_any_block_rescuing method
class MockHostState(HostState):
    def __init__(self, run_state, tasks_child_state=None):
        self.run_state = run_state
        self.tasks_child_state = tasks_child_state

@pytest.fixture
def play_iterator(mocker):
    inventory = mocker.MagicMock()
    play = mocker.MagicMock()
    play_context = mocker.MagicMock()
    variable_manager = mocker.MagicMock()
    all_vars = mocker.MagicMock()
    return PlayIterator(inventory, play, play_context, variable_manager, all_vars)

def test_is_any_block_rescuing_with_rescue_state(play_iterator):
    state = MockHostState(PlayIterator.ITERATING_RESCUE)
    assert play_iterator.is_any_block_rescuing(state) == True

def test_is_any_block_rescuing_with_child_rescue_state(play_iterator):
    child_state = MockHostState(PlayIterator.ITERATING_RESCUE)
    parent_state = MockHostState(None, tasks_child_state=child_state)
    assert play_iterator.is_any_block_rescuing(parent_state) == True

def test_is_any_block_rescuing_without_rescue_state(play_iterator):
    state = MockHostState(None)
    assert play_iterator.is_any_block_rescuing(state) == False

def test_is_any_block_rescuing_with_nested_child_rescue_state(play_iterator):
    grandchild_state = MockHostState(PlayIterator.ITERATING_RESCUE)
    child_state = MockHostState(None, tasks_child_state=grandchild_state)
    parent_state = MockHostState(None, tasks_child_state=child_state)
    assert play_iterator.is_any_block_rescuing(parent_state) == True

def test_is_any_block_rescuing_with_no_rescue_state_in_hierarchy(play_iterator):
    grandchild_state = MockHostState(None)
    child_state = MockHostState(None, tasks_child_state=grandchild_state)
    parent_state = MockHostState(None, tasks_child_state=child_state)
    assert play_iterator.is_any_block_rescuing(parent_state) == False
