# file: typesystem/base.py:157-176
# asked: {"lines": [157, 158, 167, 168, 169, 170, 171, 172, 174, 176], "branches": [[167, 168], [167, 176]]}
# gained: {"lines": [157, 158, 167, 168, 169, 170, 171, 172, 174, 176], "branches": [[167, 168], [167, 176]]}

import pytest
from typesystem.base import BaseError, Message

def test_messages_no_prefix():
    messages = [Message(text="Error 1", code="code1", index=[]), Message(text="Error 2", code="code2", index=[])]
    error = BaseError(messages=messages)
    result = error.messages()
    assert result == messages

def test_messages_with_prefix():
    messages = [Message(text="Error 1", code="code1", index=[]), Message(text="Error 2", code="code2", index=[])]
    error = BaseError(messages=messages)
    result = error.messages(add_prefix="prefix")
    expected = [Message(text="Error 1", code="code1", index=["prefix"]), Message(text="Error 2", code="code2", index=["prefix"])]
    assert result == expected
