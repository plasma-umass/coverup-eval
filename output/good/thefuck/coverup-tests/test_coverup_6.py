# file thefuck/argument_parser.py:66-82
# lines [66, 76, 77, 78, 79, 80, 82]
# branches ['76->77', '76->79', '79->80', '79->82']

import pytest
from thefuck.argument_parser import Parser

ARGUMENT_PLACEHOLDER = 'THEFUCK_ARGUMENT_PLACEHOLDER'  # Placeholder used in the original code

@pytest.fixture
def parser():
    return Parser()

def test_prepare_arguments_with_placeholder(parser):
    argv = ['arg1', 'arg2', ARGUMENT_PLACEHOLDER, 'arg3', 'arg4']
    expected = ['arg3', 'arg4', '--', 'arg1', 'arg2']
    assert parser._prepare_arguments(argv) == expected

def test_prepare_arguments_without_placeholder_starting_with_dash(parser):
    argv = ['--option', 'value']
    expected = ['--option', 'value']
    assert parser._prepare_arguments(argv) == expected

def test_prepare_arguments_without_placeholder_not_starting_with_dash(parser):
    argv = ['command', 'arg1']
    expected = ['--', 'command', 'arg1']
    assert parser._prepare_arguments(argv) == expected

def test_prepare_arguments_with_double_dash(parser):
    argv = ['--', 'command', 'arg1']
    expected = ['--', 'command', 'arg1']
    assert parser._prepare_arguments(argv) == expected
