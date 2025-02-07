# file: tornado/options.py:457-460
# asked: {"lines": [457, 458, 459, 460], "branches": [[458, 0], [458, 459]]}
# gained: {"lines": [457, 458, 459, 460], "branches": [[458, 0], [458, 459]]}

import pytest
import sys
from unittest import mock

from tornado.options import OptionParser

@pytest.fixture
def option_parser():
    return OptionParser()

def test_help_callback_triggers_print_help_and_exit(option_parser):
    with mock.patch.object(OptionParser, 'print_help') as mock_print_help, \
         mock.patch.object(sys, 'exit') as mock_exit:
        option_parser._help_callback(True)
        mock_print_help.assert_called_once()
        mock_exit.assert_called_once_with(0)

def test_help_callback_does_nothing_when_false(option_parser):
    with mock.patch.object(OptionParser, 'print_help') as mock_print_help, \
         mock.patch.object(sys, 'exit') as mock_exit:
        option_parser._help_callback(False)
        mock_print_help.assert_not_called()
        mock_exit.assert_not_called()
