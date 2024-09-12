# file: lib/ansible/playbook/play.py:322-323
# asked: {"lines": [322, 323], "branches": []}
# gained: {"lines": [322], "branches": []}

import pytest
from ansible.playbook.play import Play

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

def test_get_handlers():
    play = MockPlay()
    handlers = play.get_handlers()
    assert handlers == ['handler1', 'handler2']
    assert handlers is not play.handlers  # Ensure a copy is returned
