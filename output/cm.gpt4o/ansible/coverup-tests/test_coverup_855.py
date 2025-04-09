# file lib/ansible/plugins/lookup/config.py:84-85
# lines [84, 85]
# branches []

import pytest
from ansible.plugins.lookup.config import MissingSetting
from ansible.errors import AnsibleOptionsError

def test_missing_setting_exception():
    with pytest.raises(MissingSetting):
        raise MissingSetting("This is a missing setting error")

    # Verify that MissingSetting is a subclass of AnsibleOptionsError
    assert issubclass(MissingSetting, AnsibleOptionsError)
