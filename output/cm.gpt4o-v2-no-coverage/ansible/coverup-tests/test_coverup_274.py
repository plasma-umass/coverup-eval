# file: lib/ansible/playbook/play.py:140-161
# asked: {"lines": [140, 145, 146, 151, 154, 155, 156, 158, 159, 161], "branches": [[145, 146], [145, 151], [151, 154], [151, 161], [154, 155], [154, 158]]}
# gained: {"lines": [140, 145, 146, 151, 154, 155, 156, 158, 159, 161], "branches": [[145, 146], [145, 151], [151, 154], [151, 161], [154, 155], [154, 158]]}

import pytest
from ansible.errors import AnsibleParserError, AnsibleAssertionError
from ansible.playbook.play import Play

class MockBase:
    def preprocess_data(self, ds):
        return ds

class MockTaggable:
    pass

class MockCollectionSearch:
    pass

class TestPlay(Play, MockBase, MockTaggable, MockCollectionSearch):
    pass

@pytest.fixture
def play_instance():
    return TestPlay()

def test_preprocess_data_with_non_dict(play_instance):
    with pytest.raises(AnsibleAssertionError) as excinfo:
        play_instance.preprocess_data(['not', 'a', 'dict'])
    assert 'ds should be a dict but was a' in str(excinfo.value)

def test_preprocess_data_with_user_and_remote_user(play_instance):
    ds = {'user': 'test_user', 'remote_user': 'test_remote_user'}
    with pytest.raises(AnsibleParserError) as excinfo:
        play_instance.preprocess_data(ds)
    assert "both 'user' and 'remote_user' are set for this play" in str(excinfo.value)

def test_preprocess_data_with_user_only(play_instance):
    ds = {'user': 'test_user'}
    result = play_instance.preprocess_data(ds)
    assert 'user' not in result
    assert result['remote_user'] == 'test_user'

def test_preprocess_data_with_valid_dict(play_instance):
    ds = {'some_key': 'some_value'}
    result = play_instance.preprocess_data(ds)
    assert result == ds
