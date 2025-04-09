# file: flutils/setuputils/cfg.py:32-41
# asked: {"lines": [], "branches": [[40, 35]]}
# gained: {"lines": [], "branches": [[40, 35]]}

import pytest
from configparser import ConfigParser
from flutils.setuputils.cfg import _each_setup_cfg_command_section

def test_each_setup_cfg_command_section_with_command_section():
    parser = ConfigParser()
    parser.add_section('setup.command.test_command')
    parser.set('setup.command.test_command', 'key', 'value')

    result = list(_each_setup_cfg_command_section(parser))
    
    assert len(result) == 1
    assert result[0] == ('setup.command.test_command', 'test_command')

def test_each_setup_cfg_command_section_without_command_section():
    parser = ConfigParser()
    parser.add_section('setup.other_section')
    parser.set('setup.other_section', 'key', 'value')

    result = list(_each_setup_cfg_command_section(parser))
    
    assert len(result) == 0

def test_each_setup_cfg_command_section_with_empty_command_name():
    parser = ConfigParser()
    parser.add_section('setup.command.')
    parser.set('setup.command.', 'key', 'value')

    result = list(_each_setup_cfg_command_section(parser))
    
    assert len(result) == 0
