# file lib/ansible/playbook/attribute.py:108-109
# lines [108, 109]
# branches []

import pytest
from ansible.playbook.attribute import Attribute

# Mock class to test comparison
class MockAttribute(Attribute):
    def __init__(self, priority):
        self.priority = priority

@pytest.fixture
def create_attributes():
    # Create two attributes with different priorities
    high_priority = MockAttribute(priority=10)
    low_priority = MockAttribute(priority=5)
    return high_priority, low_priority

def test_attribute_greater_than(create_attributes):
    high_priority, low_priority = create_attributes

    # Test that high_priority is not considered greater than low_priority
    assert not (high_priority > low_priority)

    # Test that low_priority is considered greater than high_priority
    assert low_priority > high_priority
