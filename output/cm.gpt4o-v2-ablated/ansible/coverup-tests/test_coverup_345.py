# file: lib/ansible/plugins/action/wait_for_connection.py:32-33
# asked: {"lines": [32, 33], "branches": []}
# gained: {"lines": [32, 33], "branches": []}

import pytest
from ansible.plugins.action.wait_for_connection import TimedOutException

def test_timed_out_exception():
    with pytest.raises(TimedOutException):
        raise TimedOutException("Connection timed out")
