# file: lib/ansible/plugins/lookup/config.py:84-85
# asked: {"lines": [84, 85], "branches": []}
# gained: {"lines": [84, 85], "branches": []}

import pytest
from ansible.errors import AnsibleOptionsError
from ansible.plugins.lookup.config import MissingSetting

def test_missing_setting_inheritance():
    assert issubclass(MissingSetting, AnsibleOptionsError)

def test_missing_setting_instance():
    instance = MissingSetting("Test message")
    assert isinstance(instance, MissingSetting)
    assert str(instance) == "Test message"
