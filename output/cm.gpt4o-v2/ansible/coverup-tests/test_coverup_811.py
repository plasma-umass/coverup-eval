# file: lib/ansible/cli/console.py:121-122
# asked: {"lines": [121, 122], "branches": []}
# gained: {"lines": [121, 122], "branches": []}

import pytest
from ansible.cli.console import ConsoleCLI

def test_get_names():
    args = ['test']
    console_cli = ConsoleCLI(args)
    names = console_cli.get_names()
    assert isinstance(names, list)
    assert 'get_names' in names
