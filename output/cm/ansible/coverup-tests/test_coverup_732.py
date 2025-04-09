# file lib/ansible/playbook/base.py:225-227
# lines [225, 226, 227]
# branches []

import pytest
from ansible.playbook.base import FieldAttributeBase

# Test function to check the finalized property
def test_field_attribute_base_finalized_property():
    field_attribute_base = FieldAttributeBase()
    
    # Assert that the initial value is False
    assert not field_attribute_base.finalized
    
    # Change the internal state to simulate finalization
    field_attribute_base._finalized = True
    
    # Assert that the finalized property reflects the change
    assert field_attribute_base.finalized
