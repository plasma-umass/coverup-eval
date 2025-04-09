# file: lib/ansible/cli/console.py:124-133
# asked: {"lines": [124, 125, 126, 128, 129, 131, 132, 133], "branches": []}
# gained: {"lines": [124, 125, 126, 128, 129, 131, 132, 133], "branches": []}

import pytest
from unittest import mock
from ansible.cli.console import ConsoleCLI

class MockCLI(ConsoleCLI):
    def __init__(self, *args, **kwargs):
        pass

    def display(self, message):
        self.message = message

    def do_exit(self, arg):
        self.exited = True

@pytest.fixture
def console_cli():
    return MockCLI()

def test_cmdloop_normal(monkeypatch, console_cli):
    with mock.patch('cmd.Cmd.cmdloop', return_value=None) as mock_cmdloop:
        console_cli.cmdloop()
        mock_cmdloop.assert_called_once()

def test_cmdloop_keyboard_interrupt(monkeypatch, console_cli):
    call_count = 0

    def mock_cmdloop(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        if call_count == 1:
            raise KeyboardInterrupt
        return None

    monkeypatch.setattr('cmd.Cmd.cmdloop', mock_cmdloop)
    console_cli.cmdloop()
    assert call_count == 2  # cmdloop should be called twice

def test_cmdloop_eof_error(monkeypatch, console_cli):
    def mock_cmdloop(*args, **kwargs):
        raise EOFError

    monkeypatch.setattr('cmd.Cmd.cmdloop', mock_cmdloop)
    console_cli.cmdloop()
    assert console_cli.message == "[Ansible-console was exited]"
    assert console_cli.exited
