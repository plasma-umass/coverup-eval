# file thefuck/entrypoints/alias.py:7-22
# lines [7, 8, 9, 12, 14, 15, 16, 17, 18, 20, 22]
# branches ['8->9', '8->12', '14->15', '14->22', '15->16', '15->17', '17->18', '17->20']

import pytest
import six
from unittest.mock import patch, MagicMock
from thefuck.entrypoints.alias import _get_alias

@pytest.fixture
def mock_shell(mocker):
    return mocker.patch('thefuck.entrypoints.alias.shell')

@pytest.fixture
def mock_warn(mocker):
    return mocker.patch('thefuck.entrypoints.alias.warn')

@pytest.fixture
def mock_which(mocker):
    return mocker.patch('thefuck.entrypoints.alias.which')

def test_get_alias_py2_warning(mock_shell, mock_warn):
    known_args = MagicMock()
    known_args.alias = 'test_alias'
    known_args.enable_experimental_instant_mode = False

    with patch('six.PY2', True):
        alias = _get_alias(known_args)
        mock_warn.assert_called_once_with("The Fuck will drop Python 2 support soon, more details https://github.com/nvbn/thefuck/issues/685")
        mock_shell.app_alias.assert_called_once_with('test_alias')
        assert alias == mock_shell.app_alias.return_value

def test_get_alias_instant_mode_py2_warning(mock_shell, mock_warn):
    known_args = MagicMock()
    known_args.alias = 'test_alias'
    known_args.enable_experimental_instant_mode = True

    with patch('six.PY2', True):
        alias = _get_alias(known_args)
        mock_warn.assert_any_call("The Fuck will drop Python 2 support soon, more details https://github.com/nvbn/thefuck/issues/685")
        mock_warn.assert_any_call("Instant mode requires Python 3")
        mock_shell.app_alias.assert_called_once_with('test_alias')
        assert alias == mock_shell.app_alias.return_value

def test_get_alias_instant_mode_no_script(mock_shell, mock_warn, mock_which):
    known_args = MagicMock()
    known_args.alias = 'test_alias'
    known_args.enable_experimental_instant_mode = True

    with patch('six.PY2', False):
        mock_which.return_value = None
        alias = _get_alias(known_args)
        mock_warn.assert_called_once_with("Instant mode requires `script` app")
        mock_shell.app_alias.assert_called_once_with('test_alias')
        assert alias == mock_shell.app_alias.return_value

def test_get_alias_instant_mode_with_script(mock_shell, mock_warn, mock_which):
    known_args = MagicMock()
    known_args.alias = 'test_alias'
    known_args.enable_experimental_instant_mode = True

    with patch('six.PY2', False):
        mock_which.return_value = 'script'
        alias = _get_alias(known_args)
        mock_shell.instant_mode_alias.assert_called_once_with('test_alias')
        assert alias == mock_shell.instant_mode_alias.return_value
