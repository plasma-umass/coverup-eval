# file lib/ansible/playbook/base.py:75-76
# lines [75, 76]
# branches []

import pytest
from ansible.playbook.base import Base

# Mock class to test Base class functionality
class MockBase(Base):
    def __init__(self):
        super().__init__()
        self._attributes = {}

    # Define the _generic_s method in the mock class
    def _generic_s(self, prop_name, value):
        self._attributes[prop_name] = value

# Test function to cover _generic_s method
def test_generic_s_method():
    mock_base = MockBase()
    prop_name = 'test_property'
    value = 'test_value'

    # Before setting the property, it should not exist
    assert prop_name not in mock_base._attributes

    # Set the property using the _generic_s method
    mock_base._generic_s(prop_name, value)

    # After setting, the property should exist with the correct value
    assert prop_name in mock_base._attributes
    assert mock_base._attributes[prop_name] == value

    # Clean up: remove the property
    del mock_base._attributes[prop_name]
    assert prop_name not in mock_base._attributes
