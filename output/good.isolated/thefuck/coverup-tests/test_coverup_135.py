# file thefuck/entrypoints/alias.py:7-22
# lines [8, 9, 12, 14, 15, 16, 17, 18, 20, 22]
# branches ['8->9', '8->12', '14->15', '14->22', '15->16', '15->17', '17->18', '17->20']

import pytest
from thefuck.entrypoints.alias import _get_alias
from thefuck.shells import shell
from unittest.mock import patch
import six
from thefuck.types import Command
from mock import Mock

class Args:
    alias = 'fuck'
    enable_experimental_instant_mode = False

@pytest.fixture
def mock_warn():
    with patch('thefuck.entrypoints.alias.warn') as mock:
        yield mock

@pytest.fixture
def mock_shell_alias():
    with patch('thefuck.entrypoints.alias.shell') as mock:
        mock.app_alias.return_value = 'alias fuck=\'eval $(thefuck $(fc -ln -1)); fc -R\''
        yield mock

@pytest.fixture
def mock_which():
    with patch('thefuck.entrypoints.alias.which') as mock:
        mock.return_value = True
        yield mock

@pytest.fixture
def mock_instant_mode_alias():
    with patch('thefuck.entrypoints.alias.shell.instant_mode_alias') as mock:
        mock.return_value = 'alias fuck=\'thefuck --enable-experimental-instant-mode\''
        yield mock

def test_get_alias_py2(mock_warn, mock_shell_alias):
    with patch.object(six, 'PY2', True):
        _get_alias(Args())
    mock_warn.assert_called_once_with("The Fuck will drop Python 2 support soon, more details https://github.com/nvbn/thefuck/issues/685")
    mock_shell_alias.app_alias.assert_called_once_with('fuck')

def test_get_alias_py3_no_instant_mode(mock_warn, mock_shell_alias):
    with patch.object(six, 'PY2', False):
        alias = _get_alias(Args())
    mock_warn.assert_not_called()
    mock_shell_alias.app_alias.assert_called_once_with('fuck')
    assert alias == 'alias fuck=\'eval $(thefuck $(fc -ln -1)); fc -R\''

def test_get_alias_py3_instant_mode_no_script(mock_warn, mock_shell_alias, mock_which):
    args = Args()
    args.enable_experimental_instant_mode = True
    with patch.object(six, 'PY2', False):
        with patch.object(mock_which, 'return_value', False):
            _get_alias(args)
    mock_warn.assert_called_once_with("Instant mode requires `script` app")
    mock_shell_alias.app_alias.assert_called_once_with('fuck')

def test_get_alias_py3_instant_mode_with_script(mock_warn, mock_shell_alias, mock_which, mock_instant_mode_alias):
    args = Args()
    args.enable_experimental_instant_mode = True
    with patch.object(six, 'PY2', False):
        alias = _get_alias(args)
    mock_warn.assert_not_called()
    mock_instant_mode_alias.assert_called_once_with('fuck')
    assert alias == 'alias fuck=\'thefuck --enable-experimental-instant-mode\''
