# file lib/ansible/plugins/action/reboot.py:22-23
# lines [22, 23]
# branches []

import pytest
from ansible.plugins.action.reboot import TimedOutException

def test_timed_out_exception():
    with pytest.raises(TimedOutException):
        raise TimedOutException("Timeout occurred")

    # Ensure the exception message is correct
    try:
        raise TimedOutException("Timeout occurred")
    except TimedOutException as e:
        assert str(e) == "Timeout occurred"
