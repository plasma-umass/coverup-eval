# file lib/ansible/plugins/action/wait_for_connection.py:32-33
# lines [32, 33]
# branches []

import pytest
from ansible.plugins.action.wait_for_connection import TimedOutException

def test_timed_out_exception():
    with pytest.raises(TimedOutException) as exc_info:
        raise TimedOutException("Connection timed out")

    assert str(exc_info.value) == "Connection timed out", "TimedOutException did not contain the correct message"
