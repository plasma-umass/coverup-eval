# file lib/ansible/playbook/base.py:311-320
# lines [311, 317, 318, 319, 320]
# branches ['318->exit', '318->319', '319->318', '319->320']

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.base import FieldAttributeBase

# Creating a subclass of FieldAttributeBase for testing
class TestFieldAttributeBase(FieldAttributeBase):
    _valid_attrs = {'valid_attr': None}

@pytest.fixture
def test_field_attribute_base():
    return TestFieldAttributeBase()

def test_validate_attributes_with_invalid_key(test_field_attribute_base):
    invalid_data_structure = {'invalid_attr': 'value'}
    with pytest.raises(AnsibleParserError) as excinfo:
        test_field_attribute_base._validate_attributes(invalid_data_structure)
    assert "'invalid_attr' is not a valid attribute for a TestFieldAttributeBase" in str(excinfo.value)
