# file: lib/ansible/cli/console.py:121-122
# asked: {"lines": [121, 122], "branches": []}
# gained: {"lines": [121, 122], "branches": []}

import pytest
from ansible.cli.console import ConsoleCLI

class TestConsoleCLI:
    @pytest.fixture
    def console_cli(self, mocker):
        mocker.patch.object(ConsoleCLI, '__init__', lambda self, args: None)
        return ConsoleCLI(args=[])

    def test_get_names(self, console_cli):
        names = console_cli.get_names()
        assert isinstance(names, list)
        assert 'get_names' in names
