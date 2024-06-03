# file typesystem/base.py:157-176
# lines [157, 158, 167, 168, 169, 170, 171, 172, 174, 176]
# branches ['167->168', '167->176']

import pytest
from unittest.mock import MagicMock
from typesystem.base import BaseError, Message

def test_base_error_messages_with_prefix():
    # Create a mock message
    mock_message = MagicMock(spec=Message)
    mock_message.text = "Error text"
    mock_message.code = "error_code"
    mock_message.index = ["index1"]

    # Create an instance of BaseError with a mock _messages attribute
    base_error = BaseError(messages=[mock_message])

    # Call the messages method with a prefix
    prefix = "prefix"
    result = base_error.messages(add_prefix=prefix)

    # Verify the result
    assert len(result) == 1
    assert result[0].text == "Error text"
    assert result[0].code == "error_code"
    assert result[0].index == [prefix, "index1"]

def test_base_error_messages_without_prefix():
    # Create a mock message
    mock_message = MagicMock(spec=Message)
    mock_message.text = "Error text"
    mock_message.code = "error_code"
    mock_message.index = ["index1"]

    # Create an instance of BaseError with a mock _messages attribute
    base_error = BaseError(messages=[mock_message])

    # Call the messages method without a prefix
    result = base_error.messages()

    # Verify the result
    assert len(result) == 1
    assert result[0].text == "Error text"
    assert result[0].code == "error_code"
    assert result[0].index == ["index1"]
