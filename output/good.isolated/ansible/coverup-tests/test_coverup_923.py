# file lib/ansible/plugins/action/reboot.py:22-23
# lines [22, 23]
# branches []

import pytest
from ansible.plugins.action.reboot import TimedOutException

def test_timed_out_exception():
    with pytest.raises(TimedOutException) as exc_info:
        raise TimedOutException("Timeout occurred")
    assert str(exc_info.value) == "Timeout occurred"
