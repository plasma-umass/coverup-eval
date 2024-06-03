# file tornado/options.py:457-460
# lines [457, 458, 459, 460]
# branches ['458->exit', '458->459']

import pytest
import sys
from unittest import mock

from tornado.options import OptionParser

def test_help_callback(mocker):
    parser = OptionParser()
    
    # Mock the print_help method and sys.exit
    mock_print_help = mocker.patch.object(OptionParser, 'print_help', autospec=True)
    mock_exit = mocker.patch('sys.exit')
    
    # Call the _help_callback method with True
    parser._help_callback(True)
    
    # Assert that print_help was called
    mock_print_help.assert_called_once_with(parser)
    
    # Assert that sys.exit was called with 0
    mock_exit.assert_called_once_with(0)
    
    # Call the _help_callback method with False
    parser._help_callback(False)
    
    # Assert that print_help was not called again
    mock_print_help.assert_called_once()  # still only one call
    
    # Assert that sys.exit was not called again
    mock_exit.assert_called_once_with(0)  # still only one call
