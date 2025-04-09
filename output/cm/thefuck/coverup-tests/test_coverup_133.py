# file thefuck/types.py:232-246
# lines [239, 240, 241, 242, 243, 244, 246]
# branches ['239->240', '239->246']

import pytest
from thefuck.types import CorrectedCommand
from thefuck.shells import shell
from thefuck.conf import settings


@pytest.fixture
def mock_settings(mocker):
    return mocker.patch('thefuck.types.settings')


@pytest.fixture
def mock_get_alias(mocker):
    return mocker.patch('thefuck.types.get_alias', return_value='fuck')


@pytest.fixture
def mock_shell_quote(mocker):
    return mocker.patch('thefuck.shells.shell.quote', side_effect=lambda x: x)


def test_corrected_command_get_script_with_repeat(mock_settings, mock_get_alias, mock_shell_quote):
    mock_settings.repeat = True
    mock_settings.debug = False
    command = CorrectedCommand('ls', None, 0)
    script = command._get_script()
    assert script == 'ls || fuck --repeat --force-command ls'

    mock_settings.debug = True
    script = command._get_script()
    assert script == 'ls || fuck --repeat --debug --force-command ls'
