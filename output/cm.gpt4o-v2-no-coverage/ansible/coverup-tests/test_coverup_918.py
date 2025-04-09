# file: lib/ansible/plugins/action/pause.py:66-67
# asked: {"lines": [66, 67], "branches": []}
# gained: {"lines": [66, 67], "branches": []}

import pytest
from ansible.plugins.action.pause import timeout_handler, AnsibleTimeoutExceeded

def test_timeout_handler():
    with pytest.raises(AnsibleTimeoutExceeded):
        timeout_handler(signum=1, frame=None)
