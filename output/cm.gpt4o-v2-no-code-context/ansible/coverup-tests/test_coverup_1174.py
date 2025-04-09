# file: lib/ansible/playbook/base.py:557-606
# asked: {"lines": [583, 584, 594], "branches": [[569, 571], [582, 583], [583, 578], [583, 584], [589, 594], [600, 606], [602, 606]]}
# gained: {"lines": [583, 584, 594], "branches": [[582, 583], [583, 578], [583, 584], [589, 594]]}

import pytest
from ansible.playbook.base import FieldAttributeBase
from ansible.errors import AnsibleParserError
from ansible.module_utils.six import string_types
from ansible.module_utils._text import to_text

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

def test_list_required_string(field_attribute_base):
    attribute = MockAttribute(isa='list', listof=string_types, required=True)
    value = ["valid", " ", None]
    with pytest.raises(AnsibleParserError, match="the field 'test' is required, and cannot have empty values"):
        field_attribute_base.get_validated_value("test", attribute, value, MockTemplar())

def test_set_string(field_attribute_base):
    attribute = MockAttribute(isa='set')
    value = "a,b,c"
    result = field_attribute_base.get_validated_value("test", attribute, value, MockTemplar())
    assert result == {"a", "b", "c"}

def test_set_non_string(field_attribute_base):
    attribute = MockAttribute(isa='set')
    value = 123
    result = field_attribute_base.get_validated_value("test", attribute, value, MockTemplar())
    assert result == {123}

def test_dict_invalid_type(field_attribute_base):
    attribute = MockAttribute(isa='dict')
    value = []
    with pytest.raises(TypeError, match=r"\[\] is not a dictionary"):
        field_attribute_base.get_validated_value("test", attribute, value, MockTemplar())

def test_class_invalid_type(field_attribute_base):
    class MockClass:
        def post_validate(self, templar):
            pass

    attribute = MockAttribute(isa='class', class_type=MockClass)
    value = "not_a_class_instance"
    with pytest.raises(TypeError, match="test is not a valid <class '.*MockClass'>"):
        field_attribute_base.get_validated_value("test", attribute, value, MockTemplar())
