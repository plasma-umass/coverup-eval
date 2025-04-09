# file: lib/ansible/playbook/base.py:197-223
# asked: {"lines": [197, 201, 202, 205, 206, 207, 210, 216, 217, 218, 219, 220, 223], "branches": [[218, 219], [218, 223], [219, 218], [219, 220]]}
# gained: {"lines": [197, 201, 202, 205, 206, 207, 210, 216, 217, 218, 219, 220, 223], "branches": [[218, 219], [218, 223], [219, 218], [219, 220]]}

import pytest
from unittest.mock import patch
from ansible.playbook.base import FieldAttributeBase

@pytest.fixture
def mock_get_unique_id(mocker):
    return mocker.patch('ansible.playbook.base.get_unique_id', return_value='unique-id')

def test_field_attribute_base_initialization(mock_get_unique_id):
    class TestFieldAttributeBase(FieldAttributeBase):
        _attributes = {'attr1': 'value1'}
        _attr_defaults = {'default1': lambda: 'default-value1'}

    # Ensure class-level attributes are set before instantiation
    TestFieldAttributeBase._attributes = {'attr1': 'value1'}
    TestFieldAttributeBase._attr_defaults = {'default1': lambda: 'default-value1'}

    instance = TestFieldAttributeBase()

    assert instance._loader is None
    assert instance._variable_manager is None
    assert instance._validated is False
    assert instance._squashed is False
    assert instance._finalized is False
    assert instance._uuid == 'unique-id'
    assert instance._attributes == {'attr1': 'value1'}
    assert instance._attr_defaults == {'default1': 'default-value1'}
    assert instance.vars == {}

def test_field_attribute_base_callable_defaults(mock_get_unique_id):
    class TestFieldAttributeBase(FieldAttributeBase):
        _attributes = {'attr1': 'value1'}
        _attr_defaults = {'default1': lambda: 'default-value1', 'default2': 'static-value'}

    # Ensure class-level attributes are set before instantiation
    TestFieldAttributeBase._attributes = {'attr1': 'value1'}
    TestFieldAttributeBase._attr_defaults = {'default1': lambda: 'default-value1', 'default2': 'static-value'}

    instance = TestFieldAttributeBase()

    assert instance._attr_defaults['default1'] == 'default-value1'
    assert instance._attr_defaults['default2'] == 'static-value'
