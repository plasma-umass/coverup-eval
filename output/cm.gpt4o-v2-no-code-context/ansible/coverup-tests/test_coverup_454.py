# file: lib/ansible/cli/console.py:331-338
# asked: {"lines": [331, 333, 334, 335, 336, 338], "branches": [[333, 334], [333, 338]]}
# gained: {"lines": [331, 333, 334, 335, 336, 338], "branches": [[333, 334], [333, 338]]}

import pytest
from ansible.cli.console import ConsoleCLI
from ansible.utils.display import Display

@pytest.fixture
def console_cli(mocker):
    mock_args = mocker.Mock()
    return ConsoleCLI(mock_args)

@pytest.fixture
def mock_display(mocker):
    return mocker.patch('ansible.utils.display.Display.display')

@pytest.fixture
def mock_v(mocker):
    return mocker.patch('ansible.utils.display.Display.v')

@pytest.fixture
def mock_set_prompt(mocker):
    return mocker.patch.object(ConsoleCLI, 'set_prompt')

def test_do_become_with_arg(console_cli, mock_v, mock_set_prompt, mocker):
    mock_boolean = mocker.patch('ansible.cli.console.boolean', return_value=True)
    console_cli.do_become('yes')
    mock_boolean.assert_called_once_with('yes', strict=False)
    assert console_cli.become == True
    mock_v.assert_called_once_with("become changed to %s" % console_cli.become)
    mock_set_prompt.assert_called_once()

def test_do_become_without_arg(console_cli, mock_display):
    console_cli.do_become('')
    mock_display.assert_called_once_with("Please specify become value, e.g. `become yes`")
