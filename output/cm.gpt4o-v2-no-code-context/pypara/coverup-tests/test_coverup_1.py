# file: pypara/commons/errors.py:10-28
# asked: {"lines": [10, 11, 18, 19, 27, 28], "branches": [[27, 0], [27, 28]]}
# gained: {"lines": [10, 11, 18, 19, 27, 28], "branches": [[27, 0], [27, 28]]}

import pytest
from pypara.commons.errors import ProgrammingError

def test_programming_error_passert_true():
    # This should not raise an exception
    ProgrammingError.passert(True, "This should not raise")

def test_programming_error_passert_false():
    # This should raise a ProgrammingError
    with pytest.raises(ProgrammingError) as excinfo:
        ProgrammingError.passert(False, "This should raise")
    assert str(excinfo.value) == "This should raise"

def test_programming_error_passert_false_default_message():
    # This should raise a ProgrammingError with the default message
    with pytest.raises(ProgrammingError) as excinfo:
        ProgrammingError.passert(False, None)
    assert str(excinfo.value) == "Broken coherence. Check your code against domain logic to fix it."
