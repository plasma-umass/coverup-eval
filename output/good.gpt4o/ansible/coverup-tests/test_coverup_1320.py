# file lib/ansible/playbook/base.py:225-227
# lines [227]
# branches []

import pytest
from unittest.mock import patch

# Assuming the class FieldAttributeBase is imported from ansible.playbook.base
from ansible.playbook.base import FieldAttributeBase

def test_field_attribute_base_finalized():
    # Create a mock object for FieldAttributeBase
    instance = FieldAttributeBase()
    
    # Patch the instance's _finalized attribute
    with patch.object(instance, '_finalized', True):
        # Assert that the finalized property returns the expected value
        assert instance.finalized == True
