# file: pypara/commons/errors.py:10-28
# asked: {"lines": [10, 11, 18, 19, 27, 28], "branches": [[27, 0], [27, 28]]}
# gained: {"lines": [10, 11, 18, 19, 27, 28], "branches": [[27, 0], [27, 28]]}

import pytest
from pypara.commons.errors import ProgrammingError

def test_passert_true_condition():
    # Test when condition is True, no exception should be raised
    ProgrammingError.passert(True, "This should not raise an error")

def test_passert_false_condition_with_message():
    # Test when condition is False and a message is provided, the exception should be raised with the provided message
    with pytest.raises(ProgrammingError) as excinfo:
        ProgrammingError.passert(False, "Custom error message")
    assert str(excinfo.value) == "Custom error message"

def test_passert_false_condition_without_message():
    # Test when condition is False and no message is provided, the exception should be raised with the default message
    with pytest.raises(ProgrammingError) as excinfo:
        ProgrammingError.passert(False, None)
    assert str(excinfo.value) == "Broken coherence. Check your code against domain logic to fix it."
