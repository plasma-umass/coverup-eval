# file thefuck/entrypoints/not_configured.py:46-52
# lines [46, 47, 49, 50, 52]
# branches ['49->50', '49->52']

import pytest
from thefuck.entrypoints.not_configured import _get_previous_command
from thefuck.shells import shell
from unittest.mock import Mock

@pytest.fixture
def mock_shell_history(mocker):
    mocker.patch('thefuck.shells.shell.get_history')

def test_get_previous_command_with_history(mock_shell_history):
    shell.get_history.return_value = ['ls', 'cd /', 'python']
    assert _get_previous_command() == 'python'

def test_get_previous_command_without_history(mock_shell_history):
    shell.get_history.return_value = []
    assert _get_previous_command() is None
