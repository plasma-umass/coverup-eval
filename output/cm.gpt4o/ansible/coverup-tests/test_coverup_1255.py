# file lib/ansible/playbook/base.py:681-713
# lines [701]
# branches ['700->701']

import pytest
from ansible.playbook.base import FieldAttributeBase
from ansible.errors import AnsibleParserError

class TestFieldAttributeBase:
    def setup_method(self):
        self.instance = FieldAttributeBase()
        self.instance.vars = {}

    def test_load_vars_with_invalid_list_item(self):
        with pytest.raises(AnsibleParserError) as excinfo:
            self.instance._load_vars('attr', [1, 2, 3])
        assert "Vars in a FieldAttributeBase must be specified as a dictionary, or a list of dictionaries" in str(excinfo.value)

    def test_load_vars_with_invalid_dict_key(self):
        with pytest.raises(AnsibleParserError) as excinfo:
            self.instance._load_vars('attr', {'invalid-key!': 'value'})
        assert "Invalid variable name in vars specified for FieldAttributeBase" in str(excinfo.value)
