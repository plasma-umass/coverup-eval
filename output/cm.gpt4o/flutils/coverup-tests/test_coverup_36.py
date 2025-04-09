# file flutils/setuputils/cfg.py:157-172
# lines [157, 158, 160, 161, 162, 164, 165, 166, 167, 168, 169, 170, 171, 172]
# branches ['169->170', '169->172']

import os
import pytest
from unittest.mock import patch, mock_open, MagicMock
from flutils.setuputils.cfg import each_sub_command_config

@pytest.fixture
def mock_prep_setup_dir(mocker):
    return mocker.patch('flutils.setuputils.cfg._prep_setup_dir', return_value='/mock/setup/dir')

@pytest.fixture
def mock_get_name(mocker):
    return mocker.patch('flutils.setuputils.cfg._get_name', return_value='mock_name')

@pytest.fixture
def mock_each_setup_cfg_command(mocker):
    return mocker.patch('flutils.setuputils.cfg._each_setup_cfg_command', return_value=iter(['command1', 'command2']))

@pytest.fixture
def mock_isfile(mocker):
    return mocker.patch('os.path.isfile', return_value=True)

@pytest.fixture
def mock_expanduser(mocker):
    return mocker.patch('os.path.expanduser', return_value='/mock/home')

@pytest.fixture
def mock_open_file(mocker):
    m = mock_open(read_data="[section]\nkey=value")
    mocker.patch('builtins.open', m)
    return m

def test_each_sub_command_config(mock_prep_setup_dir, mock_get_name, mock_each_setup_cfg_command, mock_isfile, mock_expanduser, mock_open_file):
    setup_dir = '/mock/setup/dir'
    expected_commands = ['command1', 'command2']
    
    result = list(each_sub_command_config(setup_dir))
    
    assert result == expected_commands
    mock_prep_setup_dir.assert_called_once_with(setup_dir)
    mock_expanduser.assert_called_once_with('~')
    mock_get_name.assert_called_once()
    mock_isfile.assert_called_once_with(os.path.join(setup_dir, 'setup_commands.cfg'))
    mock_each_setup_cfg_command.assert_called_once()
