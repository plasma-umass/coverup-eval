# file: lib/ansible/plugins/action/reboot.py:22-23
# asked: {"lines": [22, 23], "branches": []}
# gained: {"lines": [22, 23], "branches": []}

import pytest
from ansible.plugins.action.reboot import TimedOutException

def test_timed_out_exception():
    with pytest.raises(TimedOutException):
        raise TimedOutException("Timeout occurred")

