# file: typesystem/base.py:72-79
# asked: {"lines": [72, 73, 74, 75, 76, 77, 78], "branches": []}
# gained: {"lines": [72, 73, 74, 75, 76, 77, 78], "branches": []}

import pytest
from typesystem.base import Message

def test_message_equality():
    msg1 = Message(text="Error", code="400", key="username", position=None, start_position=1, end_position=2)
    msg2 = Message(text="Error", code="400", key="username", position=None, start_position=1, end_position=2)
    msg3 = Message(text="Error", code="400", key="username", position=None, start_position=1, end_position=3)
    msg4 = Message(text="Error", code="400", key="username", position=None, start_position=1, end_position=2)
    msg4.text = "Different Error"

    assert msg1 == msg2  # Should be True
    assert msg1 != msg3  # Should be True
    assert msg1 != msg4  # Should be True

    msg5 = Message(text="Error", code="400", index=["users", 3, "username"], position=None, start_position=1, end_position=2)
    msg6 = Message(text="Error", code="400", index=["users", 3, "username"], position=None, start_position=1, end_position=2)

    assert msg5 == msg6  # Should be True

    msg7 = Message(text="Error", code="400", index=["users", 3, "username"], position=None, start_position=1, end_position=3)

    assert msg5 != msg7  # Should be True

    msg8 = Message(text="Error", code="400", key="username", position=1)
    msg9 = Message(text="Error", code="400", key="username", position=1)

    assert msg8 == msg9  # Should be True

    msg10 = Message(text="Error", code="400", key="username", position=1)
    msg11 = Message(text="Error", code="400", key="username", position=2)

    assert msg10 != msg11  # Should be True
