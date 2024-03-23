# file lib/ansible/playbook/play.py:140-161
# lines [145, 146, 151, 154, 155, 156, 158, 159, 161]
# branches ['145->146', '145->151', '151->154', '151->161', '154->155', '154->158']

import pytest
from ansible.errors import AnsibleAssertionError, AnsibleParserError
from ansible.playbook.play import Play

# Assuming the existence of the Base and Taggable classes, and CollectionSearch module
# If they don't exist, they should be mocked or created for the purpose of this test

def test_preprocess_data_with_non_dict_input(mocker):
    play = Play()

    with pytest.raises(AnsibleAssertionError):
        play.preprocess_data([])

def test_preprocess_data_with_user_and_remote_user_keys(mocker):
    play = Play()

    with pytest.raises(AnsibleParserError):
        play.preprocess_data({'user': 'some_user', 'remote_user': 'some_other_user'})

def test_preprocess_data_with_user_key(mocker):
    mocker.patch('ansible.playbook.play.Base.preprocess_data', return_value='mocked_base_preprocess')
    play = Play()
    ds = {'user': 'some_user'}

    result = play.preprocess_data(ds)

    assert 'user' not in ds
    assert ds['remote_user'] == 'some_user'
    assert result == 'mocked_base_preprocess'
