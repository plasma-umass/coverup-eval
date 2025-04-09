# file: tornado/options.py:726-731
# asked: {"lines": [731], "branches": []}
# gained: {"lines": [731], "branches": []}

import pytest
from unittest.mock import Mock

# Assuming the OptionParser class and add_parse_callback function are defined in the module tornado.options
from tornado.options import add_parse_callback, OptionParser

@pytest.fixture
def option_parser():
    parser = OptionParser()
    yield parser
    # Clean up if necessary

def test_add_parse_callback(option_parser, monkeypatch):
    mock_callback = Mock()

    # Patch the options object to use our fixture
    monkeypatch.setattr('tornado.options.options', option_parser)

    # Ensure no callbacks are present initially
    assert len(option_parser._parse_callbacks) == 0

    # Add the callback
    add_parse_callback(mock_callback)

    # Verify the callback was added
    assert len(option_parser._parse_callbacks) == 1
    assert option_parser._parse_callbacks[0] == mock_callback

    # Clean up
    option_parser._parse_callbacks.clear()
