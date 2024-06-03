# file lib/ansible/playbook/base.py:529-555
# lines [529, 534, 535, 536, 537, 539, 540, 541, 542, 543, 545, 546, 547, 548, 549, 552, 553, 555]
# branches ['539->540', '539->545', '540->541', '540->542', '552->553', '552->555']

import pytest
from unittest.mock import MagicMock, patch
from ansible.errors import AnsibleError
from ansible.playbook.base import FieldAttributeBase
from copy import deepcopy, copy as shallowcopy

class TestFieldAttributeBase:
    @pytest.fixture
    def field_attribute_base(self):
        class TestClass(FieldAttributeBase):
            _valid_attrs = {'attr1': None, 'attr2': None}
            _alias_attrs = []
            _attributes = {'attr1': 'value1', 'attr2': 'value2'}
            _attr_defaults = {'attr1': 'default1', 'attr2': 'default2'}
            _loader = MagicMock()
            _variable_manager = MagicMock()
            _validated = True
            _finalized = True
            _uuid = '1234-5678'
        
        return TestClass()

    def test_copy_success(self, field_attribute_base):
        new_instance = field_attribute_base.copy()
        
        assert new_instance._attributes == field_attribute_base._attributes
        assert new_instance._attr_defaults == field_attribute_base._attr_defaults
        assert new_instance._loader == field_attribute_base._loader
        assert new_instance._variable_manager == field_attribute_base._variable_manager
        assert new_instance._validated == field_attribute_base._validated
        assert new_instance._finalized == field_attribute_base._finalized
        assert new_instance._uuid == field_attribute_base._uuid

    def test_copy_with_ds(self, field_attribute_base):
        field_attribute_base._ds = 'some_data'
        new_instance = field_attribute_base.copy()
        
        assert new_instance._ds == 'some_data'

    def test_copy_runtime_error(self, mocker):
        class TestClass(FieldAttributeBase):
            def __init__(self):
                raise RuntimeError("Test error")
        
        instance = object.__new__(TestClass)
        
        with pytest.raises(AnsibleError) as excinfo:
            instance.copy()
        
        assert "Exceeded maximum object depth" in str(excinfo.value)
