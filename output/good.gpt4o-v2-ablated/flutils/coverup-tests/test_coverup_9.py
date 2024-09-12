# file: flutils/setuputils/cfg.py:32-41
# asked: {"lines": [32, 35, 36, 37, 38, 39, 40, 41], "branches": [[35, 0], [35, 36], [38, 35], [38, 39], [40, 35], [40, 41]]}
# gained: {"lines": [32, 35, 36, 37, 38, 39, 40, 41], "branches": [[35, 0], [35, 36], [38, 35], [38, 39], [40, 35], [40, 41]]}

import pytest
from configparser import ConfigParser
from flutils.setuputils.cfg import _each_setup_cfg_command_section

def test_each_setup_cfg_command_section(monkeypatch):
    # Create a mock ConfigParser
    parser = ConfigParser()
    
    # Add sections to the parser
    parser.add_section('setup.command.test')
    parser.add_section('setup.command.another.test')
    parser.add_section('not_a_command')
    parser.add_section('setup.command.')
    
    # Expected results
    expected_results = [
        ('setup.command.test', 'test'),
        ('setup.command.another.test', 'another.test')
    ]
    
    # Collect results
    results = list(_each_setup_cfg_command_section(parser))
    
    # Assertions
    assert results == expected_results

    # Clean up
    monkeypatch.undo()
