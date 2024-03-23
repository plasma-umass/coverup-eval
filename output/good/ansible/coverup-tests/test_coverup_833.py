# file lib/ansible/cli/console.py:121-122
# lines [121, 122]
# branches []

import pytest
from ansible.cli.console import ConsoleCLI
from unittest.mock import MagicMock

@pytest.fixture
def console_cli(mocker):
    mocker.patch('ansible.cli.console.CLI.__init__', return_value=None)
    cli = ConsoleCLI(['console'])
    return cli

def test_get_names(console_cli):
    names = console_cli.get_names()
    assert isinstance(names, list)
    assert 'do_help' in names  # Assuming 'do_help' is a method in ConsoleCLI
    assert 'get_names' in names
