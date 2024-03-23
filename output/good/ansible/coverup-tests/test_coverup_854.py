# file lib/ansible/playbook/base.py:298-299
# lines [298, 299]
# branches []

import pytest
from ansible.playbook.base import FieldAttributeBase
from mock import MagicMock

# Define a test case for the FieldAttributeBase class
def test_field_attribute_base_get_loader():
    # Create an instance of FieldAttributeBase with a mock loader
    field_attribute_base = FieldAttributeBase()
    mock_loader = MagicMock()
    field_attribute_base._loader = mock_loader

    # Call the get_loader method
    result = field_attribute_base.get_loader()

    # Assert that the result is the mock loader
    assert result == mock_loader

    # Clean up by deleting the instance
    del field_attribute_base
