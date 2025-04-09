# file typesystem/base.py:157-176
# lines [157, 158, 167, 168, 169, 170, 171, 172, 174, 176]
# branches ['167->168', '167->176']

import pytest
from typesystem.base import BaseError, Message

class TestBaseError:
    @pytest.fixture
    def base_error_with_messages(self):
        messages = [
            Message(text="Error 1", code="code1", index=[0]),
            Message(text="Error 2", code="code2", index=[1]),
        ]
        base_error = BaseError(messages=messages)
        return base_error

    def test_messages_with_prefix(self, base_error_with_messages):
        messages_with_prefix = base_error_with_messages.messages(add_prefix='prefix')
        assert len(messages_with_prefix) == 2
        assert messages_with_prefix[0].text == "Error 1"
        assert messages_with_prefix[0].code == "code1"
        assert messages_with_prefix[0].index == ['prefix', 0]
        assert messages_with_prefix[1].text == "Error 2"
        assert messages_with_prefix[1].code == "code2"
        assert messages_with_prefix[1].index == ['prefix', 1]

    def test_messages_without_prefix(self, base_error_with_messages):
        messages_without_prefix = base_error_with_messages.messages()
        assert len(messages_without_prefix) == 2
        assert messages_without_prefix[0].text == "Error 1"
        assert messages_without_prefix[0].code == "code1"
        assert messages_without_prefix[0].index == [0]
        assert messages_without_prefix[1].text == "Error 2"
        assert messages_without_prefix[1].code == "code2"
        assert messages_without_prefix[1].index == [1]
