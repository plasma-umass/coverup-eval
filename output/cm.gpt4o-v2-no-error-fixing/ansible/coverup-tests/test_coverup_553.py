# file: lib/ansible/constants.py:43-45
# asked: {"lines": [43, 45], "branches": []}
# gained: {"lines": [43, 45], "branches": []}

import pytest

def test_set_constant():
    from ansible.constants import set_constant

    # Prepare a dictionary to act as the export variable
    export_dict = {}

    # Call the function with test data
    set_constant('TEST_CONSTANT', 'test_value', export=export_dict)

    # Assert that the constant was set correctly
    assert export_dict['TEST_CONSTANT'] == 'test_value'

    # Clean up
    del export_dict['TEST_CONSTANT']
