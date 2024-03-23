# file lib/ansible/playbook/attribute.py:97-98
# lines [97, 98]
# branches []

import pytest

from ansible.playbook.attribute import Attribute

# Mock class to test comparison with Attribute
class MockAttribute:
    def __init__(self, priority):
        self.priority = priority

# Test function to check __eq__ method
def test_attribute_eq():
    attribute_a = Attribute()
    attribute_a.priority = 10

    attribute_b = MockAttribute(10)
    attribute_c = MockAttribute(5)

    # Test equality
    assert attribute_a == attribute_b, "Attribute equality comparison failed when it should pass"

    # Test inequality
    assert not (attribute_a == attribute_c), "Attribute equality comparison passed when it should fail"

    # Clean up
    del attribute_a
    del attribute_b
    del attribute_c
