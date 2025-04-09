# file: typesystem/base.py:184-185
# asked: {"lines": [184, 185], "branches": []}
# gained: {"lines": [184, 185], "branches": []}

import pytest
from typesystem.base import BaseError
from typesystem.base import Message, Position

def test_base_error_getitem():
    # Create a sample message
    position = Position(line_no=1, column_no=1, char_index=0)
    message = Message(text="Error message", code="error_code", key="error_key", position=position)
    
    # Initialize BaseError with the message
    error = BaseError(messages=[message])
    
    # Test __getitem__ method
    assert error["error_key"] == "Error message"
    
    # Test for a key that does not exist
    with pytest.raises(KeyError):
        _ = error["non_existent_key"]
