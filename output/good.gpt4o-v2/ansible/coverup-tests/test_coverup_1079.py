# file: lib/ansible/playbook/base.py:557-606
# asked: {"lines": [563, 569, 570, 571, 574, 580, 581, 584, 585, 586, 587, 588, 589, 590, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605], "branches": [[562, 563], [566, 569], [569, 570], [569, 571], [572, 585], [573, 574], [579, 580], [583, 584], [585, 586], [585, 597], [586, 587], [586, 588], [588, 589], [588, 595], [589, 590], [589, 594], [595, 596], [595, 606], [597, 598], [597, 602], [598, 599], [598, 600], [600, 601], [600, 606], [602, 603], [602, 606], [603, 604], [603, 605]]}
# gained: {"lines": [563, 569, 570, 571, 580, 581, 584, 585, 586, 588, 589, 590, 595, 596, 597, 598, 600, 601, 602, 603, 604, 605], "branches": [[562, 563], [566, 569], [569, 570], [572, 585], [579, 580], [583, 584], [585, 586], [585, 597], [586, 588], [588, 589], [589, 590], [595, 596], [597, 598], [597, 602], [598, 600], [600, 601], [600, 606], [602, 603], [603, 604], [603, 605]]}

import pytest
from ansible.module_utils.six import string_types
from ansible.module_utils.parsing.convert_bool import boolean
from ansible.errors import AnsibleParserError
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

class MockClassType:
    def post_validate(self, templar):
        pass

@pytest.fixture
def field_attribute_base():
    return FieldAttributeBase()

def test_get_validated_value_float(field_attribute_base):
    attribute = MockAttribute(isa='float')
    result = field_attribute_base.get_validated_value('test', attribute, '3.14', MockTemplar())
    assert result == 3.14

def test_get_validated_value_percent(field_attribute_base):
    attribute = MockAttribute(isa='percent')
    result = field_attribute_base.get_validated_value('test', attribute, '50%', MockTemplar())
    assert result == 50.0

def test_get_validated_value_list(field_attribute_base):
    attribute = MockAttribute(isa='list', listof=int)
    result = field_attribute_base.get_validated_value('test', attribute, [1, 2, 3], MockTemplar())
    assert result == [1, 2, 3]

    with pytest.raises(AnsibleParserError):
        field_attribute_base.get_validated_value('test', attribute, [1, 'two', 3], MockTemplar())

def test_get_validated_value_list_required(field_attribute_base):
    attribute = MockAttribute(isa='list', listof=string_types, required=True)
    with pytest.raises(AnsibleParserError):
        field_attribute_base.get_validated_value('test', attribute, ['valid', ''], MockTemplar())

def test_get_validated_value_set(field_attribute_base):
    attribute = MockAttribute(isa='set')
    result = field_attribute_base.get_validated_value('test', attribute, 'a,b,c', MockTemplar())
    assert result == {'a', 'b', 'c'}

def test_get_validated_value_dict(field_attribute_base):
    attribute = MockAttribute(isa='dict')
    result = field_attribute_base.get_validated_value('test', attribute, {'key': 'value'}, MockTemplar())
    assert result == {'key': 'value'}

    with pytest.raises(TypeError):
        field_attribute_base.get_validated_value('test', attribute, ['not', 'a', 'dict'], MockTemplar())

def test_get_validated_value_class(field_attribute_base):
    attribute = MockAttribute(isa='class', class_type=MockClassType)
    value = MockClassType()
    result = field_attribute_base.get_validated_value('test', attribute, value, MockTemplar())
    assert result == value

    with pytest.raises(TypeError):
        field_attribute_base.get_validated_value('test', attribute, 'not a class', MockTemplar())
