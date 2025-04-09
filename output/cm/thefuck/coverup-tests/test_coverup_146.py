# file thefuck/types.py:232-246
# lines [246]
# branches ['239->246']

import pytest
from thefuck.types import CorrectedCommand
from thefuck import shells
from thefuck.conf import settings


@pytest.fixture
def mock_settings(mocker):
    return mocker.patch('thefuck.types.settings')


@pytest.fixture
def mock_get_alias(mocker):
    return mocker.patch('thefuck.types.get_alias', return_value='fuck')


@pytest.fixture
def mock_shell_quote(mocker):
    return mocker.patch('thefuck.types.shell.quote', return_value='quoted_script')


@pytest.fixture
def mock_shell_or(mocker):
    return mocker.patch('thefuck.types.shell.or_', return_value='script || fuck')


def test_corrected_command_get_script_without_repeat(mock_settings, mock_get_alias, mock_shell_quote, mock_shell_or):
    mock_settings.repeat = False
    corrected_command = CorrectedCommand('ls -la', None, 0)
    script = corrected_command._get_script()
    assert script == 'ls -la'
    mock_shell_or.assert_not_called()


def test_corrected_command_get_script_with_repeat(mock_settings, mock_get_alias, mock_shell_quote, mock_shell_or):
    mock_settings.repeat = True
    mock_settings.debug = False
    corrected_command = CorrectedCommand('ls -la', None, 0)
    script = corrected_command._get_script()
    assert script == 'script || fuck'
    mock_shell_or.assert_called_once_with('ls -la', 'fuck --repeat --force-command quoted_script')


def test_corrected_command_get_script_with_repeat_and_debug(mock_settings, mock_get_alias, mock_shell_quote, mock_shell_or):
    mock_settings.repeat = True
    mock_settings.debug = True
    corrected_command = CorrectedCommand('ls -la', None, 0)
    script = corrected_command._get_script()
    assert script == 'script || fuck'
    mock_shell_or.assert_called_once_with('ls -la', 'fuck --repeat --debug --force-command quoted_script')
