# file lib/ansible/playbook/attribute.py:118-119
# lines [118, 119]
# branches []

import pytest
from ansible.playbook.attribute import Attribute

class FieldAttribute(Attribute):
    pass

def test_field_attribute_initialization():
    # Create an instance of FieldAttribute
    field_attr = FieldAttribute()
    
    # Assert that the instance is indeed a FieldAttribute
    assert isinstance(field_attr, FieldAttribute)
    
    # Assert that the instance is also an Attribute
    assert isinstance(field_attr, Attribute)
    
    # Clean up if necessary (not much to clean up in this simple case)
