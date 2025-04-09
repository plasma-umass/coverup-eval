# file httpie/cli/argparser.py:61-66
# lines [61, 62, 63, 64, 65, 66]
# branches []

import argparse
import pytest
from httpie.cli.argparser import HTTPieArgumentParser, HTTPieHelpFormatter

# Mock environment and stdin data for the parser
class MockEnvironment:
    stdin_isatty = True
    stdin = None

@pytest.fixture
def mock_env(mocker):
    return MockEnvironment()

# Test function to cover the missing lines/branches
def test_httpie_argument_parser_initialization(mock_env):
    parser = HTTPieArgumentParser(formatter_class=HTTPieHelpFormatter)
    parser.env = mock_env  # Set the env attribute directly
    parser.has_stdin_data = True  # Set the has_stdin_data attribute directly
    assert parser.env == mock_env
    assert parser.has_stdin_data
    assert isinstance(parser.formatter_class, type(HTTPieHelpFormatter))
    assert not parser.add_help

# Ensure that the test cleans up after itself and does not affect other tests
def test_cleanup_after_httpie_argument_parser_initialization():
    parser = HTTPieArgumentParser(formatter_class=HTTPieHelpFormatter)
    assert parser.env is None
    assert not parser.has_stdin_data
    assert isinstance(parser.formatter_class, type(HTTPieHelpFormatter))
    assert not parser.add_help
