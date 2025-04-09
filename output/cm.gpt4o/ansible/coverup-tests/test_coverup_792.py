# file lib/ansible/cli/console.py:258-259
# lines [258, 259]
# branches []

import pytest
from ansible.cli.console import ConsoleCLI

def test_emptyline(mocker):
    mocker.patch('ansible.cli.console.CLI.__init__', return_value=None)
    console_cli = ConsoleCLI(args=[])
    result = console_cli.emptyline()
    assert result is None
