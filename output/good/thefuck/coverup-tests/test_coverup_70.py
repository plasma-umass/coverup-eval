# file thefuck/argument_parser.py:84-86
# lines [84, 85, 86]
# branches []

import pytest
from thefuck.argument_parser import Parser
from unittest.mock import Mock

# Assuming the Parser class is part of a module named 'thefuck.argument_parser'
# and has a '_prepare_arguments' method and a '_parser' attribute with 'parse_args' method.

@pytest.fixture
def parser():
    p = Parser()
    p._prepare_arguments = Mock(return_value=['--some-arg'])
    p._parser = Mock()
    p._parser.parse_args = Mock(return_value='parsed_args')
    return p

def test_parser_parse_method(parser):
    argv = ['thefuck', '--some-arg']
    result = parser.parse(argv)
    parser._prepare_arguments.assert_called_once_with(['--some-arg'])
    parser._parser.parse_args.assert_called_once_with(['--some-arg'])
    assert result == 'parsed_args'
