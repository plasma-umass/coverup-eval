# file: lib/ansible/plugins/action/pause.py:66-67
# asked: {"lines": [67], "branches": []}
# gained: {"lines": [67], "branches": []}

import pytest
from ansible.plugins.action.pause import AnsibleTimeoutExceeded

def test_timeout_handler(monkeypatch):
    from ansible.plugins.action.pause import timeout_handler

    def mock_raise(signum, frame):
        raise AnsibleTimeoutExceeded

    monkeypatch.setattr('ansible.plugins.action.pause.timeout_handler', mock_raise)

    with pytest.raises(AnsibleTimeoutExceeded):
        timeout_handler(None, None)
