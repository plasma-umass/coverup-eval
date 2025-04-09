# file thefuck/argument_parser.py:91-92
# lines [91, 92]
# branches []

import pytest
import sys
from unittest import mock

# Assuming the Parser class is imported from thefuck.argument_parser
from thefuck.argument_parser import Parser

def test_parser_print_help(mocker):
    # Mock sys.stderr to capture the print output
    mock_stderr = mocker.patch('sys.stderr', new_callable=mock.Mock)
    
    # Create a mock parser with a print_help method
    mock_parser = mock.Mock()
    mock_parser.print_help = mock.Mock()
    
    # Create an instance of the Parser class and set its _parser attribute
    parser_instance = Parser()
    parser_instance._parser = mock_parser
    
    # Call the print_help method
    parser_instance.print_help()
    
    # Assert that the print_help method of the _parser was called with sys.stderr
    mock_parser.print_help.assert_called_once_with(mock_stderr)

    # Clean up by resetting the mock
    mock_stderr.reset_mock()
