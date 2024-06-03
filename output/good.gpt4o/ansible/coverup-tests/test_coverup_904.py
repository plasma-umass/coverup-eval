# file lib/ansible/utils/unsafe_proxy.py:117-118
# lines [117, 118]
# branches []

import pytest
from ansible.utils.unsafe_proxy import wrap_var

def test_wrap_set(mocker):
    # Mock the wrap_var function to track its calls and return values
    mock_wrap_var = mocker.patch('ansible.utils.unsafe_proxy.wrap_var', side_effect=lambda x: f"wrapped_{x}")

    # Define a sample set to be wrapped
    sample_set = {1, 2, 3}

    # Define the _wrap_set function as extracted from the module
    def _wrap_set(v):
        return set(mock_wrap_var(item) for item in v)

    # Call the _wrap_set function with the sample set
    wrapped_set = _wrap_set(sample_set)

    # Verify that wrap_var was called for each item in the set
    assert mock_wrap_var.call_count == len(sample_set)
    for item in sample_set:
        mock_wrap_var.assert_any_call(item)

    # Verify that the wrapped set contains the expected wrapped items
    expected_wrapped_set = {f"wrapped_{item}" for item in sample_set}
    assert wrapped_set == expected_wrapped_set
