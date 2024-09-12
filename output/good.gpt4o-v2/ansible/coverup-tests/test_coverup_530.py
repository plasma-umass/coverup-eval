# file: lib/ansible/cli/console.py:331-338
# asked: {"lines": [331, 333, 334, 335, 336, 338], "branches": [[333, 334], [333, 338]]}
# gained: {"lines": [331, 333, 334, 335, 336, 338], "branches": [[333, 334], [333, 338]]}

import pytest
from ansible.cli.console import ConsoleCLI
from ansible.module_utils.parsing.convert_bool import boolean
from ansible.utils.display import Display
from unittest.mock import patch, MagicMock

@pytest.fixture
def console_cli():
    return ConsoleCLI(['test'])

def test_do_become_with_arg(console_cli, mocker):
    mocker.patch.object(Display, 'v')
    mocker.patch.object(ConsoleCLI, 'set_prompt')
    
    console_cli.do_become('yes')
    
    assert console_cli.become is True
    Display.v.assert_called_once_with("become changed to True")
    console_cli.set_prompt.assert_called_once()

def test_do_become_without_arg(console_cli, mocker):
    mocker.patch.object(Display, 'display')
    
    console_cli.do_become('')
    
    Display.display.assert_called_once_with("Please specify become value, e.g. `become yes`")
