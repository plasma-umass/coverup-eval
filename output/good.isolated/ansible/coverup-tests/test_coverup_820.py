# file lib/ansible/constants.py:43-45
# lines [43, 45]
# branches []

import pytest
from ansible.constants import set_constant

def test_set_constant():
    # Setup a mock dictionary to act as the export dict
    mock_export = {}

    # Call the set_constant function with a test name and value
    set_constant('TEST_CONSTANT', 'test_value', export=mock_export)

    # Assert that the constant was set correctly
    assert 'TEST_CONSTANT' in mock_export
    assert mock_export['TEST_CONSTANT'] == 'test_value'

    # Cleanup is not necessary as we are using a local dictionary
