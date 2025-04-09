# file: lib/ansible/playbook/base.py:322-347
# asked: {"lines": [342, 343, 344], "branches": [[326, 347], [340, 328], [341, 342]]}
# gained: {"lines": [342, 343, 344], "branches": [[341, 342]]}

import pytest
from ansible.playbook.base import FieldAttributeBase
from ansible.errors import AnsibleParserError

class MockAttribute:
    def __init__(self, isa):
        self.isa = isa

class MockFieldAttributeBase(FieldAttributeBase):
    def __init__(self):
        self._validated = False
        self._valid_attrs = {
            'test_attr': MockAttribute('string')
        }
        self._alias_attrs = {}
        self._attributes = {
            'test_attr': ['not', 'a', 'string']
        }

    def get_ds(self):
        return 'mock_ds'

def test_validate_string_type_error():
    obj = MockFieldAttributeBase()
    with pytest.raises(AnsibleParserError) as excinfo:
        obj.validate()
    assert "The field 'test_attr' is supposed to be a string type," in str(excinfo.value)
    assert obj._validated is False

def test_validate_success(monkeypatch):
    obj = MockFieldAttributeBase()
    monkeypatch.setattr(obj, '_attributes', {'test_attr': 'a string'})
    obj.validate()
    assert obj._validated is True
