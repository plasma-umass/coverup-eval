# file: tornado/options.py:134-143
# asked: {"lines": [134, 136, 137, 138, 139, 140, 141, 142], "branches": []}
# gained: {"lines": [134, 136, 137, 138, 139, 140, 141, 142], "branches": []}

import pytest
from tornado.options import OptionParser

def test_option_parser_init(monkeypatch):
    # Arrange
    parser = OptionParser()

    # Act
    options = parser.__dict__["_options"]
    parse_callbacks = parser.__dict__["_parse_callbacks"]

    # Assert
    assert "help" in options
    assert options["help"].type == bool
    assert options["help"].help == "show this help information"
    assert options["help"].callback == parser._help_callback
    assert parse_callbacks == []

    # Cleanup
    monkeypatch.undo()
