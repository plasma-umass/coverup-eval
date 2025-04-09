# file: lib/ansible/playbook/base.py:311-320
# asked: {"lines": [311, 317, 318, 319, 320], "branches": [[318, 0], [318, 319], [319, 318], [319, 320]]}
# gained: {"lines": [311, 317, 318, 319, 320], "branches": [[318, 0], [318, 319], [319, 318], [319, 320]]}

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.base import FieldAttributeBase

class TestFieldAttributeBase:
    
    def test_validate_attributes_valid(self):
        class TestClass(FieldAttributeBase):
            _valid_attrs = {'valid_key': None}
        
        obj = TestClass()
        obj._valid_attrs = {'valid_key': None}
        obj._validate_attributes({'valid_key': 'value'})
    
    def test_validate_attributes_invalid(self):
        class TestClass(FieldAttributeBase):
            _valid_attrs = {'valid_key': None}
        
        obj = TestClass()
        obj._valid_attrs = {'valid_key': None}
        with pytest.raises(AnsibleParserError) as excinfo:
            obj._validate_attributes({'invalid_key': 'value'})
        
        assert "'invalid_key' is not a valid attribute for a TestClass" in str(excinfo.value)
