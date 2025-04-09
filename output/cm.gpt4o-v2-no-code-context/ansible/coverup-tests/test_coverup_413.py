# file: lib/ansible/playbook/base.py:311-320
# asked: {"lines": [311, 317, 318, 319, 320], "branches": [[318, 0], [318, 319], [319, 318], [319, 320]]}
# gained: {"lines": [311, 317, 318, 319, 320], "branches": [[318, 0], [318, 319], [319, 318], [319, 320]]}

import pytest
from ansible.playbook.base import FieldAttributeBase
from ansible.errors import AnsibleParserError

class MockFieldAttributeBase(FieldAttributeBase):
    def __init__(self):
        self._valid_attrs = {'valid_key': 'some_value'}

def test_validate_attributes_valid_key():
    obj = MockFieldAttributeBase()
    ds = {'valid_key': 'some_value'}
    obj._validate_attributes(ds)  # Should not raise an exception

def test_validate_attributes_invalid_key():
    obj = MockFieldAttributeBase()
    ds = {'invalid_key': 'some_value'}
    with pytest.raises(AnsibleParserError) as excinfo:
        obj._validate_attributes(ds)
    assert "'invalid_key' is not a valid attribute for a MockFieldAttributeBase" in str(excinfo.value)
    assert excinfo.value.obj == ds
