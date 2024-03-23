# file lib/ansible/executor/play_iterator.py:522-524
# lines [524]
# branches []

import pytest
from ansible.executor.play_iterator import PlayIterator

# Assuming the PlayIterator class is part of a larger file and has other dependencies
# and methods that are not shown here, we will mock any necessary parts.

class TestPlayIterator:
    @pytest.fixture
    def play_iterator(self, mocker):
        # Mock any necessary setup for the PlayIterator if needed
        inventory = mocker.MagicMock()
        play = mocker.MagicMock()
        play_context = mocker.MagicMock()
        variable_manager = mocker.MagicMock()
        all_vars = mocker.MagicMock()
        return PlayIterator(inventory, play, play_context, variable_manager, all_vars)

    def test_get_original_task(self, play_iterator, mocker):
        host = mocker.MagicMock()
        task = mocker.MagicMock()
        original_task, state = play_iterator.get_original_task(host, task)
        assert original_task is None
        assert state is None
