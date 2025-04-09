# file httpie/cli/argparser.py:61-66
# lines [61, 62, 63, 64, 65, 66]
# branches []

import pytest
import argparse
from httpie.cli.argparser import HTTPieArgumentParser, HTTPieHelpFormatter

def test_httpie_argument_parser_initialization():
    parser = HTTPieArgumentParser()
    
    # Assertions to verify the postconditions
    assert parser.env is None
    assert parser.args is None
    assert parser.has_stdin_data is False
    assert not parser.add_help
    assert isinstance(parser._get_formatter(), HTTPieHelpFormatter)
