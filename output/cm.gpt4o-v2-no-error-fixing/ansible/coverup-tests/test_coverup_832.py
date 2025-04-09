# file: lib/ansible/cli/console.py:121-122
# asked: {"lines": [122], "branches": []}
# gained: {"lines": [122], "branches": []}

import pytest
from ansible.cli.console import ConsoleCLI

def test_get_names():
    # Create an instance of ConsoleCLI with minimal required arguments
    cli_instance = ConsoleCLI(args=['test'])

    # Call the get_names method
    names = cli_instance.get_names()

    # Assert that the result is a list and contains some expected attributes/methods
    assert isinstance(names, list)
    assert 'get_names' in names
    assert 'cmdloop' in names  # from cmd.Cmd
    assert 'run' in names  # from CLI

    # Clean up if necessary (not much to clean up in this case)
