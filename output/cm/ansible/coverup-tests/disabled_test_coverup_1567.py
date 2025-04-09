# file lib/ansible/playbook/play.py:140-161
# lines [145, 146, 151, 154, 155, 156, 158, 159, 161]
# branches ['145->146', '145->151', '151->154', '151->161', '154->155', '154->158']

import pytest
from ansible.errors import AnsibleAssertionError, AnsibleParserError
from ansible.playbook.play import Play

def test_preprocess_data_non_dict():
    play = Play()

    with pytest.raises(AnsibleAssertionError):
        play.preprocess_data([])

def test_preprocess_data_user_and_remote_user():
    play = Play()

    with pytest.raises(AnsibleParserError):
        play.preprocess_data({'user': 'some_user', 'remote_user': 'some_other_user'})

def test_preprocess_data_user_only():
    play = Play()

    data_structure = {'user': 'some_user'}
    result = play.preprocess_data(data_structure)

    assert 'user' not in result
    assert result['remote_user'] == 'some_user'
