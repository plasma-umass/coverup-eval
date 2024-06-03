# file pypara/commons/errors.py:10-28
# lines [10, 11, 18, 19, 27, 28]
# branches ['27->exit', '27->28']

import pytest
from pypara.commons.errors import ProgrammingError

def test_programming_error_passert():
    # Test that no exception is raised when the condition is True
    ProgrammingError.passert(True, "This should not raise an error")
    
    # Test that ProgrammingError is raised with the provided message when the condition is False
    with pytest.raises(ProgrammingError, match="Custom error message"):
        ProgrammingError.passert(False, "Custom error message")
    
    # Test that ProgrammingError is raised with the default message when the condition is False and no message is provided
    with pytest.raises(ProgrammingError, match="Broken coherence. Check your code against domain logic to fix it."):
        ProgrammingError.passert(False, None)
