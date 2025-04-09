# file lib/ansible/playbook/base.py:301-302
# lines [301, 302]
# branches []

import pytest
from unittest.mock import MagicMock, patch

# Assuming the module and class are imported correctly
from ansible.playbook.base import FieldAttributeBase

@pytest.fixture
def mock_variable_manager():
    return MagicMock()

@pytest.fixture
def field_attribute_base_instance(mock_variable_manager):
    instance = FieldAttributeBase()
    instance._variable_manager = mock_variable_manager
    return instance

def test_get_variable_manager(field_attribute_base_instance, mock_variable_manager):
    # Act
    result = field_attribute_base_instance.get_variable_manager()

    # Assert
    assert result == mock_variable_manager

    # Clean up
    del field_attribute_base_instance._variable_manager
