# file typesystem/base.py:112-155
# lines [112, 115, 116, 117, 118, 119, 132, 134, 135, 138, 139, 140, 141, 142, 144, 145, 147, 150, 151, 152, 153, 154, 155]
# branches ['132->134', '132->138', '150->exit', '150->151', '152->153', '152->154']

import pytest
from typesystem.base import BaseError, Message

@pytest.fixture
def cleanup():
    # Fixture to perform cleanup if necessary
    yield
    # No cleanup actions needed for this test case

def test_base_error_with_single_message(cleanup):
    text = "Error message"
    code = "error_code"
    key = "error_key"
    error = BaseError(text=text, code=code, key=key)
    assert error._messages == [Message(text=text, code=code, key=key)]
    assert error._message_dict == {key: text}

def test_base_error_with_multiple_messages(cleanup):
    messages = [
        Message(text="First error", code="first_error", key="first_key"),
        Message(text="Second error", code="second_error", key="second_key")
    ]
    error = BaseError(messages=messages)
    assert error._messages == messages
    assert error._message_dict == {
        "first_key": "First error",
        "second_key": "Second error"
    }

def test_base_error_with_nested_messages(cleanup):
    messages = [
        Message(text="Nested error", code="nested_error", index=["parent", "child"])
    ]
    error = BaseError(messages=messages)
    assert error._messages == messages
    assert error._message_dict == {
        "parent": {
            "child": "Nested error"
        }
    }

def test_base_error_assertion_error(cleanup):
    with pytest.raises(AssertionError):
        BaseError()

    with pytest.raises(AssertionError):
        BaseError(text="Error message", messages=[Message(text="Error message")])

    with pytest.raises(AssertionError):
        BaseError(messages=[])

# Register the cleanup fixture to be used with the tests
test_base_error_with_single_message = pytest.mark.usefixtures("cleanup")(test_base_error_with_single_message)
test_base_error_with_multiple_messages = pytest.mark.usefixtures("cleanup")(test_base_error_with_multiple_messages)
test_base_error_with_nested_messages = pytest.mark.usefixtures("cleanup")(test_base_error_with_nested_messages)
test_base_error_assertion_error = pytest.mark.usefixtures("cleanup")(test_base_error_assertion_error)
