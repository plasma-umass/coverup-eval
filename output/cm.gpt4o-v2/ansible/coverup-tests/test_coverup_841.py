# file: lib/ansible/playbook/base.py:301-302
# asked: {"lines": [301, 302], "branches": []}
# gained: {"lines": [301, 302], "branches": []}

import pytest
from ansible.playbook.base import FieldAttributeBase

def test_get_variable_manager():
    instance = FieldAttributeBase()
    instance._variable_manager = "test_manager"
    assert instance.get_variable_manager() == "test_manager"
