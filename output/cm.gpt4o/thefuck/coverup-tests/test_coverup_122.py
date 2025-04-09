# file thefuck/types.py:248-262
# lines [254, 255, 256, 257, 259, 260, 262]
# branches ['254->255', '254->256', '256->257', '256->259']

import pytest
import os
import sys
from unittest import mock
from thefuck.types import CorrectedCommand

@pytest.fixture
def mock_settings(mocker):
    return mocker.patch('thefuck.types.settings')

@pytest.fixture
def mock_shell(mocker):
    return mocker.patch('thefuck.types.shell')

@pytest.fixture
def mock_logs(mocker):
    return mocker.patch('thefuck.types.logs')

@pytest.fixture
def mock_command(mocker):
    return mocker.Mock()

@pytest.fixture
def corrected_command():
    class TestCorrectedCommand(CorrectedCommand):
        def __init__(self, script, side_effect=None):
            self.script = script
            self.side_effect = side_effect

        def _get_script(self):
            return self.script

    return TestCorrectedCommand

def test_corrected_command_run(mock_settings, mock_shell, mock_logs, mock_command, corrected_command):
    # Arrange
    script = 'echo test'
    side_effect = mock.Mock()
    mock_settings.alter_history = True
    corrected_cmd = corrected_command(script, side_effect)

    # Act
    with mock.patch('sys.stdout', new_callable=mock.MagicMock()) as mock_stdout:
        corrected_cmd.run(mock_command)

    # Assert
    side_effect.assert_called_once_with(mock_command, script)
    mock_shell.put_to_history.assert_called_once_with(script)
    mock_logs.debug.assert_called_once_with(u'PYTHONIOENCODING: {}'.format(
        os.environ.get('PYTHONIOENCODING', '!!not-set!!')))
    mock_stdout.write.assert_called_once_with(script)
