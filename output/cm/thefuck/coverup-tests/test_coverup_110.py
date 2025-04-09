# file thefuck/argument_parser.py:91-92
# lines [91, 92]
# branches []

import sys
from io import StringIO
import pytest
from unittest.mock import Mock
from thefuck.argument_parser import Parser

@pytest.fixture
def mock_stderr(mocker):
    return mocker.patch('sys.stderr', new_callable=StringIO)

def test_parser_print_help(mock_stderr, mocker):
    parser = Parser()
    mock_parser = mocker.Mock()
    parser._parser = mock_parser
    parser.print_help()
    mock_parser.print_help.assert_called_once_with(sys.stderr)
    # Removed the incorrect assertion as the mock does not write to stderr
