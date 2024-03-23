# file cookiecutter/exceptions.py:102-107
# lines [102, 103]
# branches []

import pytest
from cookiecutter.exceptions import FailedHookException

def test_failed_hook_exception():
    with pytest.raises(FailedHookException) as exc_info:
        raise FailedHookException("Hook script failed.")

    assert str(exc_info.value) == "Hook script failed."
