# file thefuck/argument_parser.py:17-52
# lines [17, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
# branches []

import pytest
from argparse import ArgumentParser, SUPPRESS
from thefuck.argument_parser import Parser
from unittest.mock import MagicMock

@pytest.fixture
def parser(mocker):
    mocker.patch('thefuck.argument_parser.get_alias', return_value='thefuck_alias')
    parser_instance = Parser()
    parser_instance._parser = ArgumentParser(add_help=False)  # Disable default help to avoid conflict
    return parser_instance

def test_parser_add_arguments(parser):
    parser._add_arguments()
    args = parser._parser.parse_args(['--version'])
    assert args.version is True

    args = parser._parser.parse_args(['--alias'])
    assert args.alias == 'thefuck_alias'

    args = parser._parser.parse_args(['--alias', 'custom_alias'])
    assert args.alias == 'custom_alias'

    args = parser._parser.parse_args(['--shell-logger', 'logfile.log'])
    assert args.shell_logger == 'logfile.log'

    args = parser._parser.parse_args(['--enable-experimental-instant-mode'])
    assert args.enable_experimental_instant_mode is True

    args = parser._parser.parse_args(['--help'])
    assert args.help is True

    args = parser._parser.parse_args(['--debug'])
    assert args.debug is True

    args = parser._parser.parse_args(['--force-command', 'forced_command'])
    assert args.force_command == 'forced_command'

    args = parser._parser.parse_args(['command_to_fix'])
    assert args.command == ['command_to_fix']
