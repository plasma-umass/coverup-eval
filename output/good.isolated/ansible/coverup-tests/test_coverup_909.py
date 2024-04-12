# file lib/ansible/playbook/base.py:301-302
# lines [301, 302]
# branches []

import pytest
from ansible.playbook.base import FieldAttributeBase
from unittest.mock import MagicMock

# Create a mock class to replace the original FieldAttributeBase for testing
class MockFieldAttributeBase(FieldAttributeBase):
    def __init__(self):
        self._variable_manager = MagicMock()

def test_get_variable_manager():
    # Create an instance of the MockFieldAttributeBase class
    instance = MockFieldAttributeBase()
    
    # Call the get_variable_manager method
    variable_manager = instance.get_variable_manager()
    
    # Assert that the returned variable_manager is the mock
    assert isinstance(variable_manager, MagicMock)

    # Clean up by deleting the instance
    del instance
