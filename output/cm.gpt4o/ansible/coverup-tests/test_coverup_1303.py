# file lib/ansible/playbook/attribute.py:97-98
# lines [98]
# branches []

import pytest
from ansible.playbook.attribute import Attribute

class TestAttribute:
    @pytest.fixture
    def attribute(self):
        class MockAttribute(Attribute):
            def __init__(self, priority):
                self.priority = priority

        return MockAttribute

    def test_attribute_eq(self, attribute):
        attr1 = attribute(priority=1)
        attr2 = attribute(priority=1)
        attr3 = attribute(priority=2)

        assert attr1 == attr2  # This should trigger line 98
        assert attr1 != attr3  # This should also trigger line 98

        # Clean up
        del attr1
        del attr2
        del attr3
