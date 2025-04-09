# file lib/ansible/playbook/play_context.py:128-154
# lines [154]
# branches ['135->138', '153->154']

import pytest
from ansible.playbook.play_context import PlayContext

def test_play_context_with_passwords_and_play(mocker):
    # Mocking the play object and its method
    mock_play = mocker.Mock()
    mocker.patch.object(PlayContext, 'set_attributes_from_play')

    passwords = {
        'conn_pass': 'test_conn_pass',
        'become_pass': 'test_become_pass'
    }

    # Create PlayContext instance with play and passwords
    pc = PlayContext(play=mock_play, passwords=passwords)

    # Assertions to verify the correct execution of the code
    assert pc.password == 'test_conn_pass'
    assert pc.become_pass == 'test_become_pass'
    pc.set_attributes_from_play.assert_called_once_with(mock_play)

def test_play_context_without_passwords(mocker):
    # Mocking the play object and its method
    mock_play = mocker.Mock()
    mocker.patch.object(PlayContext, 'set_attributes_from_play')

    # Create PlayContext instance with play but without passwords
    pc = PlayContext(play=mock_play)

    # Assertions to verify the correct execution of the code
    assert pc.password == ''
    assert pc.become_pass == ''
    pc.set_attributes_from_play.assert_called_once_with(mock_play)
