# file lib/ansible/playbook/base.py:311-320
# lines [311, 317, 318, 319, 320]
# branches ['318->exit', '318->319', '319->318', '319->320']

import pytest
from ansible.playbook.base import FieldAttributeBase
from ansible.errors import AnsibleParserError

class TestFieldAttributeBase:
    def test_validate_attributes_valid(self):
        class TestClass(FieldAttributeBase):
            _valid_attrs = {'attr1': None, 'attr2': None}

        obj = TestClass()
        ds = {'attr1': 'value1', 'attr2': 'value2'}
        obj._valid_attrs = {'attr1': None, 'attr2': None}  # Ensure _valid_attrs is set correctly
        obj._validate_attributes(ds)  # Should not raise an exception

    def test_validate_attributes_invalid(self):
        class TestClass(FieldAttributeBase):
            _valid_attrs = {'attr1': None, 'attr2': None}

        obj = TestClass()
        ds = {'attr1': 'value1', 'invalid_attr': 'value2'}
        obj._valid_attrs = {'attr1': None, 'attr2': None}  # Ensure _valid_attrs is set correctly
        
        with pytest.raises(AnsibleParserError) as excinfo:
            obj._validate_attributes(ds)
        
        assert "'invalid_attr' is not a valid attribute for a TestClass" in str(excinfo.value)
        assert excinfo.value.obj == ds
