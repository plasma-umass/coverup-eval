# file typesystem/base.py:187-188
# lines [187, 188]
# branches []

import pytest
from typesystem.base import BaseError

def test_base_error_eq():
    class ValidationError(BaseError):
        def __init__(self, messages):
            self._messages = messages

        def __iter__(self):
            return iter(self._messages)

        def __len__(self):
            return len(self._messages)

        def __getitem__(self, index):
            return self._messages[index]

        def __eq__(self, other):
            return isinstance(other, ValidationError) and self._messages == other._messages

    error1 = ValidationError(["error1"])
    error2 = ValidationError(["error1"])
    error3 = ValidationError(["error2"])
    non_error = "not an error"

    # Test equality with same messages
    assert error1 == error2

    # Test inequality with different messages
    assert error1 != error3

    # Test inequality with non-ValidationError instance
    assert error1 != non_error
