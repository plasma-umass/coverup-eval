# file: cookiecutter/exceptions.py:102-107
# asked: {"lines": [102, 103], "branches": []}
# gained: {"lines": [102, 103], "branches": []}

import pytest
from cookiecutter.exceptions import FailedHookException, CookiecutterException

def test_failed_hook_exception():
    with pytest.raises(FailedHookException) as exc_info:
        raise FailedHookException("Hook failed")
    assert str(exc_info.value) == "Hook failed"
    assert isinstance(exc_info.value, CookiecutterException)
