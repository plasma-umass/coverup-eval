# file lib/ansible/playbook/attribute.py:100-101
# lines [101]
# branches []

import pytest
from ansible.playbook.attribute import Attribute

class TestAttribute:
    def test_ne_method(self, mocker):
        # Create a mock object for 'other' with a 'priority' attribute
        other = mocker.Mock()
        other.priority = 10

        # Create an instance of Attribute with a 'priority' attribute
        attribute = Attribute()
        attribute.priority = 5

        # Test the __ne__ method
        assert attribute != other

        # Change the priority to match and test again
        other.priority = 5
        assert not attribute != other
