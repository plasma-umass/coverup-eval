# file thefuck/argument_parser.py:88-89
# lines [88, 89]
# branches []

import sys
from io import StringIO
from unittest.mock import Mock
import pytest
from thefuck.argument_parser import Parser

@pytest.fixture
def mock_stderr(mocker):
    return mocker.patch('sys.stderr', new_callable=StringIO)

def test_parser_print_usage(mock_stderr):
    parser = Parser()
    parser._parser = Mock()
    parser.print_usage()
    parser._parser.print_usage.assert_called_once_with(sys.stderr)
    assert mock_stderr.getvalue() == '', "sys.stderr should not have actual content"
