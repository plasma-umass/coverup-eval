# file flutils/setuputils/cfg.py:157-172
# lines [157, 158, 160, 161, 162, 164, 165, 166, 167, 168, 169, 170, 171, 172]
# branches ['169->170', '169->172']

import os
from configparser import ConfigParser
from typing import Optional, Union, Generator
from unittest.mock import MagicMock
import pytest

# Assuming the module flutils.setuputils.cfg exists and contains the following functions:
# _prep_setup_dir, _get_name, _each_setup_cfg_command, and SetupCfgCommandConfig
# If not, they should be mocked or implemented accordingly.
from flutils.setuputils.cfg import each_sub_command_config, _prep_setup_dir, _get_name, _each_setup_cfg_command, SetupCfgCommandConfig

@pytest.fixture
def setup_dir(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    return d

@pytest.fixture
def setup_cfg_file(setup_dir):
    setup_cfg_path = setup_dir / 'setup.cfg'
    with open(setup_cfg_path, 'w') as f:
        f.write('[metadata]\nname = test_package\n')
    return setup_cfg_path

@pytest.fixture
def setup_commands_cfg_file(setup_dir):
    setup_commands_cfg_path = setup_dir / 'setup_commands.cfg'
    with open(setup_commands_cfg_path, 'w') as f:
        f.write('[aliases]\ncmd1 = command1\ncmd2 = command2\n')
    return setup_commands_cfg_path

def test_each_sub_command_config_with_setup_commands_cfg_file(mocker, setup_dir, setup_cfg_file, setup_commands_cfg_file):
    # Mocking the _prep_setup_dir, _get_name, and _each_setup_cfg_command functions
    mocker.patch('flutils.setuputils.cfg._prep_setup_dir', return_value=str(setup_dir))
    mocker.patch('flutils.setuputils.cfg._get_name', return_value='test_package')
    mock_each_setup_cfg_command = mocker.patch('flutils.setuputils.cfg._each_setup_cfg_command', return_value=iter([('cmd1', 'command1'), ('cmd2', 'command2')]))

    # Call the function under test
    result = list(each_sub_command_config(setup_dir=setup_dir))

    # Assertions to verify the postconditions
    assert mock_each_setup_cfg_command.called
    assert result == [('cmd1', 'command1'), ('cmd2', 'command2')]
