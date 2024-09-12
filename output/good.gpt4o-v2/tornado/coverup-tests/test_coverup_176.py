# file: tornado/options.py:726-731
# asked: {"lines": [726, 731], "branches": []}
# gained: {"lines": [726], "branches": []}

import pytest
from unittest.mock import Mock
from tornado.options import options, OptionParser

@pytest.fixture
def reset_options():
    original_callbacks = options._parse_callbacks.copy()
    yield
    options._parse_callbacks.clear()
    options._parse_callbacks.extend(original_callbacks)

def test_add_parse_callback(reset_options):
    mock_callback = Mock()

    # Ensure the callback list is initially empty
    assert mock_callback not in options._parse_callbacks

    # Call the function to test
    options.add_parse_callback(mock_callback)

    # Verify the callback was added
    assert mock_callback in options._parse_callbacks

    # Clean up
    options._parse_callbacks.remove(mock_callback)
