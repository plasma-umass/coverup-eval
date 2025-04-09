# file lib/ansible/inventory/group.py:280-281
# lines [280, 281]
# branches []

import pytest
from ansible.inventory.group import Group

# Test function to cover get_vars method
def test_get_vars():
    # Setup
    group = Group()

    # Set some variables to the group
    group.vars = {
        'key1': 'value1',
        'key2': 'value2'
    }

    # Exercise
    vars_copy = group.get_vars()

    # Verify
    assert vars_copy == group.vars
    assert vars_copy is not group.vars  # Ensure it's a copy, not the same object

    # Cleanup - nothing to do since no external resources were modified
