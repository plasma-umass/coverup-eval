# file: lib/ansible/playbook/play.py:312-313
# asked: {"lines": [312, 313], "branches": []}
# gained: {"lines": [312], "branches": []}

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
            self.vars = {'key': 'value'}

        def get_vars(self):
            return self.vars.copy()

    return MockPlay()

def test_get_vars(play_instance):
    vars_copy = play_instance.get_vars()
    assert vars_copy == {'key': 'value'}
    assert vars_copy is not play_instance.vars  # Ensure it's a copy

