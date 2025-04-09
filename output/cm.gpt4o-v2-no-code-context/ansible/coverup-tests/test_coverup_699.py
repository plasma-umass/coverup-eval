# file: lib/ansible/constants.py:43-45
# asked: {"lines": [43, 45], "branches": []}
# gained: {"lines": [43, 45], "branches": []}

import pytest
from ansible.constants import set_constant

def test_set_constant():
    # Create a mock dictionary to act as the export variable
    mock_export = {}

    # Call the function with test data
    set_constant('TEST_CONSTANT', 'test_value', export=mock_export)

    # Assert that the constant was set correctly
    assert mock_export['TEST_CONSTANT'] == 'test_value'
