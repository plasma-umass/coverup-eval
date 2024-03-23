# file lib/ansible/module_utils/urls.py:483-485
# lines [483, 484, 485]
# branches []

import pytest
from ansible.module_utils.urls import ConnectionError

def test_connection_error():
    with pytest.raises(ConnectionError) as exc_info:
        raise ConnectionError("Test connection error")

    assert str(exc_info.value) == "Test connection error", "ConnectionError did not contain the correct message"
