# file: lib/ansible/playbook/play.py:140-161
# asked: {"lines": [146, 154, 155, 156, 158, 159], "branches": [[145, 146], [151, 154], [154, 155], [154, 158]]}
# gained: {"lines": [146, 154, 155, 156, 158, 159], "branches": [[145, 146], [151, 154], [154, 155], [154, 158]]}

import pytest
from ansible.playbook.play import Play
from ansible.errors import AnsibleParserError, AnsibleAssertionError

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

def test_preprocess_data_not_dict(play_instance):
    with pytest.raises(AnsibleAssertionError) as excinfo:
        play_instance.preprocess_data(['not', 'a', 'dict'])
    assert 'ds should be a dict but was a' in str(excinfo.value)

def test_preprocess_data_user_and_remote_user(play_instance):
    ds = {'user': 'test_user', 'remote_user': 'test_remote_user'}
    with pytest.raises(AnsibleParserError) as excinfo:
        play_instance.preprocess_data(ds)
    assert "both 'user' and 'remote_user' are set for this play" in str(excinfo.value)

def test_preprocess_data_user_to_remote_user(play_instance):
    ds = {'user': 'test_user'}
    result = play_instance.preprocess_data(ds)
    assert 'remote_user' in result
    assert result['remote_user'] == 'test_user'
    assert 'user' not in result
