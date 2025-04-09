# file: lib/ansible/playbook/play_context.py:167-168
# asked: {"lines": [167, 168], "branches": []}
# gained: {"lines": [167, 168], "branches": []}

import pytest
from unittest.mock import Mock

# Assuming PlayContext and Base are defined somewhere in the ansible.playbook.play_context module
from ansible.playbook.play_context import PlayContext, Base

class TestPlayContext:
    @pytest.fixture
    def play_context(self):
        return PlayContext()

    def test_set_attributes_from_play(self, play_context):
        # Create a mock play object with the force_handlers attribute
        mock_play = Mock()
        mock_play.force_handlers = True

        # Call the method to set attributes from play
        play_context.set_attributes_from_play(mock_play)

        # Assert that the force_handlers attribute was set correctly
        assert play_context.force_handlers == True
