# file flutils/setuputils/cfg.py:32-41
# lines [32, 35, 36, 37, 38, 39, 40, 41]
# branches ['35->exit', '35->36', '38->35', '38->39', '40->35', '40->41']

import pytest
from configparser import ConfigParser
from flutils.setuputils.cfg import _each_setup_cfg_command_section

def test_each_setup_cfg_command_section():
    parser = ConfigParser()
    parser.add_section('setup.command.test_command')
    parser.add_section('setup.command.another_command')
    parser.add_section('unrelated.section')

    result = list(_each_setup_cfg_command_section(parser))

    assert result == [
        ('setup.command.test_command', 'test_command'),
        ('setup.command.another_command', 'another_command')
    ]
