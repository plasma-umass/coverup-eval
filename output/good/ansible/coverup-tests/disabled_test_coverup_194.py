# file lib/ansible/playbook/play_context.py:339-355
# lines [339, 341, 342, 343, 345, 346, 349, 350, 352, 353, 355]
# branches ['342->343', '342->349', '345->346', '345->352', '349->350', '349->352', '352->353', '352->355']

import pytest
from unittest.mock import patch, MagicMock
from ansible.playbook.play_context import PlayContext

@pytest.fixture
def play_context():
    return PlayContext()

def test_get_attr_connection_smart_with_controlpersist(play_context, mocker):
    mocker.patch('ansible.playbook.play_context.check_for_controlpersist', return_value=True)
    play_context._attributes['connection'] = 'smart'
    assert play_context._get_attr_connection() == 'ssh'
    assert play_context.connection == 'ssh'

def test_get_attr_connection_smart_without_controlpersist_and_paramiko(play_context, mocker):
    mocker.patch('ansible.playbook.play_context.check_for_controlpersist', return_value=False)
    mocker.patch('ansible.playbook.play_context.paramiko', MagicMock())
    play_context._attributes['connection'] = 'smart'
    assert play_context._get_attr_connection() == 'paramiko'
    assert play_context.connection == 'paramiko'

def test_get_attr_connection_persistent_with_paramiko(play_context, mocker):
    mocker.patch('ansible.playbook.play_context.paramiko', MagicMock())
    play_context._attributes['connection'] = 'persistent'
    assert play_context._get_attr_connection() == 'paramiko'
    assert play_context.connection == 'paramiko'

def test_get_attr_connection_persistent_without_paramiko(play_context, mocker):
    mocker.patch('ansible.playbook.play_context.paramiko', None)
    play_context._attributes['connection'] = 'persistent'
    assert play_context._get_attr_connection() == 'persistent'
    assert 'connection' not in play_context.__dict__
