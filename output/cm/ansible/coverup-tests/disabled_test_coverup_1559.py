# file lib/ansible/playbook/play_context.py:339-355
# lines [341, 342, 343, 345, 346, 349, 350, 352, 353, 355]
# branches ['342->343', '342->349', '345->346', '345->352', '349->350', '349->352', '352->353', '352->355']

import pytest
from unittest.mock import patch
from ansible.playbook.play_context import PlayContext

@pytest.fixture
def play_context():
    return PlayContext()

def test_get_attr_connection_smart_without_controlpersist_and_paramiko(play_context, mocker):
    mocker.patch.object(play_context, '_attributes', {'connection': 'smart'})
    mocker.patch('ansible.playbook.play_context.check_for_controlpersist', return_value=False)
    mocker.patch('ansible.playbook.play_context.paramiko', create=True)
    play_context._get_attr_connection()
    assert play_context.connection == 'paramiko'

def test_get_attr_connection_persistent_with_paramiko(play_context, mocker):
    mocker.patch.object(play_context, '_attributes', {'connection': 'persistent'})
    mocker.patch('ansible.playbook.play_context.paramiko', create=True)
    play_context._get_attr_connection()
    assert play_context.connection == 'paramiko'
