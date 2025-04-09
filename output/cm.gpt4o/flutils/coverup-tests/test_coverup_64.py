# file flutils/setuputils/cfg.py:157-172
# lines []
# branches ['169->172']

import os
import pytest
from unittest.mock import patch, mock_open, MagicMock
from flutils.setuputils.cfg import each_sub_command_config

@pytest.fixture
def mock_os_path_isfile(mocker):
    return mocker.patch('os.path.isfile')

@pytest.fixture
def mock_config_parser(mocker):
    mock_parser = mocker.patch('flutils.setuputils.cfg.ConfigParser')
    mock_instance = mock_parser.return_value
    mock_instance.read = mocker.MagicMock()
    return mock_instance

@pytest.fixture
def mock_prep_setup_dir(mocker):
    return mocker.patch('flutils.setuputils.cfg._prep_setup_dir', return_value='/mock/setup/dir')

@pytest.fixture
def mock_get_name(mocker):
    return mocker.patch('flutils.setuputils.cfg._get_name', return_value='mock_name')

@pytest.fixture
def mock_each_setup_cfg_command(mocker):
    return mocker.patch('flutils.setuputils.cfg._each_setup_cfg_command', return_value=iter([]))

def test_each_sub_command_config_file_exists(
    mock_os_path_isfile, mock_config_parser, mock_prep_setup_dir, mock_get_name, mock_each_setup_cfg_command
):
    mock_os_path_isfile.side_effect = lambda path: path == '/mock/setup/dir/setup_commands.cfg'
    
    list(each_sub_command_config())

    mock_os_path_isfile.assert_called_with('/mock/setup/dir/setup_commands.cfg')
    mock_config_parser.read.assert_any_call('/mock/setup/dir/setup_commands.cfg')
    mock_each_setup_cfg_command.assert_called_once()

def test_each_sub_command_config_file_not_exists(
    mock_os_path_isfile, mock_config_parser, mock_prep_setup_dir, mock_get_name, mock_each_setup_cfg_command
):
    mock_os_path_isfile.return_value = False
    
    list(each_sub_command_config())

    mock_os_path_isfile.assert_called_with('/mock/setup/dir/setup_commands.cfg')
    mock_config_parser.read.assert_called_once_with('/mock/setup/dir/setup.cfg')
    mock_each_setup_cfg_command.assert_called_once()
