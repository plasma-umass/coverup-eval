# file tornado/options.py:710-715
# lines [710, 715]
# branches []

import pytest
from tornado.options import OptionParser, options

def test_parse_config_file(mocker):
    # Mock the parse_config_file method of OptionParser
    mock_parse_config_file = mocker.patch.object(OptionParser, 'parse_config_file')

    # Create a dummy config file path
    dummy_path = 'dummy_config.cfg'

    # Call the function to be tested
    options.parse_config_file(dummy_path, final=True)

    # Assert that the parse_config_file method was called with the correct arguments
    mock_parse_config_file.assert_called_once_with(dummy_path, final=True)
