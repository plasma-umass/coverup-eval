# file: tornado/options.py:718-723
# asked: {"lines": [718, 723], "branches": []}
# gained: {"lines": [718, 723], "branches": []}

import pytest
from unittest import mock
from tornado.options import print_help, options, OptionParser

def test_print_help(monkeypatch):
    mock_file = mock.Mock()

    # Mock the OptionParser.print_help method
    with mock.patch.object(OptionParser, 'print_help', autospec=True) as mock_print_help:
        print_help(mock_file)
        mock_print_help.assert_called_once_with(options, mock_file)

    # Test with default argument
    with mock.patch.object(OptionParser, 'print_help', autospec=True) as mock_print_help:
        print_help()
        mock_print_help.assert_called_once_with(options, None)
