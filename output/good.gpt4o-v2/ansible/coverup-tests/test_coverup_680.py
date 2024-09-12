# file: lib/ansible/cli/console.py:115-119
# asked: {"lines": [115, 116, 117, 118, 119], "branches": []}
# gained: {"lines": [115, 116, 117, 118, 119], "branches": []}

import pytest
from ansible.cli.console import ConsoleCLI
from ansible.utils.display import Display
from ansible.cli import CLI

@pytest.fixture
def mock_display(mocker):
    return mocker.patch('ansible.cli.console.display', new_callable=Display)

@pytest.fixture
def mock_validate_conflicts(mocker):
    return mocker.patch.object(ConsoleCLI, 'validate_conflicts', return_value=None)

@pytest.fixture
def console_cli(mocker):
    mocker.patch.object(CLI, 'init_parser', return_value=None)
    cli = ConsoleCLI(['test'])
    cli.parser = mocker.Mock()
    cli.parser.prog = 'ansible-console'
    return cli

def test_post_process_args(console_cli, mock_display, mock_validate_conflicts):
    class MockOptions:
        verbosity = 3

    options = MockOptions()
    processed_options = console_cli.post_process_args(options)

    assert processed_options == options
    assert mock_display.verbosity == 3
    mock_validate_conflicts.assert_called_once_with(options, runas_opts=True, fork_opts=True)
