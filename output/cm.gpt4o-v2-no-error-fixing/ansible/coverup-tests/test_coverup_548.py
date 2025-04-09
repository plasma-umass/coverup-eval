# file: lib/ansible/playbook/play_context.py:167-168
# asked: {"lines": [167, 168], "branches": []}
# gained: {"lines": [167, 168], "branches": []}

import pytest
from ansible.playbook.play_context import PlayContext

class MockPlay:
    def __init__(self, force_handlers):
        self.force_handlers = force_handlers

def test_set_attributes_from_play():
    play = MockPlay(force_handlers=True)
    context = PlayContext()
    context.set_attributes_from_play(play)
    assert context.force_handlers == True

    play = MockPlay(force_handlers=False)
    context = PlayContext()
    context.set_attributes_from_play(play)
    assert context.force_handlers == False
