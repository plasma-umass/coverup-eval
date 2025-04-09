# file: lib/ansible/playbook/base.py:529-555
# asked: {"lines": [536, 537, 553], "branches": [[552, 553]]}
# gained: {"lines": [536, 537, 553], "branches": [[552, 553]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.playbook.base import FieldAttributeBase
from ansible.errors import AnsibleError

class TestFieldAttributeBase:
    
    def test_copy_runtime_error(self):
        # Mock the instantiation of the class to raise RuntimeError
        with patch.object(FieldAttributeBase, '__init__', side_effect=RuntimeError("Test Error")):
            obj = FieldAttributeBase.__new__(FieldAttributeBase)
            with pytest.raises(AnsibleError) as excinfo:
                obj.copy()
            assert "Exceeded maximum object depth" in str(excinfo.value)
    
    def test_copy_with_ds(self):
        obj = FieldAttributeBase()
        obj._valid_attrs = {'attr1': None}
        obj._alias_attrs = {}
        obj._attributes = {'attr1': 'value1'}
        obj._attr_defaults = {'attr1': 'default1'}
        obj._loader = MagicMock()
        obj._variable_manager = MagicMock()
        obj._validated = True
        obj._finalized = True
        obj._uuid = 'uuid'
        obj._ds = 'ds_value'
        
        new_obj = obj.copy()
        
        assert new_obj._attributes == obj._attributes
        assert new_obj._attr_defaults == obj._attr_defaults
        assert new_obj._loader == obj._loader
        assert new_obj._variable_manager == obj._variable_manager
        assert new_obj._validated == obj._validated
        assert new_obj._finalized == obj._finalized
        assert new_obj._uuid == obj._uuid
        assert new_obj._ds == obj._ds
