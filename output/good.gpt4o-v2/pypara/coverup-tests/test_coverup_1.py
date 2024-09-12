# file: pypara/commons/errors.py:10-28
# asked: {"lines": [10, 11, 18, 19, 27, 28], "branches": [[27, 0], [27, 28]]}
# gained: {"lines": [10, 11, 18, 19, 27, 28], "branches": [[27, 0], [27, 28]]}

import pytest
from pypara.commons.errors import ProgrammingError

def test_passert_true():
    # This should not raise an exception
    ProgrammingError.passert(True, "This should not fail")

def test_passert_false_with_message():
    # This should raise a ProgrammingError with the provided message
    with pytest.raises(ProgrammingError, match="This should fail"):
        ProgrammingError.passert(False, "This should fail")

def test_passert_false_without_message():
    # This should raise a ProgrammingError with the default message
    with pytest.raises(ProgrammingError, match="Broken coherence. Check your code against domain logic to fix it."):
        ProgrammingError.passert(False, None)
