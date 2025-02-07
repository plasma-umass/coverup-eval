# file: lib/ansible/playbook/base.py:792-815
# asked: {"lines": [792, 800, 801, 803, 804, 805, 807, 808, 810, 813, 814, 815], "branches": [[800, 801], [800, 803], [803, 804], [803, 813], [804, 805], [804, 807], [807, 808], [807, 810]]}
# gained: {"lines": [792, 800, 801, 803, 804, 805, 807, 808, 810, 813, 814, 815], "branches": [[800, 801], [800, 803], [803, 804], [803, 813], [804, 805], [804, 807], [807, 808], [807, 810]]}

import pytest
from ansible.playbook.base import FieldAttributeBase
from ansible.errors import AnsibleAssertionError

class MockAttribute:
    def __init__(self, default):
        self.default = default

def test_deserialize_with_invalid_data_type():
    obj = FieldAttributeBase()
    with pytest.raises(AnsibleAssertionError, match="data .* should be a dict but is a .*"):
        obj.deserialize([])

def test_deserialize_with_valid_data(monkeypatch):
    obj = FieldAttributeBase()
    obj._valid_attrs = {
        'attr1': MockAttribute(default='default1'),
        'attr2': MockAttribute(default=lambda: 'default2')
    }
    data = {
        'attr1': 'value1',
        'uuid': 'test-uuid',
        'finalized': True,
        'squashed': True
    }
    
    obj.deserialize(data)
    
    assert obj.attr1 == 'value1'
    assert obj.attr2 == 'default2'
    assert obj._uuid == 'test-uuid'
    assert obj._finalized is True
    assert obj._squashed is True

def test_deserialize_with_missing_attributes(monkeypatch):
    obj = FieldAttributeBase()
    obj._valid_attrs = {
        'attr1': MockAttribute(default='default1'),
        'attr2': MockAttribute(default=lambda: 'default2')
    }
    data = {
        'uuid': 'test-uuid',
        'finalized': False,
        'squashed': False
    }
    
    obj.deserialize(data)
    
    assert obj.attr1 == 'default1'
    assert obj.attr2 == 'default2'
    assert obj._uuid == 'test-uuid'
    assert obj._finalized is False
    assert obj._squashed is False
