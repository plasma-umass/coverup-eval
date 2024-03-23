# file lib/ansible/vars/manager.py:80-108
# lines [104, 107, 108]
# branches []

import os
import pytest
from ansible.errors import AnsibleError
from ansible.vars.manager import VariableManager
from ansible.utils.display import Display
from unittest.mock import MagicMock, patch

# Mock the Display class to capture warnings
@pytest.fixture
def display_mock(mocker):
    mocker.patch.object(Display, 'warning')

# Test function to cover lines 104-108
def test_variable_manager_fact_cache_exception(display_mock):
    with patch('ansible.vars.manager.FactCache') as mock_fact_cache:
        # Simulate an AnsibleError being raised when FactCache is called
        mock_fact_cache.side_effect = AnsibleError("Simulated FactCache error")

        # Create an instance of VariableManager, which should handle the exception
        vm = VariableManager()

        # Assert that the fallback to a dict occurred
        assert isinstance(vm._fact_cache, dict), "Fact cache should be a dict on AnsibleError"

        # Assert that the warning was displayed
        Display.warning.assert_called_once_with("Simulated FactCache error")

        # Clean up the mock
        mock_fact_cache.side_effect = None
