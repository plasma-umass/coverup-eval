# file: lib/ansible/playbook/base.py:301-302
# asked: {"lines": [301, 302], "branches": []}
# gained: {"lines": [301, 302], "branches": []}

import pytest
from unittest.mock import MagicMock

from ansible.playbook.base import FieldAttributeBase

@pytest.fixture
def field_attribute_base():
    instance = FieldAttributeBase()
    instance._variable_manager = MagicMock()
    return instance

def test_get_variable_manager(field_attribute_base):
    variable_manager = field_attribute_base.get_variable_manager()
    assert variable_manager is field_attribute_base._variable_manager
