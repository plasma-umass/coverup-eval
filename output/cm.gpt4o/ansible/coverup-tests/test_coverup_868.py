# file lib/ansible/plugins/action/wait_for_connection.py:32-33
# lines [32, 33]
# branches []

import pytest
from ansible.plugins.action.wait_for_connection import TimedOutException

def test_timed_out_exception():
    with pytest.raises(TimedOutException):
        raise TimedOutException("Connection timed out")

    # Ensure the exception message is correct
    try:
        raise TimedOutException("Connection timed out")
    except TimedOutException as e:
        assert str(e) == "Connection timed out"
