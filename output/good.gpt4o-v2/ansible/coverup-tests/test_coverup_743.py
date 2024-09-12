# file: lib/ansible/cli/console.py:398-401
# asked: {"lines": [398, 400, 401], "branches": []}
# gained: {"lines": [398, 400, 401], "branches": []}

import pytest
from ansible.cli.console import ConsoleCLI
import sys
from io import StringIO

@pytest.fixture
def console_cli():
    return ConsoleCLI(['test'])

def test_do_exit(console_cli, monkeypatch):
    # Capture the output
    output = StringIO()
    monkeypatch.setattr(sys, 'stdout', output)

    # Call the method
    result = console_cli.do_exit('')

    # Check the output
    assert output.getvalue() == '\nAnsible-console was exited.\n'
    # Check the return value
    assert result == -1
