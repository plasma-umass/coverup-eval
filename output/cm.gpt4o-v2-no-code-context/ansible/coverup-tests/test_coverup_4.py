# file: lib/ansible/playbook/base.py:557-606
# asked: {"lines": [557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606], "branches": [[558, 559], [558, 560], [560, 561], [560, 562], [562, 563], [562, 564], [564, 565], [564, 566], [566, 569], [566, 572], [569, 570], [569, 571], [572, 573], [572, 585], [573, 574], [573, 575], [575, 576], [575, 577], [577, 578], [577, 606], [578, 579], [578, 606], [579, 580], [579, 582], [582, 578], [582, 583], [583, 578], [583, 584], [585, 586], [585, 597], [586, 587], [586, 588], [588, 589], [588, 595], [589, 590], [589, 594], [595, 596], [595, 606], [597, 598], [597, 602], [598, 599], [598, 600], [600, 601], [600, 606], [602, 603], [602, 606], [603, 604], [603, 605]]}
# gained: {"lines": [557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 569, 570, 571, 572, 573, 575, 576, 577, 578, 579, 580, 581, 582, 585, 586, 588, 589, 590, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606], "branches": [[558, 559], [558, 560], [560, 561], [560, 562], [562, 563], [562, 564], [564, 565], [564, 566], [566, 569], [566, 572], [569, 570], [572, 573], [572, 585], [573, 575], [575, 576], [575, 577], [577, 578], [577, 606], [578, 579], [578, 606], [579, 580], [579, 582], [582, 578], [585, 586], [585, 597], [586, 588], [588, 589], [589, 590], [595, 596], [597, 598], [597, 602], [598, 599], [598, 600], [600, 601], [602, 603], [603, 604], [603, 605]]}

import pytest
from ansible.playbook.base import FieldAttributeBase
from ansible.errors import AnsibleParserError
from ansible.module_utils._text import to_text
from ansible.module_utils.common.collections import ImmutableDict
from ansible.module_utils.common._collections_compat import Sequence
from ansible.module_utils.parsing.convert_bool import boolean

class MockAttribute:
    def __init__(self, isa, listof=None, required=False, class_type=None):
        self.isa = isa
        self.listof = listof
        self.required = required
        self.class_type = class_type

class MockTemplar:
    pass

class TestFieldAttributeBase:
    def setup_method(self):
        self.field_attr_base = FieldAttributeBase()

    def test_get_validated_value_string(self):
        attribute = MockAttribute(isa='string')
        value = self.field_attr_base.get_validated_value('test', attribute, 123, MockTemplar())
        assert value == '123'

    def test_get_validated_value_int(self):
        attribute = MockAttribute(isa='int')
        value = self.field_attr_base.get_validated_value('test', attribute, '123', MockTemplar())
        assert value == 123

    def test_get_validated_value_float(self):
        attribute = MockAttribute(isa='float')
        value = self.field_attr_base.get_validated_value('test', attribute, '123.45', MockTemplar())
        assert value == 123.45

    def test_get_validated_value_bool(self):
        attribute = MockAttribute(isa='bool')
        value = self.field_attr_base.get_validated_value('test', attribute, 'yes', MockTemplar())
        assert value is True

    def test_get_validated_value_percent(self):
        attribute = MockAttribute(isa='percent')
        value = self.field_attr_base.get_validated_value('test', attribute, '50%', MockTemplar())
        assert value == 50.0

    def test_get_validated_value_list(self):
        attribute = MockAttribute(isa='list')
        value = self.field_attr_base.get_validated_value('test', attribute, 'item', MockTemplar())
        assert value == ['item']

    def test_get_validated_value_list_with_listof(self):
        attribute = MockAttribute(isa='list', listof=str)
        value = self.field_attr_base.get_validated_value('test', attribute, ['item1', 'item2'], MockTemplar())
        assert value == ['item1', 'item2']

    def test_get_validated_value_list_with_listof_invalid(self):
        attribute = MockAttribute(isa='list', listof=str)
        with pytest.raises(AnsibleParserError):
            self.field_attr_base.get_validated_value('test', attribute, ['item1', 2], MockTemplar())

    def test_get_validated_value_set(self):
        attribute = MockAttribute(isa='set')
        value = self.field_attr_base.get_validated_value('test', attribute, 'item1,item2', MockTemplar())
        assert value == {'item1', 'item2'}

    def test_get_validated_value_dict(self):
        attribute = MockAttribute(isa='dict')
        value = self.field_attr_base.get_validated_value('test', attribute, None, MockTemplar())
        assert value == {}

    def test_get_validated_value_dict_invalid(self):
        attribute = MockAttribute(isa='dict')
        with pytest.raises(TypeError):
            self.field_attr_base.get_validated_value('test', attribute, 'not_a_dict', MockTemplar())

    def test_get_validated_value_class(self):
        class MockClass:
            def post_validate(self, templar):
                pass

        attribute = MockAttribute(isa='class', class_type=MockClass)
        value = self.field_attr_base.get_validated_value('test', attribute, MockClass(), MockTemplar())
        assert isinstance(value, MockClass)

    def test_get_validated_value_class_invalid(self):
        class MockClass:
            def post_validate(self, templar):
                pass

        attribute = MockAttribute(isa='class', class_type=MockClass)
        with pytest.raises(TypeError):
            self.field_attr_base.get_validated_value('test', attribute, 'not_a_class', MockTemplar())
