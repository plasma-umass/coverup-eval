# file: httpie/cli/argparser.py:440-444
# asked: {"lines": [440, 441, 442, 443, 444], "branches": [[442, 443], [442, 444]]}
# gained: {"lines": [440, 441, 442, 443, 444], "branches": [[442, 443], [442, 444]]}

import pytest
from httpie.cli.argparser import HTTPieArgumentParser
from httpie.cli.argtypes import parse_format_options

class MockArgs:
    def __init__(self, format_options=None):
        self.format_options = format_options

@pytest.fixture
def parser():
    parser = HTTPieArgumentParser()
    return parser

def test_process_format_options_default(parser, mocker):
    mocker.patch.object(parser, 'args', MockArgs(format_options=None))
    mocker.patch('httpie.cli.argparser.PARSED_DEFAULT_FORMAT_OPTIONS', {'default_key': 'default_value'})
    parser._process_format_options()
    assert parser.args.format_options == {'default_key': 'default_value'}

def test_process_format_options_with_options(parser, mocker):
    mock_format_options = 'key=value'
    mock_parsed_options = {'key': 'value'}
    mocker.patch.object(parser, 'args', MockArgs(format_options=[mock_format_options]))
    parse_format_options_mock = mocker.patch('httpie.cli.argparser.parse_format_options', return_value=mock_parsed_options)
    mocker.patch('httpie.cli.argparser.PARSED_DEFAULT_FORMAT_OPTIONS', {'default_key': 'default_value'})
    
    parser._process_format_options()
    
    parse_format_options_mock.assert_called_once_with(mock_format_options, defaults={'default_key': 'default_value'})
    assert parser.args.format_options == mock_parsed_options
