# file lib/ansible/playbook/play.py:140-161
# lines [140, 145, 146, 151, 154, 155, 156, 158, 159, 161]
# branches ['145->146', '145->151', '151->154', '151->161', '154->155', '154->158']

import pytest
from ansible.errors import AnsibleAssertionError, AnsibleParserError
from ansible.playbook.play import Play

def test_preprocess_data_with_non_dict_input(mocker):
    play = Play()

    with pytest.raises(AnsibleAssertionError):
        play.preprocess_data([])

def test_preprocess_data_with_user_and_remote_user_keys(mocker):
    play = Play()
    ds = {'user': 'some_user', 'remote_user': 'some_other_user'}

    with pytest.raises(AnsibleParserError):
        play.preprocess_data(ds)

def test_preprocess_data_with_user_key(mocker):
    play = Play()
    ds = {'user': 'some_user'}
    mocker.spy(play, 'preprocess_data')

    result = play.preprocess_data(ds)

    play.preprocess_data.assert_called_once_with(ds)
    assert 'user' not in result
    assert result['remote_user'] == 'some_user'

# Ensure that the test functions are collected and run by pytest
pytest.main([__file__])
