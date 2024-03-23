# file typesystem/base.py:24-28
# lines [24, 25]
# branches []

import pytest
from typesystem.base import Message

def test_message_initialization():
    # Test the initialization of the Message class
    message = Message(text="Error occurred", code="error_code")
    assert message.text == "Error occurred"
    assert message.code == "error_code"
    assert message.index == []

def test_message_repr():
    # Test the __repr__ method of the Message class
    message = Message(text="Error occurred", code="error_code")
    assert repr(message) == "Message(text='Error occurred', code='error_code')"

def test_message_eq():
    # Test the __eq__ method of the Message class
    message1 = Message(text="Error occurred", code="error_code")
    message2 = Message(text="Error occurred", code="error_code")
    message3 = Message(text="Different error", code="different_code")
    assert message1 == message2
    assert message1 != message3

def test_message_ne():
    # Test the __ne__ method of the Message class
    message1 = Message(text="Error occurred", code="error_code")
    message2 = Message(text="Error occurred", code="error_code")
    message3 = Message(text="Different error", code="different_code")
    assert not (message1 != message2)
    assert message1 != message3
