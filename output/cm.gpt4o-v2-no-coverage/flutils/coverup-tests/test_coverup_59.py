# file: flutils/setuputils/cfg.py:44-79
# asked: {"lines": [], "branches": [[58, 48], [60, 62], [66, 68], [73, 48]]}
# gained: {"lines": [], "branches": [[60, 62], [66, 68], [73, 48]]}

import pytest
from configparser import ConfigParser
from flutils.setuputils.cfg import _each_setup_cfg_command, SetupCfgCommandConfig
from flutils.strutils import underscore_to_camel

@pytest.fixture
def config_parser():
    parser = ConfigParser()
    parser.add_section('setup.command.test')
    parser.set('setup.command.test', 'command', 'echo "Hello, {name}!"')
    parser.set('setup.command.test', 'name', 'test_command')
    parser.set('setup.command.test', 'description', 'This is a test command for {name}.')
    return parser

def test_each_setup_cfg_command(config_parser):
    format_kwargs = {'name': 'World'}
    commands = list(_each_setup_cfg_command(config_parser, format_kwargs))
    
    assert len(commands) == 1
    command = commands[0]
    
    assert command.name == 'test_command'
    assert command.camel == 'TestCommand'
    assert command.description == 'This is a test command for World.'
    assert command.commands == ('echo "Hello, World!"',)

def test_each_setup_cfg_command_no_name(config_parser):
    config_parser.remove_option('setup.command.test', 'name')
    format_kwargs = {'name': 'World'}
    commands = list(_each_setup_cfg_command(config_parser, format_kwargs))
    
    assert len(commands) == 1
    command = commands[0]
    
    assert command.name == 'test'
    assert command.camel == 'Test'
    assert command.description == 'This is a test command for World.'
    assert command.commands == ('echo "Hello, World!"',)

def test_each_setup_cfg_command_no_description(config_parser):
    config_parser.remove_option('setup.command.test', 'description')
    format_kwargs = {'name': 'World'}
    commands = list(_each_setup_cfg_command(config_parser, format_kwargs))
    
    assert len(commands) == 1
    command = commands[0]
    
    assert command.name == 'test_command'
    assert command.camel == 'TestCommand'
    assert command.description == ''
    assert command.commands == ('echo "Hello, World!"',)

def test_each_setup_cfg_command_invalid_identifier(config_parser):
    config_parser.set('setup.command.test', 'name', '123invalid')
    format_kwargs = {'name': 'World'}
    commands = list(_each_setup_cfg_command(config_parser, format_kwargs))
    
    assert len(commands) == 0
