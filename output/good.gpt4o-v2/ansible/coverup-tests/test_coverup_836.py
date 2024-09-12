# file: lib/ansible/playbook/play_context.py:167-168
# asked: {"lines": [167, 168], "branches": []}
# gained: {"lines": [167, 168], "branches": []}

import pytest
from ansible.playbook.play_context import PlayContext

class MockPlay:
    def __init__(self, force_handlers):
        self.force_handlers = force_handlers

def test_set_attributes_from_play():
    play_context = PlayContext()
    mock_play = MockPlay(force_handlers=True)
    
    play_context.set_attributes_from_play(mock_play)
    
    assert play_context.force_handlers == True

    mock_play = MockPlay(force_handlers=False)
    
    play_context.set_attributes_from_play(mock_play)
    
    assert play_context.force_handlers == False
