# file: httpie/cli/argparser.py:298-335
# asked: {"lines": [303, 305, 306, 307, 309, 312, 315, 317, 318, 320, 321, 322, 323, 327, 329, 330, 331, 332, 333, 335], "branches": [[303, 305], [303, 312], [306, 307], [306, 309], [312, 0], [312, 315], [321, 322], [321, 323]]}
# gained: {"lines": [303, 305, 306, 307, 309, 312, 315, 317, 318, 320, 321, 323, 327, 329, 330, 331, 332, 333, 335], "branches": [[303, 305], [303, 312], [306, 307], [306, 309], [312, 315], [321, 323]]}

import pytest
from unittest.mock import MagicMock, patch
from httpie.cli.argparser import HTTPieArgumentParser, HTTPieHelpFormatter
from httpie.cli.constants import HTTP_GET, HTTP_POST, SEPARATOR_GROUP_ALL_ITEMS, SEPARATOR_GROUP_DATA_ITEMS
from httpie.cli.argtypes import KeyValueArgType
import re
import argparse

@pytest.fixture
def parser():
    parser = HTTPieArgumentParser(formatter_class=HTTPieHelpFormatter)
    parser.args = MagicMock()
    parser.has_stdin_data = False
    return parser

def test_guess_method_no_method_no_data(parser):
    parser.args.method = None
    parser.args.request_items = []
    parser.has_stdin_data = False

    parser._guess_method()

    assert parser.args.method == HTTP_GET

def test_guess_method_no_method_with_data(parser):
    parser.args.method = None
    parser.args.request_items = []
    parser.has_stdin_data = True

    parser._guess_method()

    assert parser.args.method == HTTP_POST

def test_guess_method_invalid_method(parser):
    parser.args.method = 'http://example.com'
    parser.args.url = 'http://example.com'
    parser.args.request_items = []
    parser.args.traceback = False

    with patch.object(KeyValueArgType, '__call__', return_value=MagicMock(sep='=')) as mock_call:
        parser._guess_method()

    assert parser.args.url == 'http://example.com'
    assert parser.args.method == HTTP_POST
    assert parser.args.request_items[0].sep == '='
    mock_call.assert_called_once_with('http://example.com')

def test_guess_method_invalid_method_with_data(parser):
    parser.args.method = 'http://example.com'
    parser.args.url = 'http://example.com'
    parser.args.request_items = [MagicMock(sep='=')]
    parser.args.traceback = False
    parser.has_stdin_data = False

    with patch.object(KeyValueArgType, '__call__', return_value=MagicMock(sep='=')) as mock_call:
        parser._guess_method()

    assert parser.args.url == 'http://example.com'
    assert parser.args.method == HTTP_POST
    assert parser.args.request_items[0].sep == '='
    mock_call.assert_called_once_with('http://example.com')

def test_guess_method_invalid_method_with_stdin_data(parser):
    parser.args.method = 'http://example.com'
    parser.args.url = 'http://example.com'
    parser.args.request_items = []
    parser.args.traceback = False
    parser.has_stdin_data = True

    with patch.object(KeyValueArgType, '__call__', return_value=MagicMock(sep='=')) as mock_call:
        parser._guess_method()

    assert parser.args.url == 'http://example.com'
    assert parser.args.method == HTTP_POST
    assert parser.args.request_items[0].sep == '='
    mock_call.assert_called_once_with('http://example.com')

def test_guess_method_argparse_error(parser):
    parser.args.method = 'http://example.com'
    parser.args.url = 'http://example.com'
    parser.args.request_items = []
    parser.args.traceback = False

    with patch.object(KeyValueArgType, '__call__', side_effect=argparse.ArgumentTypeError('error')), \
         patch.object(parser, 'error') as mock_error:
        parser._guess_method()

    mock_error.assert_called_once_with('error')
