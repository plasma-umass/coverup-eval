# file: flutils/setuputils/cfg.py:44-79
# asked: {"lines": [], "branches": [[58, 48], [60, 62], [66, 68], [73, 48]]}
# gained: {"lines": [], "branches": [[60, 62]]}

import pytest
from configparser import ConfigParser
from flutils.setuputils.cfg import _each_setup_cfg_command, SetupCfgCommandConfig

@pytest.fixture
def config_parser():
    parser = ConfigParser()
    parser.add_section('section1')
    parser.set('section1', 'command', 'echo Hello')
    parser.set('section1', 'commands', 'echo World')
    parser.set('section1', 'name', 'test_command')
    parser.set('section1', 'description', 'This is a test command')
    
    parser.add_section('section2')
    parser.set('section2', 'command', 'echo Another')
    parser.set('section2', 'name', 'another_command')
    parser.set('section2', 'description', 'This is another test command')
    
    parser.add_section('section3')
    parser.set('section3', 'commands', 'echo Third')
    parser.set('section3', 'description', 'This is a third test command')
    
    return parser

def test_each_setup_cfg_command(config_parser, mocker):
    format_kwargs = {'name': 'test'}
    
    # Mocking _each_setup_cfg_command_section to return the expected sections
    mocker.patch('flutils.setuputils.cfg._each_setup_cfg_command_section', return_value=[
        ('section1', 'default_command_name1'),
        ('section2', 'default_command_name2'),
        ('section3', 'default_command_name3')
    ])
    
    commands = list(_each_setup_cfg_command(config_parser, format_kwargs))
    
    assert len(commands) == 3
    
    command1 = commands[0]
    assert command1.name == 'test_command'
    assert command1.camel == 'TestCommand'
    assert command1.description == 'This is a test command'
    assert command1.commands == ('echo Hello', 'echo World')
    
    command2 = commands[1]
    assert command2.name == 'another_command'
    assert command2.camel == 'AnotherCommand'
    assert command2.description == 'This is another test command'
    assert command2.commands == ('echo Another',)
    
    command3 = commands[2]
    assert command3.name == 'default_command_name3'
    assert command3.camel == 'DefaultCommandName3'
    assert command3.description == 'This is a third test command'
    assert command3.commands == ('echo Third',)
