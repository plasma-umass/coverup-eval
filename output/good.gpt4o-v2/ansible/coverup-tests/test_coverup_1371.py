# file: lib/ansible/playbook/base.py:557-606
# asked: {"lines": [574, 587, 594, 599], "branches": [[569, 571], [573, 574], [586, 587], [588, 595], [589, 594], [595, 606], [598, 599], [602, 606]]}
# gained: {"lines": [574, 587, 594, 599], "branches": [[573, 574], [586, 587], [589, 594], [595, 606], [598, 599]]}

import pytest
from ansible.errors import AnsibleParserError
from ansible.module_utils.six import string_types
from ansible.module_utils.parsing.convert_bool import boolean
from ansible.module_utils._text import to_text
from ansible.playbook.base import FieldAttributeBase

class MockAttribute:
    def __init__(self, isa, listof=None, required=False, class_type=None):
        self.isa = isa
        self.listof = listof
        self.required = required
        self.class_type = class_type

class MockTemplar:
    pass

def test_percent_with_string():
    field = FieldAttributeBase()
    attribute = MockAttribute(isa='percent')
    value = "50%"
    result = field.get_validated_value("test", attribute, value, MockTemplar())
    assert result == 50.0

def test_list_with_none():
    field = FieldAttributeBase()
    attribute = MockAttribute(isa='list')
    value = None
    result = field.get_validated_value("test", attribute, value, MockTemplar())
    assert result == []

def test_set_with_none():
    field = FieldAttributeBase()
    attribute = MockAttribute(isa='set')
    value = None
    result = field.get_validated_value("test", attribute, value, MockTemplar())
    assert result == set()

def test_set_with_string():
    field = FieldAttributeBase()
    attribute = MockAttribute(isa='set')
    value = "a,b,c"
    result = field.get_validated_value("test", attribute, value, MockTemplar())
    assert result == {"a", "b", "c"}

def test_set_with_non_iterable():
    field = FieldAttributeBase()
    attribute = MockAttribute(isa='set')
    value = 123
    result = field.get_validated_value("test", attribute, value, MockTemplar())
    assert result == {123}

def test_dict_with_none():
    field = FieldAttributeBase()
    attribute = MockAttribute(isa='dict')
    value = None
    result = field.get_validated_value("test", attribute, value, MockTemplar())
    assert result == {}

def test_class_with_invalid_type():
    class MockClass:
        def post_validate(self, templar):
            pass

    field = FieldAttributeBase()
    attribute = MockAttribute(isa='class', class_type=MockClass)
    value = "not a class instance"
    with pytest.raises(TypeError):
        field.get_validated_value("test", attribute, value, MockTemplar())
