# file: lib/ansible/playbook/base.py:792-815
# asked: {"lines": [801], "branches": [[800, 801]]}
# gained: {"lines": [801], "branches": [[800, 801]]}

import pytest
from ansible.errors import AnsibleAssertionError
from ansible.playbook.base import FieldAttributeBase
from unittest.mock import MagicMock

class MockAttribute:
    def __init__(self, default=None):
        self.default = default

@pytest.fixture
def mock_valid_attrs():
    return {
        'attr1': MockAttribute(default='default1'),
        'attr2': MockAttribute(default=lambda: 'default2'),
    }

@pytest.fixture
def field_attribute_base(mock_valid_attrs, monkeypatch):
    instance = FieldAttributeBase()
    monkeypatch.setattr(instance, '_valid_attrs', mock_valid_attrs)
    return instance

def test_deserialize_with_valid_data(field_attribute_base):
    data = {
        'attr1': 'value1',
        'attr2': 'value2',
        'uuid': '1234',
        'finalized': True,
        'squashed': True
    }
    field_attribute_base.deserialize(data)
    assert field_attribute_base.attr1 == 'value1'
    assert field_attribute_base.attr2 == 'value2'
    assert field_attribute_base._uuid == '1234'
    assert field_attribute_base._finalized is True
    assert field_attribute_base._squashed is True

def test_deserialize_with_missing_data(field_attribute_base):
    data = {
        'uuid': '1234',
        'finalized': False,
        'squashed': False
    }
    field_attribute_base.deserialize(data)
    assert field_attribute_base.attr1 == 'default1'
    assert field_attribute_base.attr2 == 'default2'
    assert field_attribute_base._uuid == '1234'
    assert field_attribute_base._finalized is False
    assert field_attribute_base._squashed is False

def test_deserialize_with_invalid_data(field_attribute_base):
    data = ['not', 'a', 'dict']
    with pytest.raises(AnsibleAssertionError):
        field_attribute_base.deserialize(data)
