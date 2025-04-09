# file: lib/ansible/playbook/play.py:322-323
# asked: {"lines": [323], "branches": []}
# gained: {"lines": [323], "branches": []}

import pytest
from ansible.playbook.play import Play

@pytest.fixture
def play_instance():
    class MockPlay(Play):
        def __init__(self):
            self.handlers = ['handler1', 'handler2']
    return MockPlay()

def test_get_handlers(play_instance):
    handlers = play_instance.get_handlers()
    assert handlers == ['handler1', 'handler2']
    assert handlers is not play_instance.handlers  # Ensure a copy is returned
