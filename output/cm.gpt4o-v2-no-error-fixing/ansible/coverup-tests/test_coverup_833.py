# file: lib/ansible/cli/console.py:258-259
# asked: {"lines": [259], "branches": []}
# gained: {"lines": [259], "branches": []}

import pytest
from ansible.cli.console import ConsoleCLI

@pytest.fixture
def console_cli():
    args = ['test']
    return ConsoleCLI(args)

def test_emptyline(console_cli):
    assert console_cli.emptyline() is None
