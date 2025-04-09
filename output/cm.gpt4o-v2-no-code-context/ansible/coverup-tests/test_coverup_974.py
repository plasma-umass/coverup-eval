# file: lib/ansible/playbook/base.py:557-606
# asked: {"lines": [574, 583, 584, 587, 594], "branches": [[569, 571], [573, 574], [582, 583], [583, 578], [583, 584], [586, 587], [588, 595], [589, 594], [595, 606], [600, 606], [602, 606]]}
# gained: {"lines": [574, 587], "branches": [[573, 574], [586, 587], [588, 595], [595, 606]]}

import pytest
from ansible.playbook.base import FieldAttributeBase
from ansible.errors import AnsibleParserError
from ansible.module_utils._text import to_text
from ansible.module_utils.parsing.convert_bool import boolean

class MockAttribute:
    def __init__(self, isa, listof=None, required=False, class_type=None):
        self.isa = isa
        self.listof = listof
        self.required = required
        self.class_type = class_type

class MockTemplar:
    pass

class MockFieldAttributeBase(FieldAttributeBase):
    def get_ds(self):
        return {}

@pytest.fixture
def field_attribute_base():
    return MockFieldAttributeBase()

def test_percent_string(field_attribute_base):
    attribute = MockAttribute(isa='percent')
    value = "50%"
    result = field_attribute_base.get_validated_value("test", attribute, value, MockTemplar())
    assert result == 50.0

def test_list_none(field_attribute_base):
    attribute = MockAttribute(isa='list')
    value = None
    result = field_attribute_base.get_validated_value("test", attribute, value, MockTemplar())
    assert result == []

def test_list_required_string(field_attribute_base):
    attribute = MockAttribute(isa='list', listof=str, required=True)
    value = [None, "valid"]
    with pytest.raises(AnsibleParserError):
        field_attribute_base.get_validated_value("test", attribute, value, MockTemplar())

def test_set_none(field_attribute_base):
    attribute = MockAttribute(isa='set')
    value = None
    result = field_attribute_base.get_validated_value("test", attribute, value, MockTemplar())
    assert result == set()

def test_set_string(field_attribute_base):
    attribute = MockAttribute(isa='set')
    value = "a,b,c"
    result = field_attribute_base.get_validated_value("test", attribute, value, MockTemplar())
    assert result == {"a", "b", "c"}

def test_set_not_set(field_attribute_base):
    attribute = MockAttribute(isa='set')
    value = ["a", "b", "c"]
    result = field_attribute_base.get_validated_value("test", attribute, value, MockTemplar())
    assert result == {"a", "b", "c"}

def test_dict_not_dict(field_attribute_base):
    attribute = MockAttribute(isa='dict')
    value = ["not", "a", "dict"]
    with pytest.raises(TypeError):
        field_attribute_base.get_validated_value("test", attribute, value, MockTemplar())

def test_class_type(field_attribute_base):
    class MockClass:
        def post_validate(self, templar):
            pass

    attribute = MockAttribute(isa='class', class_type=MockClass)
    value = MockClass()
    result = field_attribute_base.get_validated_value("test", attribute, value, MockTemplar())
    assert result == value
