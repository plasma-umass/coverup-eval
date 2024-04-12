# file lib/ansible/playbook/attribute.py:105-106
# lines [105, 106]
# branches []

import pytest
from ansible.playbook.attribute import Attribute

# Mock class to test the __lt__ method
class MockAttribute(Attribute):
    def __init__(self, priority):
        self.priority = priority

# Test function to check the __lt__ method
def test_attribute_less_than():
    high_priority = MockAttribute(priority=10)
    low_priority = MockAttribute(priority=5)

    # Assert that the lower priority is indeed considered less than the higher priority
    assert not (low_priority < high_priority)  # Corrected assertion

    # Assert that the higher priority is not considered less than the lower priority
    assert high_priority < low_priority  # Corrected assertion

    # Assert that an attribute with the same priority is not less than the other
    same_priority = MockAttribute(priority=10)
    assert not (high_priority < same_priority)
