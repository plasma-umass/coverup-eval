# file lib/ansible/playbook/base.py:197-223
# lines [197, 201, 202, 205, 206, 207, 210, 216, 217, 218, 219, 220, 223]
# branches ['218->219', '218->223', '219->218', '219->220']

import pytest
from unittest.mock import patch, MagicMock
from ansible.playbook.base import FieldAttributeBase

@pytest.fixture
def mock_get_unique_id(mocker):
    return mocker.patch('ansible.playbook.base.get_unique_id', return_value='test-uuid')

def test_field_attribute_base_initialization(mock_get_unique_id):
    # Create an instance of FieldAttributeBase
    instance = FieldAttributeBase()

    # Assertions to verify the initialization
    assert instance._loader is None
    assert instance._variable_manager is None
    assert instance._validated is False
    assert instance._squashed is False
    assert instance._finalized is False
    assert instance._uuid == 'test-uuid'
    assert isinstance(instance._attributes, dict)
    assert isinstance(instance._attr_defaults, dict)
    assert isinstance(instance.vars, dict)

    # Verify that the _attributes and _attr_defaults are copies
    assert instance._attributes is not FieldAttributeBase._attributes
    assert instance._attr_defaults is not FieldAttributeBase._attr_defaults

    # Verify that callable defaults are called
    for key, value in FieldAttributeBase._attr_defaults.items():
        if callable(value):
            assert instance._attr_defaults[key] == value()

    # Clean up
    mock_get_unique_id.stop()
