# file: flutils/setuputils/cfg.py:157-172
# asked: {"lines": [160, 161, 162, 164, 165, 166, 167, 168, 169, 170, 171, 172], "branches": [[169, 170], [169, 172]]}
# gained: {"lines": [160, 161, 162, 164, 165, 166, 167, 168, 169, 170, 171, 172], "branches": [[169, 170], [169, 172]]}

import os
import pytest
from unittest.mock import patch, mock_open, MagicMock
from flutils.setuputils.cfg import each_sub_command_config

@pytest.fixture
def mock_prep_setup_dir(monkeypatch):
    def mock_prep_setup_dir(setup_dir):
        return setup_dir or '/mock/setup/dir'
    monkeypatch.setattr('flutils.setuputils.cfg._prep_setup_dir', mock_prep_setup_dir)

@pytest.fixture
def mock_get_name(monkeypatch):
    def mock_get_name(parser, setup_cfg_path):
        return 'mock_name'
    monkeypatch.setattr('flutils.setuputils.cfg._get_name', mock_get_name)

@pytest.fixture
def mock_each_setup_cfg_command(monkeypatch):
    def mock_each_setup_cfg_command(parser, format_kwargs):
        yield 'mock_command'
    monkeypatch.setattr('flutils.setuputils.cfg._each_setup_cfg_command', mock_each_setup_cfg_command)

@pytest.fixture
def mock_config_parser(monkeypatch):
    mock_parser = MagicMock()
    monkeypatch.setattr('flutils.setuputils.cfg.ConfigParser', lambda: mock_parser)
    return mock_parser

def test_each_sub_command_config_with_setup_commands_cfg(mock_prep_setup_dir, mock_get_name, mock_each_setup_cfg_command, mock_config_parser):
    setup_dir = '/mock/setup/dir'
    setup_cfg_content = "[metadata]\nname = mock_name"
    setup_commands_cfg_content = "[command]\noption = value"

    with patch('builtins.open', mock_open(read_data=setup_cfg_content)) as mock_file:
        with patch('os.path.isfile', return_value=True):
            with patch('builtins.open', mock_open(read_data=setup_commands_cfg_content)) as mock_file_commands:
                result = list(each_sub_command_config(setup_dir))
                assert result == ['mock_command']
                mock_config_parser.read.assert_any_call(os.path.join(setup_dir, 'setup.cfg'))
                mock_config_parser.read.assert_any_call(os.path.join(setup_dir, 'setup_commands.cfg'))

def test_each_sub_command_config_without_setup_commands_cfg(mock_prep_setup_dir, mock_get_name, mock_each_setup_cfg_command, mock_config_parser):
    setup_dir = '/mock/setup/dir'
    setup_cfg_content = "[metadata]\nname = mock_name"

    with patch('builtins.open', mock_open(read_data=setup_cfg_content)) as mock_file:
        with patch('os.path.isfile', return_value=False):
            result = list(each_sub_command_config(setup_dir))
            assert result == ['mock_command']
            mock_config_parser.read.assert_called_once_with(os.path.join(setup_dir, 'setup.cfg'))
