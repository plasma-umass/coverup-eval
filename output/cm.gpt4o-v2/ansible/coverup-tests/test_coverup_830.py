# file: lib/ansible/cli/console.py:258-259
# asked: {"lines": [258, 259], "branches": []}
# gained: {"lines": [258, 259], "branches": []}

import pytest
from ansible.cli.console import ConsoleCLI

@pytest.fixture
def console_cli():
    return ConsoleCLI(['test'])

def test_emptyline(console_cli):
    # Call the emptyline method and assert it returns None
    assert console_cli.emptyline() is None
