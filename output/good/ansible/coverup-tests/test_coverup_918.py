# file lib/ansible/plugins/action/pause.py:62-63
# lines [62, 63]
# branches []

import pytest
from ansible.plugins.action.pause import AnsibleTimeoutExceeded

def test_ansible_timeout_exceeded_exception():
    with pytest.raises(AnsibleTimeoutExceeded) as exc_info:
        raise AnsibleTimeoutExceeded("Timeout exceeded")

    assert str(exc_info.value) == "Timeout exceeded", "Exception message should match the expected message"
