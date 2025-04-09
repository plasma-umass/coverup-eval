# file: lib/ansible/cli/console.py:261-273
# asked: {"lines": [261, 273], "branches": []}
# gained: {"lines": [261, 273], "branches": []}

import pytest
from ansible.cli.console import ConsoleCLI

@pytest.fixture
def console_cli(mocker):
    # Mock the required arguments for ConsoleCLI
    mock_args = mocker.Mock()
    return ConsoleCLI(mock_args)

def test_do_shell_executes_default(monkeypatch, console_cli):
    # Mock the default method to verify it gets called
    def mock_default(arg, force):
        assert arg == "ps aux | grep java | wc -l"
        assert force is True

    monkeypatch.setattr(console_cli, 'default', mock_default)
    
    # Call the do_shell method with a sample argument
    console_cli.do_shell("ps aux | grep java | wc -l")
