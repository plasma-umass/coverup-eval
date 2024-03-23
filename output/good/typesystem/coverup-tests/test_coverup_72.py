# file typesystem/base.py:29-70
# lines [29, 33, 34, 35, 36, 37, 38, 55, 56, 57, 58, 59, 61, 63, 64, 65, 67, 68, 69, 70]
# branches ['57->58', '57->61', '63->64', '63->67']

import pytest
from typesystem.base import Message

@pytest.fixture
def cleanup():
    # Fixture to perform cleanup if necessary
    yield
    # No cleanup actions needed for this test

def test_message_initialization(cleanup):
    # Test initialization with position
    position = (1, 1)
    message_with_position = Message(text="Error with position", position=position)
    assert message_with_position.text == "Error with position"
    assert message_with_position.code == "custom"
    assert message_with_position.index == []
    assert message_with_position.start_position == position
    assert message_with_position.end_position == position

    # Test initialization with start_position and end_position
    start_position = (1, 1)
    end_position = (1, 5)
    message_with_start_end = Message(
        text="Error with start and end",
        start_position=start_position,
        end_position=end_position
    )
    assert message_with_start_end.text == "Error with start and end"
    assert message_with_start_end.code == "custom"
    assert message_with_start_end.index == []
    assert message_with_start_end.start_position == start_position
    assert message_with_start_end.end_position == end_position

    # Test initialization with key
    message_with_key = Message(text="Error with key", key='error_key')
    assert message_with_key.text == "Error with key"
    assert message_with_key.code == "custom"
    assert message_with_key.index == ['error_key']

    # Test initialization with index
    message_with_index = Message(text="Error with index", index=['users', 3, 'username'])
    assert message_with_index.text == "Error with index"
    assert message_with_index.code == "custom"
    assert message_with_index.index == ['users', 3, 'username']

    # Test initialization with code
    message_with_code = Message(text="Error with code", code='error_code')
    assert message_with_code.text == "Error with code"
    assert message_with_code.code == "error_code"
    assert message_with_code.index == []

    # Test initialization with both key and index should raise AssertionError
    with pytest.raises(AssertionError):
        Message(text="Error", key='error_key', index=['users', 3, 'username'])

    # Test initialization with both position and start_position should raise AssertionError
    with pytest.raises(AssertionError):
        Message(
            text="Error",
            position=position,
            start_position=start_position
        )

    # Test initialization with both position and end_position should raise AssertionError
    with pytest.raises(AssertionError):
        Message(
            text="Error",
            position=position,
            end_position=end_position
        )
