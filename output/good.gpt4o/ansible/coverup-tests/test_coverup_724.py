# file lib/ansible/module_utils/urls.py:483-485
# lines [483, 484, 485]
# branches []

import pytest
from ansible.module_utils.urls import ConnectionError

def test_connection_error():
    with pytest.raises(ConnectionError) as excinfo:
        raise ConnectionError("Failed to connect to the server")
    assert str(excinfo.value) == "Failed to connect to the server"
