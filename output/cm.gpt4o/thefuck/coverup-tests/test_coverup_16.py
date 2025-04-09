# file thefuck/entrypoints/not_configured.py:46-52
# lines [46, 47, 49, 50, 52]
# branches ['49->50', '49->52']

import pytest
from unittest import mock
from thefuck.entrypoints import not_configured

def test_get_previous_command_with_history(mocker):
    mocker.patch('thefuck.entrypoints.not_configured.shell.get_history', return_value=['ls', 'cd /'])
    result = not_configured._get_previous_command()
    assert result == 'cd /'

def test_get_previous_command_without_history(mocker):
    mocker.patch('thefuck.entrypoints.not_configured.shell.get_history', return_value=[])
    result = not_configured._get_previous_command()
    assert result is None
