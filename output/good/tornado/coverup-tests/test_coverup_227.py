# file tornado/options.py:457-460
# lines [458, 459, 460]
# branches ['458->exit', '458->459']

import pytest
from tornado.options import OptionParser
from unittest.mock import patch
import sys

@pytest.fixture
def parser():
    return OptionParser()

def test_help_callback_exits_when_value_true(parser):
    with patch('tornado.options.OptionParser.print_help') as mock_print_help:
        with patch('sys.exit') as mock_exit:
            parser._help_callback(True)
            mock_print_help.assert_called_once()
            mock_exit.assert_called_once_with(0)

def test_help_callback_does_not_exit_when_value_false(parser):
    with patch('tornado.options.OptionParser.print_help') as mock_print_help:
        with patch('sys.exit') as mock_exit:
            parser._help_callback(False)
            mock_print_help.assert_not_called()
            mock_exit.assert_not_called()
