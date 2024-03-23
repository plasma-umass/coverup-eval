# file thefuck/exceptions.py:9-10
# lines [9, 10]
# branches []

import pytest
from thefuck.exceptions import ScriptNotInLog

def test_script_not_in_log_exception():
    with pytest.raises(ScriptNotInLog) as exc_info:
        raise ScriptNotInLog("Test message")

    assert str(exc_info.value) == "Test message", "Exception message does not match expected message"
