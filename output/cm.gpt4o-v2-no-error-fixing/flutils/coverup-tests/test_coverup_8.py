# file: flutils/setuputils/cfg.py:32-41
# asked: {"lines": [32, 35, 36, 37, 38, 39, 40, 41], "branches": [[35, 0], [35, 36], [38, 35], [38, 39], [40, 35], [40, 41]]}
# gained: {"lines": [32, 35, 36, 37, 38, 39, 40, 41], "branches": [[35, 0], [35, 36], [38, 35], [38, 39], [40, 41]]}

import pytest
from configparser import ConfigParser
from flutils.setuputils.cfg import _each_setup_cfg_command_section

def test_each_setup_cfg_command_section():
    parser = ConfigParser()
    parser.add_section('setup.command.install')
    parser.add_section('setup.command.build')
    parser.add_section('other.section')

    parser.set('setup.command.install', 'option', 'value')
    parser.set('setup.command.build', 'option', 'value')
    parser.set('other.section', 'option', 'value')

    result = list(_each_setup_cfg_command_section(parser))

    assert result == [
        ('setup.command.install', 'install'),
        ('setup.command.build', 'build')
    ]
