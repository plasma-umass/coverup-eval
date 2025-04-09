# file: flutils/setuputils/cfg.py:157-172
# asked: {"lines": [160, 161, 162, 164, 165, 166, 167, 168, 169, 170, 171, 172], "branches": [[169, 170], [169, 172]]}
# gained: {"lines": [160, 161, 162, 164, 165, 166, 167, 168, 169, 170, 171, 172], "branches": [[169, 170], [169, 172]]}

import os
import pytest
from configparser import ConfigParser
from unittest.mock import patch, mock_open
from flutils.setuputils.cfg import each_sub_command_config, _prep_setup_dir, _get_name, _each_setup_cfg_command

@pytest.fixture
def mock_setup_dir(tmp_path):
    setup_dir = tmp_path / "project"
    setup_dir.mkdir()
    (setup_dir / "setup.py").write_text("")
    return setup_dir

@pytest.fixture
def mock_setup_cfg(mock_setup_dir):
    setup_cfg_path = mock_setup_dir / "setup.cfg"
    setup_cfg_path.write_text("[metadata]\nname = test_project\n")
    return setup_cfg_path

@pytest.fixture
def mock_setup_commands_cfg(mock_setup_dir):
    setup_commands_cfg_path = mock_setup_dir / "setup_commands.cfg"
    setup_commands_cfg_path.write_text("[command1]\ncommand = echo 'Hello, World!'\n")
    return setup_commands_cfg_path

def test_each_sub_command_config_with_setup_cfg(mock_setup_dir, mock_setup_cfg, mock_setup_commands_cfg):
    with patch('flutils.setuputils.cfg._prep_setup_dir', return_value=str(mock_setup_dir)), \
         patch('flutils.setuputils.cfg._get_name', return_value='test_project'), \
         patch('flutils.setuputils.cfg._each_setup_cfg_command', return_value=iter([])) as mock_each_command:
        
        result = list(each_sub_command_config(setup_dir=mock_setup_dir))
        
        assert mock_each_command.called
        assert len(result) == 0

def test_each_sub_command_config_without_setup_commands_cfg(mock_setup_dir, mock_setup_cfg):
    with patch('flutils.setuputils.cfg._prep_setup_dir', return_value=str(mock_setup_dir)), \
         patch('flutils.setuputils.cfg._get_name', return_value='test_project'), \
         patch('flutils.setuputils.cfg._each_setup_cfg_command', return_value=iter([])) as mock_each_command:
        
        result = list(each_sub_command_config(setup_dir=mock_setup_dir))
        
        assert mock_each_command.called
        assert len(result) == 0

def test_each_sub_command_config_no_setup_py():
    with pytest.raises(FileNotFoundError):
        list(each_sub_command_config(setup_dir=None))

def test_each_sub_command_config_no_metadata_section(mock_setup_dir):
    setup_cfg_path = mock_setup_dir / "setup.cfg"
    setup_cfg_path.write_text("")
    
    with patch('flutils.setuputils.cfg._prep_setup_dir', return_value=str(mock_setup_dir)), \
         patch('flutils.setuputils.cfg._get_name', side_effect=LookupError):
        
        with pytest.raises(LookupError):
            list(each_sub_command_config(setup_dir=mock_setup_dir))
