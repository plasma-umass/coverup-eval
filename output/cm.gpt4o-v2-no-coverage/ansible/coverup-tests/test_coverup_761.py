# file: lib/ansible/playbook/base.py:225-227
# asked: {"lines": [225, 226, 227], "branches": []}
# gained: {"lines": [225, 226, 227], "branches": []}

import pytest
from ansible.playbook.base import FieldAttributeBase

@pytest.fixture
def field_attribute_base():
    return FieldAttributeBase()

def test_finalized_property(field_attribute_base):
    # Ensure the initial state of _finalized is False
    assert field_attribute_base._finalized is False
    # Access the finalized property and check its value
    assert field_attribute_base.finalized is False
    # Modify the _finalized attribute
    field_attribute_base._finalized = True
    # Access the finalized property again and check its new value
    assert field_attribute_base.finalized is True
