# file lib/ansible/playbook/play.py:140-161
# lines []
# branches ['151->161']

import pytest
from ansible.playbook.play import Play
from ansible.errors import AnsibleAssertionError, AnsibleParserError

def test_preprocess_data_user_and_remote_user(mocker):
    play_instance = Play()
    ds = {
        'user': 'test_user',
        'remote_user': 'test_remote_user'
    }

    with pytest.raises(AnsibleParserError, match="both 'user' and 'remote_user' are set for this play. The use of 'user' is deprecated, and should be removed"):
        play_instance.preprocess_data(ds)

def test_preprocess_data_user_only(mocker):
    play_instance = Play()
    ds = {
        'user': 'test_user'
    }

    mock_super = mocker.patch('ansible.playbook.play.Base.preprocess_data', return_value=None)
    
    play_instance.preprocess_data(ds)
    
    assert 'user' not in ds
    assert ds['remote_user'] == 'test_user'
    mock_super.assert_called_once_with(ds)

def test_preprocess_data_no_user(mocker):
    play_instance = Play()
    ds = {
        'remote_user': 'test_remote_user'
    }

    mock_super = mocker.patch('ansible.playbook.play.Base.preprocess_data', return_value=None)
    
    play_instance.preprocess_data(ds)
    
    assert 'user' not in ds
    assert ds['remote_user'] == 'test_remote_user'
    mock_super.assert_called_once_with(ds)
