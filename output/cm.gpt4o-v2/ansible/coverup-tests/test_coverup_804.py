# file: lib/ansible/constants.py:43-45
# asked: {"lines": [43, 45], "branches": []}
# gained: {"lines": [43, 45], "branches": []}

import pytest

from ansible.constants import set_constant

def test_set_constant():
    # Prepare the test data
    name = "TEST_CONSTANT"
    value = "test_value"
    export = {}

    # Call the function
    set_constant(name, value, export)

    # Assert the postconditions
    assert export[name] == value

    # Clean up
    del export[name]
