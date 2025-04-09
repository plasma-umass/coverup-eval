# file: lib/ansible/playbook/attribute.py:118-119
# asked: {"lines": [118, 119], "branches": []}
# gained: {"lines": [118, 119], "branches": []}

import pytest
from ansible.playbook.attribute import FieldAttribute, Attribute

def test_field_attribute_instantiation():
    # Create an instance of FieldAttribute
    field_attr = FieldAttribute()

    # Assert that the instance is indeed a FieldAttribute
    assert isinstance(field_attr, FieldAttribute)

    # Assert that the instance is also an instance of Attribute
    assert isinstance(field_attr, Attribute)

    # Assert that all attributes of the base class are present
    assert hasattr(field_attr, 'isa')
    assert hasattr(field_attr, 'private')
    assert hasattr(field_attr, 'default')
    assert hasattr(field_attr, 'required')
    assert hasattr(field_attr, 'listof')
    assert hasattr(field_attr, 'priority')
    assert hasattr(field_attr, 'class_type')
    assert hasattr(field_attr, 'always_post_validate')
    assert hasattr(field_attr, 'inherit')
    assert hasattr(field_attr, 'alias')
    assert hasattr(field_attr, 'extend')
    assert hasattr(field_attr, 'prepend')
    assert hasattr(field_attr, 'static')

@pytest.fixture
def mock_attribute_init(mocker):
    return mocker.patch('ansible.playbook.attribute.Attribute.__init__', return_value=None)

def test_field_attribute_init_calls_super(mock_attribute_init):
    # Create an instance of FieldAttribute
    field_attr = FieldAttribute()

    # Assert that the __init__ method of the base class was called
    mock_attribute_init.assert_called_once_with()
