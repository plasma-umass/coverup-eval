# file: flutils/setuputils/cfg.py:32-41
# asked: {"lines": [], "branches": [[40, 35]]}
# gained: {"lines": [], "branches": [[40, 35]]}

import pytest
from configparser import ConfigParser
from flutils.setuputils.cfg import _each_setup_cfg_command_section

def test_each_setup_cfg_command_section():
    config_data = """
    [setup.command.test]
    key = value

    [setup.command.another]
    key = value

    [other.section]
    key = value
    """
    parser = ConfigParser()
    parser.read_string(config_data)

    result = list(_each_setup_cfg_command_section(parser))
    
    assert result == [
        ('setup.command.test', 'test'),
        ('setup.command.another', 'another')
    ]

def test_each_setup_cfg_command_section_no_command_name():
    config_data = """
    [setup.command.]
    key = value
    """
    parser = ConfigParser()
    parser.read_string(config_data)

    result = list(_each_setup_cfg_command_section(parser))
    
    assert result == []

