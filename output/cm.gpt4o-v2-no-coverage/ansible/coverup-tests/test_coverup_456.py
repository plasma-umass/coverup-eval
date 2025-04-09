# file: lib/ansible/playbook/play.py:121-131
# asked: {"lines": [121, 123, 124, 126, 127, 129, 131], "branches": [[123, 124], [123, 126], [126, 127], [126, 129]]}
# gained: {"lines": [121, 123, 124, 126, 127, 129, 131], "branches": [[123, 124], [123, 126], [126, 127], [126, 129]]}

import pytest
from ansible.playbook.play import Play
from ansible.module_utils.common.collections import is_sequence

@pytest.fixture
def play_instance(monkeypatch):
    class MockBase:
        pass

    class MockTaggable:
        pass

    class MockCollectionSearch:
        pass

    class MockPlay(MockBase, MockTaggable, MockCollectionSearch, Play):
        def __init__(self, name=None, hosts=None):
            self.name = name
            self.hosts = hosts

    monkeypatch.setattr("ansible.playbook.play.Base", MockBase)
    monkeypatch.setattr("ansible.playbook.play.Taggable", MockTaggable)
    monkeypatch.setattr("ansible.playbook.play.CollectionSearch", MockCollectionSearch)
    return MockPlay

def test_get_name_with_name(play_instance):
    play = play_instance(name="test_play")
    assert play.get_name() == "test_play"

def test_get_name_with_sequence_hosts(play_instance, monkeypatch):
    play = play_instance(hosts=["host1", "host2"])

    def mock_is_sequence(obj):
        return True

    monkeypatch.setattr("ansible.playbook.play.is_sequence", mock_is_sequence)
    assert play.get_name() == "host1,host2"

def test_get_name_with_non_sequence_hosts(play_instance, monkeypatch):
    play = play_instance(hosts="host1")

    def mock_is_sequence(obj):
        return False

    monkeypatch.setattr("ansible.playbook.play.is_sequence", mock_is_sequence)
    assert play.get_name() == "host1"

def test_get_name_with_no_name_or_hosts(play_instance, monkeypatch):
    play = play_instance()

    def mock_is_sequence(obj):
        return False

    monkeypatch.setattr("ansible.playbook.play.is_sequence", mock_is_sequence)
    assert play.get_name() == ""
