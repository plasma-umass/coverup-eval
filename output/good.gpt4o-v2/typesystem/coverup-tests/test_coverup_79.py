# file: typesystem/base.py:190-192
# asked: {"lines": [190, 191, 192], "branches": []}
# gained: {"lines": [190, 191, 192], "branches": []}

import pytest
import typing
from typesystem.base import BaseError

class Message:
    def __init__(self, *, text: str, code: str=None, key: typing.Union[int, str]=None, index: typing.List[typing.Union[int, str]]=None, position: 'Position'=None, start_position: 'Position'=None, end_position: 'Position'=None):
        self.text = text
        self.code = 'custom' if code is None else code
        if key is not None:
            assert index is None
            self.index = [key]
        else:
            self.index = [] if index is None else index
        if position is None:
            self.start_position = start_position
            self.end_position = end_position
        else:
            assert start_position is None
            assert end_position is None
            self.start_position = position
            self.end_position = position

def test_base_error_hash():
    # Create a list of messages
    messages = [
        Message(text="Error 1", code="code1", key="key1"),
        Message(text="Error 2", code="code2", key="key2")
    ]
    
    # Instantiate BaseError with the list of messages
    error = BaseError(messages=messages)
    
    # Calculate the hash
    error_hash = hash(error)
    
    # Verify the hash is an integer
    assert isinstance(error_hash, int)
    
    # Verify the hash is consistent
    assert error_hash == hash(error)
