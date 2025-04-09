# file: typesystem/base.py:72-79
# asked: {"lines": [72, 73, 74, 75, 76, 77, 78], "branches": []}
# gained: {"lines": [72, 73, 74, 75, 76, 77, 78], "branches": []}

import pytest
from typesystem.base import Message

def test_message_equality():
    msg1 = Message(text="Error", code="400", key="username", start_position=1, end_position=5)
    msg2 = Message(text="Error", code="400", key="username", start_position=1, end_position=5)
    msg3 = Message(text="Error", code="400", key="username", start_position=1, end_position=6)
    msg4 = Message(text="Error", code="400", key="username", start_position=2, end_position=5)
    msg5 = Message(text="Error", code="401", key="username", start_position=1, end_position=5)
    msg6 = Message(text="Error", code="400", key="email", start_position=1, end_position=5)
    msg7 = Message(text="Different Error", code="400", key="username", start_position=1, end_position=5)

    assert msg1 == msg2  # Same attributes
    assert msg1 != msg3  # Different end_position
    assert msg1 != msg4  # Different start_position
    assert msg1 != msg5  # Different code
    assert msg1 != msg6  # Different key
    assert msg1 != msg7  # Different text
