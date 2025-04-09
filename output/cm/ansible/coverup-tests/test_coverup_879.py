# file lib/ansible/playbook/attribute.py:111-112
# lines [111, 112]
# branches []

import pytest
from ansible.playbook.attribute import Attribute

# Mock class to test the Attribute class comparison
class MockAttribute(Attribute):
    def __init__(self, priority):
        self.priority = priority

@pytest.fixture
def attribute_cleanup():
    # Setup code if needed
    yield
    # Cleanup code if needed

def test_attribute_comparison(attribute_cleanup):
    # Create two instances of MockAttribute with different priorities
    attr_high_priority = MockAttribute(priority=10)
    attr_low_priority = MockAttribute(priority=5)

    # Test the __le__ method for both possible outcomes
    assert attr_high_priority <= attr_low_priority, "High priority should be less than or equal to low priority"
    assert not attr_low_priority <= attr_high_priority, "Low priority should not be less than or equal to high priority"
