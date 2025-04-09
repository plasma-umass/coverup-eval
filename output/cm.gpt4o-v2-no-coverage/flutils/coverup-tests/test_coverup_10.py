# file: flutils/setuputils/cfg.py:44-79
# asked: {"lines": [44, 48, 49, 50, 51, 52, 53, 54, 55, 56, 58, 59, 60, 61, 62, 63, 65, 66, 67, 68, 70, 71, 73, 74, 75, 76, 77, 78], "branches": [[48, 0], [48, 49], [51, 52], [51, 58], [52, 51], [52, 53], [58, 48], [58, 59], [60, 61], [60, 62], [66, 67], [66, 68], [73, 48], [73, 74]]}
# gained: {"lines": [44, 48, 49, 50, 51, 52, 53, 54, 55, 56, 58, 59, 60, 61, 62, 63, 65, 66, 67, 68, 70, 71, 73, 74, 75, 76, 77, 78], "branches": [[48, 0], [48, 49], [51, 52], [51, 58], [52, 51], [52, 53], [58, 59], [60, 61], [66, 67], [73, 74]]}

import pytest
from configparser import ConfigParser
from flutils.setuputils.cfg import _each_setup_cfg_command, SetupCfgCommandConfig
from unittest.mock import MagicMock

@pytest.fixture
def mock_parser():
    parser = ConfigParser()
    parser.add_section('setup.command.test')
    parser.set('setup.command.test', 'command', 'echo "Hello, World!"')
    parser.set('setup.command.test', 'name', 'test_command')
    parser.set('setup.command.test', 'description', 'This is a test command.')
    return parser

def test_each_setup_cfg_command(mock_parser):
    format_kwargs = {'name': 'test'}
    commands = list(_each_setup_cfg_command(mock_parser, format_kwargs))
    
    assert len(commands) == 1
    command = commands[0]
    assert command.name == 'test_command'
    assert command.camel == 'TestCommand'
    assert command.description == 'This is a test command.'
    assert command.commands == ('echo "Hello, World!"',)

@pytest.fixture(autouse=True)
def cleanup(monkeypatch):
    yield
    monkeypatch.undo()
