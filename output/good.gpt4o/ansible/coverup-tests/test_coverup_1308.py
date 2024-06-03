# file lib/ansible/inventory/group.py:167-168
# lines [168]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the Group class is imported from ansible.inventory.group
from ansible.inventory.group import Group

def test_get_name():
    # Create a mock object for Group
    group = Group()
    
    # Mock the 'name' attribute
    group.name = "test_group"
    
    # Call the method and assert the result
    assert group.get_name() == "test_group"
