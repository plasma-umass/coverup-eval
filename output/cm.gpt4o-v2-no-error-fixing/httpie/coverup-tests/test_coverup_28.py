# file: httpie/cli/argparser.py:440-444
# asked: {"lines": [440, 441, 442, 443, 444], "branches": [[442, 443], [442, 444]]}
# gained: {"lines": [440, 441, 442, 443, 444], "branches": [[442, 443], [442, 444]]}

import pytest
from httpie.cli.argparser import HTTPieArgumentParser
from httpie.cli.argtypes import PARSED_DEFAULT_FORMAT_OPTIONS, parse_format_options

class MockArgs:
    def __init__(self, format_options=None):
        self.format_options = format_options

@pytest.fixture
def parser():
    parser = HTTPieArgumentParser()
    return parser

def test_process_format_options_default(parser, mocker):
    mocker.patch.object(parser, 'args', MockArgs(format_options=None))
    parser._process_format_options()
    assert parser.args.format_options == PARSED_DEFAULT_FORMAT_OPTIONS

def test_process_format_options_custom(parser, mocker):
    custom_options = 'json.indent:2,json.sort_keys:false'
    expected_options = parse_format_options(custom_options, defaults=PARSED_DEFAULT_FORMAT_OPTIONS)
    mocker.patch.object(parser, 'args', MockArgs(format_options=[custom_options]))
    parser._process_format_options()
    assert parser.args.format_options == expected_options
