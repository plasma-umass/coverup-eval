# file thefuck/exceptions.py:1-2
# lines [1, 2]
# branches []

import pytest
from thefuck.exceptions import EmptyCommand

def test_empty_command_exception():
    with pytest.raises(EmptyCommand) as exc_info:
        raise EmptyCommand("No command provided")

    assert str(exc_info.value) == "No command provided", "Exception message does not match"
