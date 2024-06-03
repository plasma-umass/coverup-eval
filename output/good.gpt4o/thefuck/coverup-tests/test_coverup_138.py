# file thefuck/entrypoints/fix_command.py:29-48
# lines [29, 31, 32, 33, 34, 36, 37, 38, 39, 40, 42, 43, 45, 46, 48]
# branches ['45->46', '45->48']

import pytest
from unittest import mock
from thefuck.entrypoints.fix_command import fix_command
from thefuck import logs, types
from thefuck.exceptions import EmptyCommand

@pytest.fixture
def mock_settings(mocker):
    return mocker.patch('thefuck.entrypoints.fix_command.settings')

@pytest.fixture
def mock_logs(mocker):
    return mocker.patch('thefuck.entrypoints.fix_command.logs')

@pytest.fixture
def mock_get_raw_command(mocker):
    return mocker.patch('thefuck.entrypoints.fix_command._get_raw_command')

@pytest.fixture
def mock_get_corrected_commands(mocker):
    return mocker.patch('thefuck.entrypoints.fix_command.get_corrected_commands')

@pytest.fixture
def mock_select_command(mocker):
    return mocker.patch('thefuck.entrypoints.fix_command.select_command')

@pytest.fixture
def mock_sys_exit(mocker):
    return mocker.patch('sys.exit')

def test_fix_command_empty_command(mock_settings, mock_logs, mock_get_raw_command, mocker):
    mock_get_raw_command.return_value = ''
    mocker.patch('thefuck.entrypoints.fix_command.types.Command.from_raw_script', side_effect=EmptyCommand)
    
    fix_command(mock.Mock())
    
    mock_logs.debug.assert_called_with('Empty command, nothing to do')

def test_fix_command_no_selected_command(mock_settings, mock_logs, mock_get_raw_command, mock_get_corrected_commands, mock_select_command, mock_sys_exit):
    mock_get_raw_command.return_value = 'some command'
    mock_get_corrected_commands.return_value = ['corrected command']
    mock_select_command.return_value = None
    
    fix_command(mock.Mock())
    
    mock_sys_exit.assert_called_once_with(1)

def test_fix_command_selected_command(mock_settings, mock_logs, mock_get_raw_command, mock_get_corrected_commands, mock_select_command):
    mock_get_raw_command.return_value = 'some command'
    mock_get_corrected_commands.return_value = ['corrected command']
    mock_selected_command = mock.Mock()
    mock_select_command.return_value = mock_selected_command
    
    fix_command(mock.Mock())
    
    mock_selected_command.run.assert_called_once()
