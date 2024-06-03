# file thefuck/argument_parser.py:13-15
# lines [13, 14, 15]
# branches []

import pytest
from thefuck.argument_parser import Parser
from argparse import ArgumentParser

def test_parser_initialization(mocker):
    mock_add_arguments = mocker.patch.object(Parser, '_add_arguments', autospec=True)
    
    parser_instance = Parser()
    
    assert isinstance(parser_instance._parser, ArgumentParser)
    assert parser_instance._parser.prog == 'thefuck'
    assert not parser_instance._parser.add_help
    mock_add_arguments.assert_called_once_with(parser_instance)
