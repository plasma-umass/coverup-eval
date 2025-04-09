# file: httpie/cli/argparser.py:61-66
# asked: {"lines": [61, 62, 63, 64, 65, 66], "branches": []}
# gained: {"lines": [61, 62, 63, 64, 65, 66], "branches": []}

import pytest
from httpie.cli.argparser import HTTPieArgumentParser, HTTPieHelpFormatter

def test_httpie_argument_parser_init():
    parser = HTTPieArgumentParser()
    assert parser.env is None
    assert parser.args is None
    assert parser.has_stdin_data is False
    assert isinstance(parser.formatter_class, type(HTTPieHelpFormatter))
    assert not parser.add_help
