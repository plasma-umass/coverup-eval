# file: lib/ansible/playbook/play.py:101-102
# asked: {"lines": [102], "branches": []}
# gained: {"lines": [102], "branches": []}

import pytest
from ansible.playbook.play import Play

class MockBase:
    pass

class MockTaggable:
    pass

class MockCollectionSearch:
    pass

class MockPlay(MockBase, MockTaggable, MockCollectionSearch, Play):
    def get_name(self):
        return "mock_play"

@pytest.fixture
def mock_play():
    return MockPlay()

def test_play_repr(mock_play):
    assert repr(mock_play) == "mock_play"
