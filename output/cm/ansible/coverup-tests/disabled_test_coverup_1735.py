# file lib/ansible/executor/play_iterator.py:522-524
# lines [524]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.executor.play_iterator import PlayIterator

# Test function to cover the get_original_task method
def test_get_original_task():
    # Setup
    inventory = MagicMock()
    play = MagicMock()
    play_context = MagicMock()
    variable_manager = MagicMock()
    all_vars = MagicMock()
    play_iterator = PlayIterator(inventory, play, play_context, variable_manager, all_vars)

    # Execute
    original_task = play_iterator.get_original_task('some_host', 'some_task')

    # Assert
    assert original_task == (None, None), "get_original_task should return (None, None)"
