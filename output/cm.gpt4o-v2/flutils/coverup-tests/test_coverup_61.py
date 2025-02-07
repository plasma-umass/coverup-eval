# file: flutils/setuputils/cfg.py:44-79
# asked: {"lines": [], "branches": [[58, 48], [66, 68], [73, 48]]}
# gained: {"lines": [], "branches": [[58, 48], [66, 68]]}

import pytest
from configparser import ConfigParser
from flutils.setuputils.cfg import _each_setup_cfg_command, SetupCfgCommandConfig

@pytest.fixture
def config_parser():
    parser = ConfigParser()
    parser.add_section('setup.command.test')
    parser.set('setup.command.test', 'command', 'echo Hello')
    parser.set('setup.command.test', 'name', 'test_command')
    parser.set('setup.command.test', 'description', 'This is a test command')
    
    parser.add_section('setup.command.empty')
    parser.set('setup.command.empty', 'command', '')
    
    parser.add_section('setup.command.no_description')
    parser.set('setup.command.no_description', 'command', 'echo NoDescription')
    parser.set('setup.command.no_description', 'name', 'no_description_command')
    
    return parser

def test_each_setup_cfg_command(config_parser):
    format_kwargs = {'name': 'test'}
    commands = list(_each_setup_cfg_command(config_parser, format_kwargs))
    
    assert len(commands) == 2
    
    command = commands[0]
    assert command.name == 'test_command'
    assert command.description == 'This is a test command'
    assert command.commands == ('echo Hello',)
    assert command.camel == 'TestCommand'
    
    command = commands[1]
    assert command.name == 'no_description_command'
    assert command.description == ''
    assert command.commands == ('echo NoDescription',)
    assert command.camel == 'NoDescriptionCommand'
