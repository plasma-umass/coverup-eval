# file: lib/ansible/playbook/base.py:301-302
# asked: {"lines": [301, 302], "branches": []}
# gained: {"lines": [301, 302], "branches": []}

import pytest
from unittest.mock import MagicMock

# Assuming the class FieldAttributeBase is imported from ansible.playbook.base
from ansible.playbook.base import FieldAttributeBase

class TestFieldAttributeBase:
    def test_get_variable_manager(self):
        # Create an instance of FieldAttributeBase
        instance = FieldAttributeBase()
        
        # Mock the _variable_manager attribute
        mock_variable_manager = MagicMock()
        instance._variable_manager = mock_variable_manager
        
        # Call the method and assert the return value
        result = instance.get_variable_manager()
        assert result == mock_variable_manager
