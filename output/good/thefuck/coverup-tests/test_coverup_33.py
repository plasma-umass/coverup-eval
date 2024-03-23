# file thefuck/argument_parser.py:54-64
# lines [54, 56, 57, 58, 59, 60, 61, 62, 63, 64]
# branches []

import pytest
from thefuck.argument_parser import Parser
from argparse import ArgumentParser

@pytest.fixture
def parser(mocker):
    mocker.patch('argparse.ArgumentParser.add_mutually_exclusive_group', return_value=mocker.Mock())
    return Parser()

def test_conflicting_arguments(parser):
    parser._add_conflicting_arguments()
    group = parser._parser.add_mutually_exclusive_group.return_value
    assert parser._parser.add_mutually_exclusive_group.called
    # Check if '-y' and '-r' are in the added arguments
    call_args_list = group.add_argument.call_args_list
    assert any('-y' in call_args[0] for call_args in call_args_list)
    assert any('-r' in call_args[0] for call_args in call_args_list)
