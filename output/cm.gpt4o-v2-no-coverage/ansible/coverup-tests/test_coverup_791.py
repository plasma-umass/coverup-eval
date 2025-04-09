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
    mock_stdout = StringIO()
    monkeypatch.setattr(sys, 'stdout', mock_stdout)

    # Call the method
    result = console_cli.do_exit('')

    # Check the output and return value
    assert mock_stdout.getvalue() == '\nAnsible-console was exited.\n'
    assert result == -1
