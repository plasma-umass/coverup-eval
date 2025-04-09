# file tornado/options.py:462-464
# lines [462, 464]
# branches []

import pytest
from unittest.mock import Mock
from tornado.options import OptionParser

@pytest.fixture
def option_parser():
    return OptionParser()

def test_add_parse_callback(option_parser):
    # Setup: Create a mock callback function
    mock_callback = Mock()

    # Exercise: Add the mock callback to the OptionParser
    option_parser.add_parse_callback(mock_callback)

    # Verify: Check that the callback is in the _parse_callbacks list
    assert mock_callback in option_parser._parse_callbacks

    # Cleanup: Remove the mock callback from the _parse_callbacks list
    option_parser._parse_callbacks.remove(mock_callback)
    assert mock_callback not in option_parser._parse_callbacks
