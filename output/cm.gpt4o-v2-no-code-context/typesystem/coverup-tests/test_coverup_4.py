# file: typesystem/base.py:157-176
# asked: {"lines": [157, 158, 167, 168, 169, 170, 171, 172, 174, 176], "branches": [[167, 168], [167, 176]]}
# gained: {"lines": [157, 158, 167, 168, 169, 170, 171, 172, 174, 176], "branches": [[167, 168], [167, 176]]}

import pytest
from typesystem.base import BaseError, Message

class TestBaseError:
    @pytest.fixture
    def base_error(self):
        class TestError(BaseError):
            def __init__(self, messages):
                self._messages = messages

        messages = [
            Message(text="Error 1", code="error_1", index=[]),
            Message(text="Error 2", code="error_2", index=[1])
        ]
        return TestError(messages)

    def test_messages_without_prefix(self, base_error):
        messages = base_error.messages()
        assert len(messages) == 2
        assert messages[0].text == "Error 1"
        assert messages[0].code == "error_1"
        assert messages[0].index == []
        assert messages[1].text == "Error 2"
        assert messages[1].code == "error_2"
        assert messages[1].index == [1]

    def test_messages_with_prefix(self, base_error):
        messages = base_error.messages(add_prefix="prefix")
        assert len(messages) == 2
        assert messages[0].text == "Error 1"
        assert messages[0].code == "error_1"
        assert messages[0].index == ["prefix"]
        assert messages[1].text == "Error 2"
        assert messages[1].code == "error_2"
        assert messages[1].index == ["prefix", 1]
