# file lib/ansible/playbook/play.py:322-323
# lines [322, 323]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the Play class is imported from ansible.playbook.play
from ansible.playbook.play import Play

@pytest.fixture
def play_instance():
    # Create a mock instance of Play with handlers attribute
    play = Play()
    handler1 = MagicMock()
    handler1.name = 'handler1'
    handler2 = MagicMock()
    handler2.name = 'handler2'
    play.handlers = [handler1, handler2]
    yield play
    # Clean up if necessary (not much to clean up in this simple case)

def test_get_handlers(play_instance):
    handlers = play_instance.get_handlers()
    assert handlers == play_instance.handlers
    assert len(handlers) == 2
    assert handlers[0].name == 'handler1'
    assert handlers[1].name == 'handler2'
