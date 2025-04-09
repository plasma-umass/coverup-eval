# file: lib/ansible/playbook/base.py:322-347
# asked: {"lines": [331, 342, 343, 344], "branches": [[326, 347], [330, 331], [340, 328], [341, 342]]}
# gained: {"lines": [331, 342, 343, 344], "branches": [[330, 331], [341, 342]]}

import pytest
from ansible.errors import AnsibleParserError
from ansible.module_utils.six import iteritems
from ansible.playbook.base import FieldAttributeBase

class TestFieldAttributeBase:
    
    def setup_method(self):
        self.field_attr_base = FieldAttributeBase()
        self.field_attr_base._valid_attrs = {
            'attr1': type('Attribute', (object,), {'isa': 'string'}),
            'attr2': type('Attribute', (object,), {'isa': 'string'})
        }
        self.field_attr_base._alias_attrs = {'attr1': 'alias_attr1'}
        self.field_attr_base._attributes = {
            'alias_attr1': 'value1',
            'attr2': ['not', 'a', 'string']
        }
        self.field_attr_base._validated = False

    def test_validate_with_alias_and_invalid_type(self):
        with pytest.raises(AnsibleParserError) as excinfo:
            self.field_attr_base.validate()
        assert "The field 'attr2' is supposed to be a string type" in str(excinfo.value)
        assert self.field_attr_base._validated is False

    def test_validate_successful(self):
        self.field_attr_base._attributes['attr2'] = 'a valid string'
        self.field_attr_base.validate()
        assert self.field_attr_base._validated is True
