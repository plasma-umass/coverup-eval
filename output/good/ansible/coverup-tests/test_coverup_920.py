# file lib/ansible/plugins/lookup/config.py:84-85
# lines [84, 85]
# branches []

import pytest
from ansible.errors import AnsibleOptionsError
from ansible.plugins.lookup import config

# Assuming the MissingSetting class is inside the config.py file
# and is used when a required configuration is missing.

def test_missing_setting_exception():
    with pytest.raises(config.MissingSetting) as exc_info:
        raise config.MissingSetting("Test missing setting exception")

    assert str(exc_info.value) == "Test missing setting exception", "Exception message does not match expected message"
