# file typesystem/base.py:194-199
# lines [195, 196, 197, 198, 199]
# branches ['196->197', '196->199']

import pytest
from typesystem.base import BaseError, Message

def test_base_error_repr_single_message_without_index():
    # Arrange
    message = Message(text="An error occurred", code="error_code")
    error = BaseError(messages=[message])

    # Act
    result = repr(error)

    # Assert
    assert result == "BaseError(text='An error occurred', code='error_code')"

def test_base_error_repr_multiple_messages_or_with_index():
    # Arrange
    message1 = Message(text="First error", code="first_code", index=[1])
    message2 = Message(text="Second error", code="second_code")
    error = BaseError(messages=[message1, message2])

    # Act
    result = repr(error)

    # Assert
    assert result == f"BaseError([{message1!r}, {message2!r}])"
