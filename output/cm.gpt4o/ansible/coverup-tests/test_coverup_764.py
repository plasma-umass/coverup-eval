# file lib/ansible/constants.py:43-45
# lines [43, 45]
# branches []

import pytest
from ansible import constants

def test_set_constant(mocker):
    # Mock the export dictionary
    mock_export = {}
    mocker.patch('ansible.constants.vars', return_value=mock_export)

    # Call the function with test data
    constants.set_constant('TEST_CONSTANT', 'test_value', export=mock_export)

    # Assert that the constant was set correctly
    assert mock_export['TEST_CONSTANT'] == 'test_value'
