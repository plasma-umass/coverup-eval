# file: lib/ansible/cli/console.py:366-373
# asked: {"lines": [366, 368, 369, 370, 372, 373], "branches": [[368, 369], [368, 372]]}
# gained: {"lines": [366, 368, 369, 370, 372, 373], "branches": [[368, 369], [368, 372]]}

import pytest
from ansible.cli.console import ConsoleCLI
from ansible.module_utils.parsing.convert_bool import boolean
from unittest.mock import patch
from ansible.utils.display import Display

@pytest.fixture
def console_cli():
    return ConsoleCLI(['test'])

def test_do_check_with_arg(console_cli, mocker):
    mock_display = mocker.patch('ansible.utils.display.Display.display')
    mock_v = mocker.patch('ansible.utils.display.Display.v')
    
    console_cli.do_check('yes')
    
    assert console_cli.check_mode == boolean('yes', strict=False)
    mock_display.assert_called_once_with("check mode changed to True")
    mock_v.assert_not_called()

def test_do_check_without_arg(console_cli, mocker):
    mock_display = mocker.patch('ansible.utils.display.Display.display')
    mock_v = mocker.patch('ansible.utils.display.Display.v')
    
    console_cli.check_mode = True
    console_cli.do_check('')
    
    mock_display.assert_called_once_with("Please specify check mode value, e.g. `check yes`")
    mock_v.assert_called_once_with("check mode is currently True.")
