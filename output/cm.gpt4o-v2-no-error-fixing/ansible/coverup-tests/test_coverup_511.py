# file: lib/ansible/module_utils/urls.py:483-485
# asked: {"lines": [483, 484, 485], "branches": []}
# gained: {"lines": [483, 484, 485], "branches": []}

import pytest
from ansible.module_utils.urls import ConnectionError

def test_connection_error():
    with pytest.raises(ConnectionError, match="Failed to connect to the server"):
        raise ConnectionError("Failed to connect to the server")
