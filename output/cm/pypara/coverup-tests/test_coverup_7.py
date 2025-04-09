# file pypara/commons/errors.py:10-28
# lines [10, 11, 18, 19, 27, 28]
# branches ['27->exit', '27->28']

import pytest
from pypara.commons.errors import ProgrammingError

def test_programming_error_passert():
    with pytest.raises(ProgrammingError) as exc_info:
        ProgrammingError.passert(False, "Custom error message")
    assert str(exc_info.value) == "Custom error message"

    with pytest.raises(ProgrammingError) as exc_info_no_message:
        ProgrammingError.passert(False, None)
    assert str(exc_info_no_message.value) == "Broken coherence. Check your code against domain logic to fix it."

def test_programming_error_passert_no_raise():
    # This test should not raise an exception, thus no cleanup is necessary.
    try:
        ProgrammingError.passert(True, "This should not raise an error")
    except ProgrammingError:
        pytest.fail("ProgrammingError.passert raised an exception unexpectedly!")
