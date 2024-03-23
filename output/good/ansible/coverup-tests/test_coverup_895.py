# file lib/ansible/playbook/attribute.py:118-119
# lines [118, 119]
# branches []

import pytest
from ansible.playbook.attribute import Attribute

# Since the FieldAttribute class does not have any functionality of its own,
# we will create a subclass that has some attributes and test that.

class TestFieldAttribute(Attribute):
    def __init__(self, name=None, default=None, required=False):
        super(TestFieldAttribute, self).__init__()
        self.name = name
        self.default = default
        self.required = required

def test_field_attribute_initialization():
    # Create an instance of the subclass with some values
    test_attr = TestFieldAttribute(name='test_name', default='test_default', required=True)
    
    # Assert that the values are correctly set
    assert test_attr.name == 'test_name'
    assert test_attr.default == 'test_default'
    assert test_attr.required is True

# Run the test
def test_field_attribute():
    test_field_attribute_initialization()
