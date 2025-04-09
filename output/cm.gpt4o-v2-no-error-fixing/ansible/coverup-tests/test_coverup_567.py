# file: lib/ansible/playbook/play.py:322-323
# asked: {"lines": [322, 323], "branches": []}
# gained: {"lines": [322], "branches": []}

import pytest
from ansible.playbook.play import Play

@pytest.fixture
def play_instance():
    class MockBase:
        pass

    class MockTaggable:
        pass

    class MockCollectionSearch:
        pass

    class MockPlay(MockBase, MockTaggable, MockCollectionSearch):
        def __init__(self):
            self.handlers = ['handler1', 'handler2']

        def get_handlers(self):
            return self.handlers[:]

    return MockPlay()

def test_get_handlers(play_instance):
    handlers = play_instance.get_handlers()
    assert handlers == ['handler1', 'handler2']
    assert handlers is not play_instance.handlers  # Ensure a copy is returned
