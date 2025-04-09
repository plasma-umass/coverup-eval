# file: pypara/commons/errors.py:10-28
# asked: {"lines": [10, 11, 18, 19, 27, 28], "branches": [[27, 0], [27, 28]]}
# gained: {"lines": [10, 11, 18, 19, 27, 28], "branches": [[27, 0], [27, 28]]}

import pytest
from pypara.commons.errors import ProgrammingError

def test_programming_error_passert_true():
    # Test that no exception is raised when condition is True
    ProgrammingError.passert(True, "This should not raise an error")

def test_programming_error_passert_false_with_message():
    # Test that ProgrammingError is raised with the provided message when condition is False
    with pytest.raises(ProgrammingError) as excinfo:
        ProgrammingError.passert(False, "Custom error message")
    assert str(excinfo.value) == "Custom error message"

def test_programming_error_passert_false_without_message():
    # Test that ProgrammingError is raised with the default message when condition is False and no message is provided
    with pytest.raises(ProgrammingError) as excinfo:
        ProgrammingError.passert(False, None)
    assert str(excinfo.value) == "Broken coherence. Check your code against domain logic to fix it."
