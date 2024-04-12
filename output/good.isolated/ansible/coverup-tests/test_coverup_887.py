# file lib/ansible/executor/play_iterator.py:522-524
# lines [522, 524]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.executor.play_iterator import PlayIterator

# Since the method `get_original_task` is a noop and always returns (None, None),
# we just need to test that it indeed returns these values.
# We will mock the required arguments for the PlayIterator constructor.

def test_get_original_task(mocker):
    inventory = mocker.MagicMock()
    play = mocker.MagicMock()
    play_context = mocker.MagicMock()
    variable_manager = mocker.MagicMock()
    all_vars = mocker.MagicMock()

    play_iterator = PlayIterator(inventory, play, play_context, variable_manager, all_vars)
    host = object()  # Mock host object
    task = object()  # Mock task object

    original_task, state = play_iterator.get_original_task(host, task)

    assert original_task is None
    assert state is None
