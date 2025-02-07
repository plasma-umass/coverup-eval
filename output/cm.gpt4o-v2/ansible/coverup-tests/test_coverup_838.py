# file: lib/ansible/playbook/attribute.py:118-119
# asked: {"lines": [118, 119], "branches": []}
# gained: {"lines": [118, 119], "branches": []}

import pytest
from ansible.playbook.attribute import FieldAttribute, Attribute

def test_field_attribute_inheritance():
    # Verify that FieldAttribute is a subclass of Attribute
    assert issubclass(FieldAttribute, Attribute)

    # Verify that an instance of FieldAttribute is also an instance of Attribute
    field_attr_instance = FieldAttribute()
    assert isinstance(field_attr_instance, FieldAttribute)
    assert isinstance(field_attr_instance, Attribute)
