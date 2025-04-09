# file lib/ansible/utils/unsafe_proxy.py:145-146
# lines [145, 146]
# branches []

import pytest
from ansible.utils.unsafe_proxy import to_unsafe_text
from ansible.module_utils._text import to_text

def test_to_unsafe_text(mocker):
    # Mock the wrap_var function
    mock_wrap_var = mocker.patch('ansible.utils.unsafe_proxy.wrap_var', side_effect=lambda x: f"unsafe_{x}")

    # Test data
    input_data = "test_string"
    expected_output = f"unsafe_{to_text(input_data)}"

    # Call the function
    result = to_unsafe_text(input_data)

    # Assertions
    assert result == expected_output
    mock_wrap_var.assert_called_once_with(to_text(input_data))
