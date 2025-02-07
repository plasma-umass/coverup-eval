# file: lib/ansible/playbook/base.py:753-772
# asked: {"lines": [757, 758, 759, 760, 761, 762, 763, 765, 771, 772], "branches": [[757, 758], [757, 771], [758, 757], [758, 759], [760, 761], [760, 765]]}
# gained: {"lines": [757, 758, 759, 760, 761, 762, 763, 765, 771, 772], "branches": [[757, 758], [757, 771], [758, 759], [760, 761], [760, 765]]}

import pytest
from unittest.mock import Mock
from ansible.playbook.base import FieldAttributeBase

class MockClassType:
    def deserialize(self, value):
        self.value = value

class MockAttribute:
    def __init__(self, isa, class_type=None):
        self.isa = isa
        self.class_type = class_type

@pytest.fixture
def field_attribute_base():
    fab = FieldAttributeBase()
    fab._valid_attrs = {
        'attr1': MockAttribute('class', MockClassType),
        'attr2': MockAttribute('other')
    }
    return fab

def test_from_attrs_with_class_type(field_attribute_base):
    attrs = {
        'attr1': {'key': 'value'},
        'attr2': 'some_value'
    }
    field_attribute_base.from_attrs(attrs)
    
    assert field_attribute_base._finalized is True
    assert field_attribute_base._squashed is True
    assert isinstance(field_attribute_base.attr1, MockClassType)
    assert field_attribute_base.attr1.value == {'key': 'value'}
    assert field_attribute_base.attr2 == 'some_value'

def test_from_attrs_without_class_type(field_attribute_base):
    attrs = {
        'attr2': 'some_value'
    }
    field_attribute_base.from_attrs(attrs)
    
    assert field_attribute_base._finalized is True
    assert field_attribute_base._squashed is True
    assert field_attribute_base.attr2 == 'some_value'
