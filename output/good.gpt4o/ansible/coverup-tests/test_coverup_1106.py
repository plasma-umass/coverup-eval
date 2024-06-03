# file lib/ansible/playbook/play.py:140-161
# lines [145, 146, 151, 154, 155, 156, 158, 159, 161]
# branches ['145->146', '145->151', '151->154', '151->161', '154->155', '154->158']

import pytest
from ansible.playbook.play import Play
from ansible.errors import AnsibleAssertionError, AnsibleParserError

def test_preprocess_data_not_dict():
    play = Play()
    with pytest.raises(AnsibleAssertionError) as excinfo:
        play.preprocess_data(['not', 'a', 'dict'])
    assert 'ds should be a dict but was a' in str(excinfo.value)

def test_preprocess_data_user_and_remote_user():
    play = Play()
    ds = {
        'user': 'test_user',
        'remote_user': 'test_remote_user'
    }
    with pytest.raises(AnsibleParserError) as excinfo:
        play.preprocess_data(ds)
    assert "both 'user' and 'remote_user' are set for this play" in str(excinfo.value)

def test_preprocess_data_user_only():
    play = Play()
    ds = {
        'user': 'test_user'
    }
    result = play.preprocess_data(ds)
    assert 'remote_user' in result
    assert result['remote_user'] == 'test_user'
    assert 'user' not in result
