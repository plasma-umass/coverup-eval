# file: lib/ansible/playbook/play_context.py:128-154
# asked: {"lines": [128, 133, 135, 136, 138, 139, 141, 143, 144, 147, 150, 151, 153, 154], "branches": [[135, 136], [135, 138], [150, 151], [150, 153], [153, 0], [153, 154]]}
# gained: {"lines": [128, 133, 135, 136, 138, 139, 141, 143, 144, 147, 150, 151, 153, 154], "branches": [[135, 136], [135, 138], [150, 151], [153, 0], [153, 154]]}

import pytest
from ansible.playbook.play_context import PlayContext
from ansible import context
from ansible.utils.context_objects import CLIArgs

@pytest.fixture
def mock_context_cliargs(monkeypatch):
    mock_cliargs = {
        'timeout': 10,
        'private_key_file': '/path/to/key',
        'verbosity': 2,
        'start_at_task': 'task_name'
    }
    monkeypatch.setattr(context, 'CLIARGS', CLIArgs(mock_cliargs))
    yield
    monkeypatch.undo()

def test_play_context_init_with_passwords_and_play(mock_context_cliargs):
    play = type('Play', (object,), {'force_handlers': True})()
    passwords = {'conn_pass': 'password1', 'become_pass': 'password2'}
    connection_lockfd = 3

    pc = PlayContext(play=play, passwords=passwords, connection_lockfd=connection_lockfd)

    assert pc.password == 'password1'
    assert pc.become_pass == 'password2'
    assert pc.connection_lockfd == connection_lockfd
    assert pc._become_plugin is None
    assert pc.prompt == ''
    assert pc.success_key == ''
    assert pc.force_handlers is True
    assert pc.timeout == 10
    assert pc.private_key_file == '/path/to/key'
    assert pc.verbosity == 2
    assert pc.start_at_task == 'task_name'

def test_play_context_init_without_passwords(mock_context_cliargs):
    play = type('Play', (object,), {'force_handlers': True})()
    connection_lockfd = 3

    pc = PlayContext(play=play, connection_lockfd=connection_lockfd)

    assert pc.password == ''
    assert pc.become_pass == ''
    assert pc.connection_lockfd == connection_lockfd
    assert pc._become_plugin is None
    assert pc.prompt == ''
    assert pc.success_key == ''
    assert pc.force_handlers is True
    assert pc.timeout == 10
    assert pc.private_key_file == '/path/to/key'
    assert pc.verbosity == 2
    assert pc.start_at_task == 'task_name'

def test_play_context_init_without_play(mock_context_cliargs):
    passwords = {'conn_pass': 'password1', 'become_pass': 'password2'}
    connection_lockfd = 3

    pc = PlayContext(passwords=passwords, connection_lockfd=connection_lockfd)

    assert pc.password == 'password1'
    assert pc.become_pass == 'password2'
    assert pc.connection_lockfd == connection_lockfd
    assert pc._become_plugin is None
    assert pc.prompt == ''
    assert pc.success_key == ''
    assert pc.force_handlers is False  # Default value is False
    assert pc.timeout == 10
    assert pc.private_key_file == '/path/to/key'
    assert pc.verbosity == 2
    assert pc.start_at_task == 'task_name'
