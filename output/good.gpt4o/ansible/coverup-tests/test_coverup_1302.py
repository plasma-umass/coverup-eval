# file lib/ansible/playbook/attribute.py:108-109
# lines [109]
# branches []

import pytest
from ansible.playbook.attribute import Attribute

class TestAttribute:
    def test_gt(self, mocker):
        # Create mock objects for self and other
        self_mock = mocker.Mock(spec=Attribute)
        other_mock = mocker.Mock(spec=Attribute)

        # Set the priority attributes
        self_mock.priority = 1
        other_mock.priority = 2

        # Use the __gt__ method and assert the result
        result = Attribute.__gt__(self_mock, other_mock)
        assert result == True

        # Change the priority to test the other branch
        self_mock.priority = 3
        result = Attribute.__gt__(self_mock, other_mock)
        assert result == False
