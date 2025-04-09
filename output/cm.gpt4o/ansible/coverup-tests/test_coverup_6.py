# file lib/ansible/playbook/base.py:557-606
# lines [557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606]
# branches ['558->559', '558->560', '560->561', '560->562', '562->563', '562->564', '564->565', '564->566', '566->569', '566->572', '569->570', '569->571', '572->573', '572->585', '573->574', '573->575', '575->576', '575->577', '577->578', '577->606', '578->579', '578->606', '579->580', '579->582', '582->578', '582->583', '583->578', '583->584', '585->586', '585->597', '586->587', '586->588', '588->589', '588->595', '589->590', '589->594', '595->596', '595->606', '597->598', '597->602', '598->599', '598->600', '600->601', '600->606', '602->603', '602->606', '603->604', '603->605']

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

class MockClassType:
    def post_validate(self, templar):
        pass

@pytest.fixture
def field_attribute_base():
    return FieldAttributeBase()

def test_get_validated_value_string(field_attribute_base):
    attribute = MockAttribute(isa='string')
    value = field_attribute_base.get_validated_value('test', attribute, 123, None)
    assert value == '123'

def test_get_validated_value_int(field_attribute_base):
    attribute = MockAttribute(isa='int')
    value = field_attribute_base.get_validated_value('test', attribute, '123', None)
    assert value == 123

def test_get_validated_value_float(field_attribute_base):
    attribute = MockAttribute(isa='float')
    value = field_attribute_base.get_validated_value('test', attribute, '123.45', None)
    assert value == 123.45

def test_get_validated_value_bool(field_attribute_base):
    attribute = MockAttribute(isa='bool')
    value = field_attribute_base.get_validated_value('test', attribute, 'yes', None)
    assert value is True

def test_get_validated_value_percent(field_attribute_base):
    attribute = MockAttribute(isa='percent')
    value = field_attribute_base.get_validated_value('test', attribute, '50%', None)
    assert value == 50.0

def test_get_validated_value_list(field_attribute_base):
    attribute = MockAttribute(isa='list', listof=str)
    value = field_attribute_base.get_validated_value('test', attribute, 'item', None)
    assert value == ['item']

def test_get_validated_value_list_invalid_item(field_attribute_base):
    attribute = MockAttribute(isa='list', listof=int)
    with pytest.raises(AnsibleParserError):
        field_attribute_base.get_validated_value('test', attribute, 'item', None)

def test_get_validated_value_set(field_attribute_base):
    attribute = MockAttribute(isa='set')
    value = field_attribute_base.get_validated_value('test', attribute, 'item1,item2', None)
    assert value == {'item1', 'item2'}

def test_get_validated_value_dict(field_attribute_base):
    attribute = MockAttribute(isa='dict')
    value = field_attribute_base.get_validated_value('test', attribute, None, None)
    assert value == {}

def test_get_validated_value_dict_invalid(field_attribute_base):
    attribute = MockAttribute(isa='dict')
    with pytest.raises(TypeError):
        field_attribute_base.get_validated_value('test', attribute, 'not_a_dict', None)

def test_get_validated_value_class(field_attribute_base):
    attribute = MockAttribute(isa='class', class_type=MockClassType)
    value = field_attribute_base.get_validated_value('test', attribute, MockClassType(), MockTemplar())
    assert isinstance(value, MockClassType)

def test_get_validated_value_class_invalid(field_attribute_base):
    attribute = MockAttribute(isa='class', class_type=MockClassType)
    with pytest.raises(TypeError):
        field_attribute_base.get_validated_value('test', attribute, 'not_a_class', None)
