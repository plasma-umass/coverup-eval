# file lib/ansible/playbook/play_context.py:167-168
# lines [167, 168]
# branches []

import pytest
from ansible.playbook.play_context import PlayContext
from ansible.playbook.play import Play

# Mock class to simulate the Play object
class MockPlay:
    def __init__(self, force_handlers):
        self.force_handlers = force_handlers

@pytest.fixture
def mock_play():
    return MockPlay(force_handlers=True)

def test_set_attributes_from_play(mock_play):
    play_context = PlayContext()
    play_context.set_attributes_from_play(mock_play)
    assert play_context.force_handlers == mock_play.force_handlers

    # Clean up by resetting the attribute if necessary
    play_context.force_handlers = None
