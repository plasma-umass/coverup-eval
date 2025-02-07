# file: pymonet/either.py:22-35
# asked: {"lines": [22, 33, 34, 35], "branches": [[33, 34], [33, 35]]}
# gained: {"lines": [22, 33, 34, 35], "branches": [[33, 34], [33, 35]]}

import pytest
from pymonet.either import Either

def test_either_case_success():
    class Right(Either):
        def is_right(self):
            return True

    right_instance = Right(10)
    result = right_instance.case(
        error=lambda x: f"Error: {x}",
        success=lambda x: f"Success: {x}"
    )
    assert result == "Success: 10"

def test_either_case_error():
    class Left(Either):
        def is_right(self):
            return False

    left_instance = Left(10)
    result = left_instance.case(
        error=lambda x: f"Error: {x}",
        success=lambda x: f"Success: {x}"
    )
    assert result == "Error: 10"
