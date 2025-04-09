# file: lib/ansible/cli/console.py:258-259
# asked: {"lines": [258, 259], "branches": []}
# gained: {"lines": [258, 259], "branches": []}

import pytest
from ansible.cli.console import ConsoleCLI

def test_emptyline():
    cli = ConsoleCLI(args=['test'])
    assert cli.emptyline() is None
