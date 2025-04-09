# file: pymonet/either.py:22-35
# asked: {"lines": [22, 33, 34, 35], "branches": [[33, 34], [33, 35]]}
# gained: {"lines": [22, 33, 34, 35], "branches": [[33, 34], [33, 35]]}

import pytest
from pymonet.either import Either

class TestEither:
    def test_case_success(self):
        class Right(Either):
            def __init__(self, value):
                self._value = value

            def is_right(self):
                return True

            @property
            def value(self):
                return self._value

        right_instance = Right(42)
        result = right_instance.case(
            error=lambda x: f"Error: {x}",
            success=lambda x: f"Success: {x}"
        )
        assert result == "Success: 42"

    def test_case_error(self):
        class Left(Either):
            def __init__(self, value):
                self._value = value

            def is_right(self):
                return False

            @property
            def value(self):
                return self._value

        left_instance = Left("error")
        result = left_instance.case(
            error=lambda x: f"Error: {x}",
            success=lambda x: f"Success: {x}"
        )
        assert result == "Error: error"
