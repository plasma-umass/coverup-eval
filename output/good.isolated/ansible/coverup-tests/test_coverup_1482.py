# file lib/ansible/cli/console.py:258-259
# lines [259]
# branches []

import pytest
from ansible.cli.console import ConsoleCLI

@pytest.fixture
def console_cli(mocker):
    mocker.patch('ansible.cli.console.CLI.__init__', return_value=None)
    mocker.patch('cmd.Cmd.__init__', return_value=None)
    mocker.patch('ansible.cli.console.ConsoleCLI.parse', return_value=None)
    return ConsoleCLI(args=[])

def test_emptyline(console_cli):
    assert console_cli.emptyline() is None
