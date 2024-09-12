# file: tornado/options.py:466-468
# asked: {"lines": [466, 467, 468], "branches": [[467, 0], [467, 468]]}
# gained: {"lines": [466, 467, 468], "branches": [[467, 0], [467, 468]]}

import pytest
from unittest.mock import Mock
from tornado.options import OptionParser

@pytest.fixture
def option_parser():
    return OptionParser()

def test_run_parse_callbacks(option_parser):
    # Create mock callbacks
    mock_callback1 = Mock()
    mock_callback2 = Mock()

    # Add mock callbacks to the parser
    option_parser.add_parse_callback(mock_callback1)
    option_parser.add_parse_callback(mock_callback2)

    # Run the parse callbacks
    option_parser.run_parse_callbacks()

    # Assert that both callbacks were called
    mock_callback1.assert_called_once()
    mock_callback2.assert_called_once()

    # Clean up by resetting the callbacks using the internal dictionary
    option_parser.__dict__['_parse_callbacks'] = []
