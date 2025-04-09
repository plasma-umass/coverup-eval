# file: lib/ansible/executor/play_iterator.py:236-254
# asked: {"lines": [238, 239, 241, 242, 243, 244, 246, 248, 249, 251, 252, 253, 254], "branches": [[242, 243], [242, 246], [248, 249], [248, 251]]}
# gained: {"lines": [238, 239, 241, 242, 243, 244, 246, 248, 249, 251, 252, 253, 254], "branches": [[242, 243], [242, 246], [248, 249], [248, 251]]}

import pytest
from unittest.mock import MagicMock, patch

# Assuming the PlayIterator class and necessary imports are available in the context
from ansible.executor.play_iterator import PlayIterator

class TestPlayIterator:
    
    @pytest.fixture
    def play_iterator(self):
        inventory = MagicMock()
        play = MagicMock()
        play_context = MagicMock()
        variable_manager = MagicMock()
        all_vars = MagicMock()
        return PlayIterator(inventory, play, play_context, variable_manager, all_vars)

    @pytest.fixture
    def host(self):
        host = MagicMock()
        host.name = "test_host"
        return host

    @pytest.fixture
    def mock_display(self, monkeypatch):
        display = MagicMock()
        monkeypatch.setattr("ansible.executor.play_iterator.display", display)
        return display

    @pytest.fixture
    def mock_get_host_state(self, play_iterator, monkeypatch):
        get_host_state = MagicMock()
        monkeypatch.setattr(play_iterator, "get_host_state", get_host_state)
        return get_host_state

    @pytest.fixture
    def mock_get_next_task_from_state(self, play_iterator, monkeypatch):
        get_next_task_from_state = MagicMock()
        monkeypatch.setattr(play_iterator, "_get_next_task_from_state", get_next_task_from_state)
        return get_next_task_from_state

    def test_get_next_task_for_host_iterating_complete(self, play_iterator, host, mock_display, mock_get_host_state):
        play_iterator.ITERATING_COMPLETE = "ITERATING_COMPLETE"
        mock_get_host_state.return_value.run_state = play_iterator.ITERATING_COMPLETE

        state, task = play_iterator.get_next_task_for_host(host)

        mock_display.debug.assert_any_call("getting the next task for host %s" % host.name)
        mock_display.debug.assert_any_call("host %s is done iterating, returning" % host.name)
        assert state.run_state == play_iterator.ITERATING_COMPLETE
        assert task is None

    def test_get_next_task_for_host_not_peek(self, play_iterator, host, mock_display, mock_get_host_state, mock_get_next_task_from_state):
        play_iterator.ITERATING_COMPLETE = "ITERATING_COMPLETE"
        mock_get_host_state.return_value.run_state = "NOT_COMPLETE"
        mock_get_next_task_from_state.return_value = (mock_get_host_state.return_value, "task")

        state, task = play_iterator.get_next_task_for_host(host, peek=False)

        mock_display.debug.assert_any_call("getting the next task for host %s" % host.name)
        mock_display.debug.assert_any_call("done getting next task for host %s" % host.name)
        mock_display.debug.assert_any_call(" ^ task is: %s" % task)
        mock_display.debug.assert_any_call(" ^ state is: %s" % state)
        assert play_iterator._host_states[host.name] == state
        assert task == "task"

    def test_get_next_task_for_host_peek(self, play_iterator, host, mock_display, mock_get_host_state, mock_get_next_task_from_state):
        play_iterator.ITERATING_COMPLETE = "ITERATING_COMPLETE"
        mock_get_host_state.return_value.run_state = "NOT_COMPLETE"
        mock_get_next_task_from_state.return_value = (mock_get_host_state.return_value, "task")

        state, task = play_iterator.get_next_task_for_host(host, peek=True)

        mock_display.debug.assert_any_call("getting the next task for host %s" % host.name)
        mock_display.debug.assert_any_call("done getting next task for host %s" % host.name)
        mock_display.debug.assert_any_call(" ^ task is: %s" % task)
        mock_display.debug.assert_any_call(" ^ state is: %s" % state)
        assert host.name not in play_iterator._host_states
        assert task == "task"
