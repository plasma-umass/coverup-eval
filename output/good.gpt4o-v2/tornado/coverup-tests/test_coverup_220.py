# file: tornado/options.py:726-731
# asked: {"lines": [731], "branches": []}
# gained: {"lines": [731], "branches": []}

import pytest
from unittest.mock import Mock
from tornado.options import OptionParser, add_parse_callback

@pytest.fixture
def clean_options(monkeypatch):
    # Create a new OptionParser instance and patch it in the module
    new_options = OptionParser()
    monkeypatch.setattr('tornado.options.options', new_options)
    return new_options

def test_add_parse_callback(clean_options):
    mock_callback = Mock()

    # Ensure the callback list is empty before the test
    assert len(clean_options._parse_callbacks) == 0

    # Add the mock callback
    add_parse_callback(mock_callback)

    # Verify the callback was added
    assert mock_callback in clean_options._parse_callbacks

    # Clean up by removing the mock callback
    clean_options._parse_callbacks.remove(mock_callback)
    assert len(clean_options._parse_callbacks) == 0
