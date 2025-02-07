# file: flutils/setuputils/cfg.py:32-41
# asked: {"lines": [32, 35, 36, 37, 38, 39, 40, 41], "branches": [[35, 0], [35, 36], [38, 35], [38, 39], [40, 35], [40, 41]]}
# gained: {"lines": [32, 35, 36, 37, 38, 39, 40, 41], "branches": [[35, 0], [35, 36], [38, 35], [38, 39], [40, 35], [40, 41]]}

import pytest
from configparser import ConfigParser
from flutils.setuputils.cfg import _each_setup_cfg_command_section

def test_each_setup_cfg_command_section():
    parser = ConfigParser()
    parser.add_section('setup.command.test')
    parser.set('setup.command.test', 'option', 'value')

    result = list(_each_setup_cfg_command_section(parser))
    assert result == [('setup.command.test', 'test')]

    parser.add_section('setup.command.another.test')
    parser.set('setup.command.another.test', 'option', 'value')

    result = list(_each_setup_cfg_command_section(parser))
    assert result == [('setup.command.test', 'test'), ('setup.command.another.test', 'another.test')]

    parser.add_section('not_a_command')
    parser.set('not_a_command', 'option', 'value')

    result = list(_each_setup_cfg_command_section(parser))
    assert result == [('setup.command.test', 'test'), ('setup.command.another.test', 'another.test')]

    parser.add_section('setup.command.')
    parser.set('setup.command.', 'option', 'value')

    result = list(_each_setup_cfg_command_section(parser))
    assert result == [('setup.command.test', 'test'), ('setup.command.another.test', 'another.test')]

