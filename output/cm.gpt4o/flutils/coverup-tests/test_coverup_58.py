# file flutils/setuputils/cfg.py:32-41
# lines []
# branches ['40->35']

import pytest
from configparser import ConfigParser
from flutils.setuputils.cfg import _each_setup_cfg_command_section

def test_each_setup_cfg_command_section(mocker):
    # Create a mock ConfigParser
    parser = ConfigParser()
    
    # Add sections to the parser
    parser.add_section('setup.command.test')
    parser.add_section('setup.command.')
    parser.add_section('setup.command.another.test')
    parser.add_section('unrelated.section')
    
    # Mock the sections method to return our custom sections
    mocker.patch.object(parser, 'sections', return_value=parser.sections())
    
    # Collect the results
    results = list(_each_setup_cfg_command_section(parser))
    
    # Assertions to verify the correct sections and command names are yielded
    assert results == [
        ('setup.command.test', 'test'),
        ('setup.command.another.test', 'another.test')
    ]
