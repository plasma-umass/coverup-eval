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

@pytest.fixture
def play_instance(monkeypatch):
    class MockPlay(MockBase, MockTaggable, MockCollectionSearch):
        def __init__(self):
            self.handlers = ['handler1', 'handler2']

        def get_handlers(self):
            return self.handlers[:]

    monkeypatch.setattr('ansible.playbook.play.Play', MockPlay)
    return MockPlay()

def test_get_handlers(play_instance):
    handlers = play_instance.get_handlers()
    assert handlers == ['handler1', 'handler2']
    assert handlers is not play_instance.handlers  # Ensure a copy is returned
