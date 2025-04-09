# file: lib/ansible/cli/console.py:366-373
# asked: {"lines": [366, 368, 369, 370, 372, 373], "branches": [[368, 369], [368, 372]]}
# gained: {"lines": [366, 368, 369, 370, 372, 373], "branches": [[368, 369], [368, 372]]}

import pytest
from unittest import mock
from ansible.cli.console import ConsoleCLI
from ansible.utils.display import Display

@pytest.fixture
def console_cli():
    return ConsoleCLI(args=['dummy'])

def test_do_check_with_argument(monkeypatch, console_cli):
    display = Display()
    monkeypatch.setattr('ansible.cli.console.display', display)
    mock_display = mock.Mock()
    monkeypatch.setattr(display, 'display', mock_display)
    
    console_cli.do_check('yes')
    
    assert console_cli.check_mode is True
    mock_display.assert_called_with("check mode changed to True")

def test_do_check_without_argument(monkeypatch, console_cli):
    display = Display()
    monkeypatch.setattr('ansible.cli.console.display', display)
    mock_display = mock.Mock()
    mock_v = mock.Mock()
    monkeypatch.setattr(display, 'display', mock_display)
    monkeypatch.setattr(display, 'v', mock_v)
    
    console_cli.check_mode = False
    console_cli.do_check('')
    
    mock_display.assert_called_with("Please specify check mode value, e.g. `check yes`")
    mock_v.assert_called_with("check mode is currently False.")
