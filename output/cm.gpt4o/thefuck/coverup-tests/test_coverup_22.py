# file thefuck/types.py:232-246
# lines [232, 239, 240, 241, 242, 243, 244, 246]
# branches ['239->240', '239->246']

import pytest
from unittest import mock
from thefuck.types import CorrectedCommand

@pytest.fixture
def mock_settings(mocker):
    return mocker.patch('thefuck.types.settings')

@pytest.fixture
def mock_shell(mocker):
    return mocker.patch('thefuck.types.shell')

@pytest.fixture
def mock_get_alias(mocker):
    return mocker.patch('thefuck.types.get_alias')

def test_get_script_with_repeat(mock_settings, mock_shell, mock_get_alias):
    mock_settings.repeat = True
    mock_settings.debug = False
    mock_get_alias.return_value = 'fuck'
    mock_shell.quote.return_value = 'quoted_script'
    mock_shell.or_.return_value = 'or_script'

    command = CorrectedCommand(script='original_script', side_effect=None, priority=0)
    result = command._get_script()

    mock_get_alias.assert_called_once()
    mock_shell.quote.assert_called_once_with('original_script')
    mock_shell.or_.assert_called_once_with('original_script', 'fuck --repeat --force-command quoted_script')
    assert result == 'or_script'

def test_get_script_without_repeat(mock_settings):
    mock_settings.repeat = False

    command = CorrectedCommand(script='original_script', side_effect=None, priority=0)
    result = command._get_script()

    assert result == 'original_script'
