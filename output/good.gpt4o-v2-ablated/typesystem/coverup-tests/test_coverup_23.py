# file: typesystem/base.py:81-83
# asked: {"lines": [82, 83], "branches": []}
# gained: {"lines": [82, 83], "branches": []}

import pytest

from typesystem.base import Message

@pytest.fixture
def message_instance():
    class TestMessage(Message):
        def __init__(self, code, index):
            self.code = code
            self.index = index

    return TestMessage

def test_message_hash(message_instance):
    msg1 = message_instance(code=1, index=[1, 2, 3])
    msg2 = message_instance(code=1, index=[1, 2, 3])
    msg3 = message_instance(code=2, index=[1, 2, 3])
    msg4 = message_instance(code=1, index=[3, 2, 1])

    # Test that identical messages have the same hash
    assert hash(msg1) == hash(msg2)

    # Test that different messages have different hashes
    assert hash(msg1) != hash(msg3)
    assert hash(msg1) != hash(msg4)

    # Test that the hash is consistent
    assert hash(msg1) == hash(msg1)
