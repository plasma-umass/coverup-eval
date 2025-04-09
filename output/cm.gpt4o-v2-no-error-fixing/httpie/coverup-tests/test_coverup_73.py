# file: httpie/cli/argparser.py:259-283
# asked: {"lines": [265, 267, 268, 269, 270, 273, 274, 275, 276, 277, 279, 281, 282, 283], "branches": [[267, 268], [267, 281], [268, 269], [268, 273], [274, 275], [274, 279], [275, 274], [275, 276], [281, 0], [281, 282]]}
# gained: {"lines": [265, 267, 268, 273, 274, 275, 276, 277, 279, 281, 282, 283], "branches": [[267, 268], [267, 281], [268, 273], [274, 275], [274, 279], [275, 274], [275, 276], [281, 0], [281, 282]]}

import pytest
from httpie.cli.argparser import HTTPieArgumentParser
import argparse

class MockArgs:
    def __init__(self):
        self.some_option = None

@pytest.fixture
def parser():
    parser = HTTPieArgumentParser()
    parser.args = MockArgs()
    parser._actions = [
        argparse.Action(option_strings=['--some-option'], dest='some_option', default='default_value')
    ]
    return parser

def test_apply_no_options_valid(parser):
    parser._apply_no_options(['--no-some-option'])
    assert parser.args.some_option == 'default_value'

def test_apply_no_options_invalid(parser, mocker):
    mock_error = mocker.patch.object(parser, 'error')
    parser._apply_no_options(['--no-invalid-option'])
    mock_error.assert_called_once_with('unrecognized arguments: --no-invalid-option')

def test_apply_no_options_mixed(parser, mocker):
    mock_error = mocker.patch.object(parser, 'error')
    parser._apply_no_options(['--no-some-option', '--no-invalid-option'])
    assert parser.args.some_option == 'default_value'
    mock_error.assert_called_once_with('unrecognized arguments: --no-invalid-option')
