# file: flutils/setuputils/cfg.py:32-41
# asked: {"lines": [35, 36, 37, 38, 39, 40, 41], "branches": [[35, 0], [35, 36], [38, 35], [38, 39], [40, 35], [40, 41]]}
# gained: {"lines": [35, 36, 37, 38, 39, 40, 41], "branches": [[35, 0], [35, 36], [38, 35], [38, 39], [40, 41]]}

import pytest
from configparser import ConfigParser
from typing import Generator, Tuple, cast
from flutils.setuputils.cfg import _each_setup_cfg_command_section

def test_each_setup_cfg_command_section(monkeypatch):
    config_data = """
    [setup.command.install]
    option1 = value1

    [setup.command.build]
    option2 = value2

    [other.section]
    option3 = value3
    """

    parser = ConfigParser()
    parser.read_string(config_data)

    result = list(_each_setup_cfg_command_section(parser))

    assert result == [
        ('setup.command.install', 'install'),
        ('setup.command.build', 'build')
    ]

    # Clean up
    monkeypatch.undo()
