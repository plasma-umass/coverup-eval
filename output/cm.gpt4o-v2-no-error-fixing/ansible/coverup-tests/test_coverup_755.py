# file: lib/ansible/playbook/play.py:140-161
# asked: {"lines": [145, 146, 151, 154, 155, 156, 158, 159, 161], "branches": [[145, 146], [145, 151], [151, 154], [151, 161], [154, 155], [154, 158]]}
# gained: {"lines": [145, 146, 151, 154, 155, 156, 158, 159, 161], "branches": [[145, 146], [145, 151], [151, 154], [151, 161], [154, 155], [154, 158]]}

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

def test_preprocess_data_not_dict():
    play = TestPlay()
    with pytest.raises(AnsibleAssertionError, match="ds should be a dict but was a"):
        play.preprocess_data([])

def test_preprocess_data_user_and_remote_user():
    play = TestPlay()
    ds = {'user': 'test_user', 'remote_user': 'test_remote_user'}
    with pytest.raises(AnsibleParserError, match="both 'user' and 'remote_user' are set for this play"):
        play.preprocess_data(ds)

def test_preprocess_data_user_only():
    play = TestPlay()
    ds = {'user': 'test_user'}
    result = play.preprocess_data(ds)
    assert 'remote_user' in result
    assert result['remote_user'] == 'test_user'
    assert 'user' not in result

def test_preprocess_data_no_user():
    play = TestPlay()
    ds = {}
    result = play.preprocess_data(ds)
    assert result == ds
