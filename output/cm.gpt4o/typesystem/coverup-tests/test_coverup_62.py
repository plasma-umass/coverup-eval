# file typesystem/base.py:24-28
# lines [24, 25]
# branches []

import pytest
from typesystem.base import Message

def test_message_class():
    # Create an instance of the Message class with the required argument
    message_instance = Message(text="Sample error message")
    
    # Assert that the instance is indeed of type Message
    assert isinstance(message_instance, Message)
    
    # Assert that the text attribute is correctly set
    assert message_instance.text == "Sample error message"
    
    # Assert that the docstring is correctly set
    assert message_instance.__doc__.strip() == "An individual error message, within a ValidationError."
