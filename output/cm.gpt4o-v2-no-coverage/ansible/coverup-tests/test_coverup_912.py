# file: lib/ansible/plugins/lookup/config.py:84-85
# asked: {"lines": [84, 85], "branches": []}
# gained: {"lines": [84, 85], "branches": []}

import pytest
from ansible.errors import AnsibleOptionsError
from ansible.plugins.lookup.config import MissingSetting

def test_missing_setting_inheritance():
    assert issubclass(MissingSetting, AnsibleOptionsError)

def test_missing_setting_instance():
    error_message = "This is a test error message"
    error_instance = MissingSetting(error_message)
    assert isinstance(error_instance, MissingSetting)
    assert str(error_instance) == error_message
