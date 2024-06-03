# file thefuck/argument_parser.py:17-52
# lines [17, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
# branches []

import pytest
from unittest.mock import MagicMock, patch
from argparse import ArgumentParser, ArgumentError

# Assuming the Parser class is defined in thefuck.argument_parser module
from thefuck.argument_parser import Parser

@pytest.fixture
def parser():
    parser_instance = Parser()
    parser_instance._parser = ArgumentParser(add_help=False)  # Disable default help to avoid conflict
    return parser_instance

def test_add_arguments(parser, mocker):
    mock_get_alias = mocker.patch('thefuck.argument_parser.get_alias', return_value='mock_alias')
    mock_add_conflicting_arguments = mocker.patch.object(parser, '_add_conflicting_arguments')

    parser._add_arguments()

    args = parser._parser.parse_args(['--version'])
    assert args.version is True

    args = parser._parser.parse_args(['--alias'])
    assert args.alias == 'mock_alias'

    args = parser._parser.parse_args(['--alias', 'custom_alias'])
    assert args.alias == 'custom_alias'

    args = parser._parser.parse_args(['--shell-logger', 'logfile.txt'])
    assert args.shell_logger == 'logfile.txt'

    args = parser._parser.parse_args(['--enable-experimental-instant-mode'])
    assert args.enable_experimental_instant_mode is True

    args = parser._parser.parse_args(['--help'])
    assert args.help is True

    args = parser._parser.parse_args(['--debug'])
    assert args.debug is True

    args = parser._parser.parse_args(['--force-command', 'some_command'])
    assert args.force_command == 'some_command'

    args = parser._parser.parse_args(['command1', 'command2'])
    assert args.command == ['command1', 'command2']

    mock_get_alias.assert_called_once()
    mock_add_conflicting_arguments.assert_called_once()
