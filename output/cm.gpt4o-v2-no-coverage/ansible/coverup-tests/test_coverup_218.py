# file: lib/ansible/playbook/play_context.py:128-154
# asked: {"lines": [128, 133, 135, 136, 138, 139, 141, 143, 144, 147, 150, 151, 153, 154], "branches": [[135, 136], [135, 138], [150, 151], [150, 153], [153, 0], [153, 154]]}
# gained: {"lines": [128, 133, 135, 136, 138, 139, 141, 143, 144, 147, 150, 151, 153, 154], "branches": [[135, 136], [135, 138], [150, 151], [150, 153], [153, 0], [153, 154]]}

import pytest
from ansible.playbook.play_context import PlayContext
from ansible import context

@pytest.fixture
def mock_context(mocker):
    mocker.patch.object(context, 'CLIARGS', {
        'timeout': '10',
        'private_key_file': '/path/to/key',
        'verbosity': 2,
        'start_at_task': 'task_name'
    })

def test_play_context_init_with_no_passwords(mock_context, mocker):
    mocker.patch('ansible.playbook.play_context.Base.__init__', return_value=None)
    play_context = PlayContext()
    assert play_context.password == ''
    assert play_context.become_pass == ''
    assert play_context._become_plugin is None
    assert play_context.prompt == ''
    assert play_context.success_key == ''
    assert play_context.connection_lockfd is None
    assert play_context.timeout == 10
    assert play_context.private_key_file == '/path/to/key'
    assert play_context.verbosity == 2
    assert play_context.start_at_task == 'task_name'

def test_play_context_init_with_passwords(mock_context, mocker):
    mocker.patch('ansible.playbook.play_context.Base.__init__', return_value=None)
    passwords = {'conn_pass': 'conn_password', 'become_pass': 'become_password'}
    play_context = PlayContext(passwords=passwords)
    assert play_context.password == 'conn_password'
    assert play_context.become_pass == 'become_password'
    assert play_context._become_plugin is None
    assert play_context.prompt == ''
    assert play_context.success_key == ''
    assert play_context.connection_lockfd is None
    assert play_context.timeout == 10
    assert play_context.private_key_file == '/path/to/key'
    assert play_context.verbosity == 2
    assert play_context.start_at_task == 'task_name'

def test_play_context_init_with_play(mocker):
    mocker.patch('ansible.playbook.play_context.Base.__init__', return_value=None)
    play = mocker.Mock()
    play.force_handlers = True
    play_context = PlayContext(play=play)
    assert play_context.force_handlers is True
