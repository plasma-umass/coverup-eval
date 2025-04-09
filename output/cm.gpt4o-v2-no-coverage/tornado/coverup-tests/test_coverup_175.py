# file: tornado/options.py:710-715
# asked: {"lines": [710, 715], "branches": []}
# gained: {"lines": [710, 715], "branches": []}

import pytest
from unittest import mock
from tornado.options import parse_config_file, options

def test_parse_config_file(monkeypatch):
    # Mock the OptionParser.parse_config_file method
    mock_parse_config_file = mock.Mock()
    monkeypatch.setattr(options.__class__, 'parse_config_file', mock_parse_config_file)

    # Define test path and final flag
    test_path = "test_config.cfg"
    test_final = True

    # Call the function under test
    parse_config_file(test_path, final=test_final)

    # Assert the mock was called with the correct arguments
    mock_parse_config_file.assert_called_once_with(test_path, final=test_final)
