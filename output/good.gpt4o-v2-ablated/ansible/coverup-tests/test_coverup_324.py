# file: lib/ansible/playbook/attribute.py:118-119
# asked: {"lines": [118, 119], "branches": []}
# gained: {"lines": [118, 119], "branches": []}

import pytest
from ansible.playbook.attribute import Attribute, FieldAttribute

def test_field_attribute_inheritance():
    # Ensure FieldAttribute is a subclass of Attribute
    assert issubclass(FieldAttribute, Attribute)

    # Ensure an instance of FieldAttribute is also an instance of Attribute
    field_attr_instance = FieldAttribute()
    assert isinstance(field_attr_instance, FieldAttribute)
    assert isinstance(field_attr_instance, Attribute)
