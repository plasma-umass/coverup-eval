# file: lib/ansible/cli/console.py:398-401
# asked: {"lines": [398, 400, 401], "branches": []}
# gained: {"lines": [398, 400, 401], "branches": []}

import pytest
from ansible.cli.console import ConsoleCLI
import sys
from io import StringIO

@pytest.fixture
def console_cli(monkeypatch):
    # Mock the required arguments for ConsoleCLI
    monkeypatch.setattr('sys.argv', ['ansible-console'])
    return ConsoleCLI(['ansible-console'])

def test_do_exit(monkeypatch, console_cli):
    # Capture the output
    captured_output = StringIO()
    monkeypatch.setattr(sys, 'stdout', captured_output)

    # Call the method
    result = console_cli.do_exit('')

    # Check the output and return value
    assert captured_output.getvalue() == '\nAnsible-console was exited.\n'
    assert result == -1
