# file: httpie/cli/argparser.py:61-66
# asked: {"lines": [61, 62, 63, 64, 65, 66], "branches": []}
# gained: {"lines": [61, 62, 63, 64, 65, 66], "branches": []}

import pytest
import argparse
from httpie.cli.argparser import HTTPieArgumentParser

def test_httpie_argument_parser_initialization():
    parser = HTTPieArgumentParser()
    assert not parser.add_help
    assert parser.env is None
    assert parser.args is None
    assert not parser.has_stdin_data
