# file: lib/ansible/plugins/action/pause.py:62-63
# asked: {"lines": [62, 63], "branches": []}
# gained: {"lines": [62, 63], "branches": []}

import pytest
from ansible.plugins.action.pause import AnsibleTimeoutExceeded

def test_ansible_timeout_exceeded():
    with pytest.raises(AnsibleTimeoutExceeded):
        raise AnsibleTimeoutExceeded("Timeout exceeded")

    # Ensure the exception message is correct
    try:
        raise AnsibleTimeoutExceeded("Timeout exceeded")
    except AnsibleTimeoutExceeded as e:
        assert str(e) == "Timeout exceeded"
