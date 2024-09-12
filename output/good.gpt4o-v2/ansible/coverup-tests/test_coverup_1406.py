# file: lib/ansible/playbook/base.py:681-713
# asked: {"lines": [708], "branches": [[705, 708]]}
# gained: {"lines": [708], "branches": [[705, 708]]}

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.base import FieldAttributeBase

class TestFieldAttributeBase:
    
    def setup_method(self):
        self.instance = FieldAttributeBase()
        self.instance.vars = {}

    def test_load_vars_with_invalid_type(self):
        with pytest.raises(AnsibleParserError, match="Vars in a FieldAttributeBase must be specified as a dictionary, or a list of dictionaries"):
            self.instance._load_vars('attr', 'invalid_type')

    def test_load_vars_with_none(self):
        result = self.instance._load_vars('attr', None)
        assert result == {}

    def test_load_vars_with_invalid_dict_key(self):
        with pytest.raises(AnsibleParserError, match="Invalid variable name in vars specified for FieldAttributeBase"):
            self.instance._load_vars('attr', {'invalid key': 'value'})

    def test_load_vars_with_invalid_list_item(self):
        with pytest.raises(AnsibleParserError, match="Vars in a FieldAttributeBase must be specified as a dictionary, or a list of dictionaries"):
            self.instance._load_vars('attr', [{'valid_key': 'value'}, 'invalid_item'])

    def test_load_vars_with_valid_dict(self):
        result = self.instance._load_vars('attr', {'valid_key': 'value'})
        assert result == {'valid_key': 'value'}

    def test_load_vars_with_valid_list_of_dicts(self):
        result = self.instance._load_vars('attr', [{'valid_key1': 'value1'}, {'valid_key2': 'value2'}])
        assert result == {'valid_key1': 'value1', 'valid_key2': 'value2'}
