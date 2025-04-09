# file: lib/ansible/playbook/base.py:557-606
# asked: {"lines": [574, 583, 584, 587, 594, 604], "branches": [[569, 571], [573, 574], [582, 583], [583, 578], [583, 584], [586, 587], [588, 595], [589, 594], [595, 606], [600, 606], [602, 606], [603, 604]]}
# gained: {"lines": [574, 583, 584, 587, 604], "branches": [[573, 574], [582, 583], [583, 584], [586, 587], [588, 595], [595, 606], [603, 604]]}

import pytest
from ansible.playbook.base import FieldAttributeBase
from ansible.errors import AnsibleParserError
from ansible.module_utils.six import string_types
from unittest.mock import MagicMock

class MockAttribute:
    def __init__(self, isa, listof=None, required=False, class_type=None):
        self.isa = isa
        self.listof = listof
        self.required = required
        self.class_type = class_type

@pytest.fixture
def field_attribute_base():
    return FieldAttributeBase()

def test_percent_string_conversion(field_attribute_base):
    attribute = MockAttribute(isa='percent')
    value = "50%"
    result = field_attribute_base.get_validated_value("test", attribute, value, None)
    assert result == 50.0

def test_list_none_conversion(field_attribute_base):
    attribute = MockAttribute(isa='list')
    value = None
    result = field_attribute_base.get_validated_value("test", attribute, value, None)
    assert result == []

def test_list_empty_string(field_attribute_base):
    attribute = MockAttribute(isa='list', listof=string_types, required=True)
    value = [" "]
    with pytest.raises(AnsibleParserError):
        field_attribute_base.get_validated_value("test", attribute, value, None)

def test_set_none_conversion(field_attribute_base):
    attribute = MockAttribute(isa='set')
    value = None
    result = field_attribute_base.get_validated_value("test", attribute, value, None)
    assert result == set()

def test_set_string_split(field_attribute_base):
    attribute = MockAttribute(isa='set')
    value = "a,b,c"
    result = field_attribute_base.get_validated_value("test", attribute, value, None)
    assert result == {"a", "b", "c"}

def test_set_conversion(field_attribute_base):
    attribute = MockAttribute(isa='set')
    value = ["a", "b", "c"]
    result = field_attribute_base.get_validated_value("test", attribute, value, None)
    assert result == {"a", "b", "c"}

def test_dict_type_error(field_attribute_base):
    attribute = MockAttribute(isa='dict')
    value = []
    with pytest.raises(TypeError):
        field_attribute_base.get_validated_value("test", attribute, value, None)

def test_class_type_error(field_attribute_base):
    class MockClass:
        def post_validate(self, templar):
            pass

    attribute = MockAttribute(isa='class', class_type=MockClass)
    value = "not_a_class_instance"
    with pytest.raises(TypeError):
        field_attribute_base.get_validated_value("test", attribute, value, None)

def test_class_post_validate(field_attribute_base, mocker):
    class MockClass:
        def post_validate(self, templar):
            self.validated = True

    attribute = MockAttribute(isa='class', class_type=MockClass)
    value = MockClass()
    mocker.patch.object(value, 'post_validate', wraps=value.post_validate)
    result = field_attribute_base.get_validated_value("test", attribute, value, None)
    value.post_validate.assert_called_once_with(templar=None)
    assert result == value
