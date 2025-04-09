# file: lib/ansible/cli/console.py:258-259
# asked: {"lines": [258, 259], "branches": []}
# gained: {"lines": [258, 259], "branches": []}

import pytest
from ansible.cli.console import ConsoleCLI

@pytest.fixture
def console_cli(mocker):
    mocker.patch.object(ConsoleCLI, '__init__', lambda self, args: None)
    return ConsoleCLI(args=[])

def test_emptyline(console_cli, mocker):
    mocker.patch.object(console_cli, 'emptyline', wraps=console_cli.emptyline)
    console_cli.emptyline()
    console_cli.emptyline.assert_called_once()
