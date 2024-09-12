# file: lib/ansible/playbook/base.py:529-555
# asked: {"lines": [529, 534, 535, 536, 537, 539, 540, 541, 542, 543, 545, 546, 547, 548, 549, 552, 553, 555], "branches": [[539, 540], [539, 545], [540, 541], [540, 542], [552, 553], [552, 555]]}
# gained: {"lines": [529, 534, 535, 536, 537, 539, 540, 542, 543, 545, 546, 547, 548, 549, 552, 553, 555], "branches": [[539, 540], [539, 545], [540, 542], [552, 553], [552, 555]]}

import pytest
from copy import copy as shallowcopy
from ansible.errors import AnsibleError
from ansible.playbook.base import FieldAttributeBase

class TestFieldAttributeBase:
    
    def test_copy_success(self):
        original = FieldAttributeBase()
        original._valid_attrs = {'attr1': 'value1'}
        original._alias_attrs = []
        original._attributes = {'attr1': 'value1'}
        original._attr_defaults = {'attr1': 'default1'}
        original._loader = 'loader'
        original._variable_manager = 'variable_manager'
        original._validated = True
        original._finalized = True
        original._uuid = 'uuid'
        
        copy_obj = original.copy()
        
        assert copy_obj._attributes == original._attributes
        assert copy_obj._attr_defaults == original._attr_defaults
        assert copy_obj._loader == original._loader
        assert copy_obj._variable_manager == original._variable_manager
        assert copy_obj._validated == original._validated
        assert copy_obj._finalized == original._finalized
        assert copy_obj._uuid == original._uuid

    def test_copy_with_ds(self):
        original = FieldAttributeBase()
        original._valid_attrs = {'attr1': 'value1'}
        original._alias_attrs = []
        original._attributes = {'attr1': 'value1'}
        original._attr_defaults = {'attr1': 'default1'}
        original._loader = 'loader'
        original._variable_manager = 'variable_manager'
        original._validated = True
        original._finalized = True
        original._uuid = 'uuid'
        original._ds = 'ds_value'
        
        copy_obj = original.copy()
        
        assert copy_obj._attributes == original._attributes
        assert copy_obj._attr_defaults == original._attr_defaults
        assert copy_obj._loader == original._loader
        assert copy_obj._variable_manager == original._variable_manager
        assert copy_obj._validated == original._validated
        assert copy_obj._finalized == original._finalized
        assert copy_obj._uuid == original._uuid
        assert copy_obj._ds == original._ds

    def test_copy_runtime_error(self, mocker):
        mocker.patch.object(FieldAttributeBase, '__new__', side_effect=RuntimeError('error'))
        original = object.__new__(FieldAttributeBase)
        original.__init__()
        original._valid_attrs = {'attr1': 'value1'}
        original._alias_attrs = []
        original._attributes = {'attr1': 'value1'}
        original._attr_defaults = {'attr1': 'default1'}
        original._loader = 'loader'
        original._variable_manager = 'variable_manager'
        original._validated = True
        original._finalized = True
        original._uuid = 'uuid'
        
        with pytest.raises(AnsibleError) as excinfo:
            original.copy()
        
        assert 'Exceeded maximum object depth' in str(excinfo.value)
