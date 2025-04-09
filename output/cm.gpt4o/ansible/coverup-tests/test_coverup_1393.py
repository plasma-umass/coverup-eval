# file lib/ansible/playbook/play_context.py:339-355
# lines [341, 342, 343, 345, 346, 349, 350, 352, 353, 355]
# branches ['342->343', '342->349', '345->346', '345->352', '349->350', '349->352', '352->353', '352->355']

import pytest
from unittest.mock import patch, MagicMock

# Assuming the PlayContext class is imported from ansible.playbook.play_context
from ansible.playbook.play_context import PlayContext

@pytest.fixture
def play_context():
    return PlayContext()

def test_get_attr_connection_smart_with_controlpersist(play_context, mocker):
    mocker.patch('ansible.playbook.play_context.check_for_controlpersist', return_value=True)
    play_context._attributes = {'connection': 'smart'}
    play_context._get_attr_connection()
    assert play_context.connection == 'ssh'

def test_get_attr_connection_smart_without_controlpersist(play_context, mocker):
    mocker.patch('ansible.playbook.play_context.check_for_controlpersist', return_value=False)
    mocker.patch('ansible.playbook.play_context.paramiko', MagicMock())
    play_context._attributes = {'connection': 'smart'}
    play_context._get_attr_connection()
    assert play_context.connection == 'paramiko'

def test_get_attr_connection_persistent(play_context, mocker):
    mocker.patch('ansible.playbook.play_context.paramiko', MagicMock())
    play_context._attributes = {'connection': 'persistent'}
    play_context._get_attr_connection()
    assert play_context.connection == 'paramiko'

def test_get_attr_connection_no_special_case(play_context):
    play_context._attributes = {'connection': 'local'}
    result = play_context._get_attr_connection()
    assert result == 'local'
    assert play_context.connection == 'local'
