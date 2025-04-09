# file: lib/ansible/playbook/play.py:322-323
# asked: {"lines": [322, 323], "branches": []}
# gained: {"lines": [322, 323], "branches": []}

import pytest
from ansible.playbook.play import Play

@pytest.fixture
def play_instance():
    instance = Play()
    instance.handlers = []
    return instance

def test_get_handlers(play_instance):
    # Ensure handlers list is initially empty
    assert play_instance.get_handlers() == []

    # Add a handler and test again
    play_instance.handlers.append('handler1')
    assert play_instance.get_handlers() == ['handler1']

    # Clean up
    play_instance.handlers.clear()
    assert play_instance.get_handlers() == []
