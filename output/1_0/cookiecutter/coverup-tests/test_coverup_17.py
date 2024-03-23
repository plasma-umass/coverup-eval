# file cookiecutter/exceptions.py:93-99
# lines [93, 94]
# branches []

import pytest
from cookiecutter.exceptions import InvalidModeException

def test_invalid_mode_exception():
    with pytest.raises(InvalidModeException) as exc_info:
        raise InvalidModeException("Incompatible modes: cannot have no_input=True and replay=True.")
    
    assert str(exc_info.value) == "Incompatible modes: cannot have no_input=True and replay=True."
