# file lib/ansible/playbook/base.py:557-606
# lines [574, 583, 584, 587, 594]
# branches ['569->571', '573->574', '575->577', '577->606', '582->583', '583->578', '583->584', '586->587', '588->595', '589->594', '595->606', '600->606', '602->606']

import pytest
from ansible.playbook.base import FieldAttributeBase
from ansible.errors import AnsibleParserError
from ansible.module_utils.six import string_types
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

class TestFieldAttributeBase:
    def setup_method(self):
        self.field_attribute_base = FieldAttributeBase()

    def test_percent_string(self):
        attribute = MockAttribute(isa='percent')
        value = "50%"
        result = self.field_attribute_base.get_validated_value('test', attribute, value, MockTemplar())
        assert result == 50.0

    def test_list_none(self):
        attribute = MockAttribute(isa='list')
        value = None
        result = self.field_attribute_base.get_validated_value('test', attribute, value, MockTemplar())
        assert result == []

    def test_list_not_list(self):
        attribute = MockAttribute(isa='list')
        value = "not_a_list"
        result = self.field_attribute_base.get_validated_value('test', attribute, value, MockTemplar())
        assert result == ["not_a_list"]

    def test_list_required_string(self):
        attribute = MockAttribute(isa='list', listof=string_types, required=True)
        value = ["valid", " "]
        with pytest.raises(AnsibleParserError):
            self.field_attribute_base.get_validated_value('test', attribute, value, MockTemplar())

    def test_set_none(self):
        attribute = MockAttribute(isa='set')
        value = None
        result = self.field_attribute_base.get_validated_value('test', attribute, value, MockTemplar())
        assert result == set()

    def test_set_not_list_or_set(self):
        attribute = MockAttribute(isa='set')
        value = "a,b,c"
        result = self.field_attribute_base.get_validated_value('test', attribute, value, MockTemplar())
        assert result == {"a", "b", "c"}

    def test_set_not_set(self):
        attribute = MockAttribute(isa='set')
        value = ["a", "b", "c"]
        result = self.field_attribute_base.get_validated_value('test', attribute, value, MockTemplar())
        assert result == {"a", "b", "c"}

    def test_dict_not_dict(self):
        attribute = MockAttribute(isa='dict')
        value = "not_a_dict"
        with pytest.raises(TypeError):
            self.field_attribute_base.get_validated_value('test', attribute, value, MockTemplar())

    def test_class_type(self, mocker):
        class MockClass:
            def post_validate(self, templar):
                pass

        attribute = MockAttribute(isa='class', class_type=MockClass)
        value = MockClass()
        mock_post_validate = mocker.patch.object(value, 'post_validate')
        result = self.field_attribute_base.get_validated_value('test', attribute, value, MockTemplar())
        mock_post_validate.assert_called_once()
        assert result == value
