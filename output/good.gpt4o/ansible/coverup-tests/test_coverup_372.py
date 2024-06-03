# file lib/ansible/modules/replace.py:213-223
# lines [213, 215, 216, 218, 219, 220, 221, 223]
# branches ['216->218', '216->223', '218->219', '218->220']

import pytest
from unittest.mock import Mock

def test_check_file_attrs(mocker):
    # Mock the module and its methods
    module = Mock()
    module.params = {}
    module.load_file_common_arguments.return_value = {}
    module.set_file_attributes_if_different.return_value = True

    # Import the function to test
    from ansible.modules.replace import check_file_attrs

    # Test when 'changed' is initially False
    message, changed = check_file_attrs(module, False, "Initial message")
    assert changed is True
    assert message == "Initial messageownership, perms or SE linux context changed"

    # Test when 'changed' is initially True
    message, changed = check_file_attrs(module, True, "Initial message")
    assert changed is True
    assert message == "Initial message and ownership, perms or SE linux context changed"

    # Ensure the mock was called as expected
    assert module.load_file_common_arguments.call_count == 2
    module.set_file_attributes_if_different.assert_called_with({}, False)
