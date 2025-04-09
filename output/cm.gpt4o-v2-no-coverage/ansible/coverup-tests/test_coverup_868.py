# file: lib/ansible/cli/console.py:121-122
# asked: {"lines": [121, 122], "branches": []}
# gained: {"lines": [121, 122], "branches": []}

import pytest
from ansible.cli.console import ConsoleCLI

@pytest.fixture
def console_cli():
    return ConsoleCLI(args=['test'])

def test_get_names(console_cli):
    names = console_cli.get_names()
    assert isinstance(names, list)
    assert 'get_names' in names
    assert 'cmdloop' in names  # cmd.Cmd method
    assert 'do_help' in names  # cmd.Cmd method
