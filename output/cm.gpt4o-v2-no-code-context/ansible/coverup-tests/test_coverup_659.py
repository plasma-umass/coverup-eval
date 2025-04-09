# file: lib/ansible/module_utils/urls.py:483-485
# asked: {"lines": [483, 484, 485], "branches": []}
# gained: {"lines": [483, 484, 485], "branches": []}

import pytest
from ansible.module_utils.urls import ConnectionError

def test_connection_error_inheritance():
    with pytest.raises(ConnectionError):
        raise ConnectionError("Failed to connect to the server")

def test_connection_error_message():
    try:
        raise ConnectionError("Failed to connect to the server")
    except ConnectionError as e:
        assert str(e) == "Failed to connect to the server"
