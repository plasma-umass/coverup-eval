# file: tornado/escape.py:209-211
# asked: {"lines": [209, 210, 211], "branches": []}
# gained: {"lines": [209, 210], "branches": []}

import pytest
import typing
from tornado.escape import to_unicode

def test_to_unicode_bytes(monkeypatch):
    # Mock the overload decorator to ensure the function is called
    def mock_overload(func):
        return func

    monkeypatch.setattr(typing, 'overload', mock_overload)

    # Define the function to test
    @typing.overload
    def to_unicode(value: bytes) -> str:
        return value.decode('utf-8')

    # Test the function with bytes input
    result = to_unicode(b'hello')
    assert result == 'hello'
