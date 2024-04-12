# file lib/ansible/utils/unsafe_proxy.py:117-118
# lines [118]
# branches []

import pytest
from ansible.utils.unsafe_proxy import wrap_var, AnsibleUnsafeText

def test_wrap_set_executes_line_118():
    # Create a set with an AnsibleUnsafeText object to trigger the wrap_var call
    original_set = {AnsibleUnsafeText("unsafe_text")}

    # Call the function that includes line 118
    wrapped_set = wrap_var(original_set)

    # Verify that the returned set is wrapped correctly
    # This assumes that wrap_var returns an AnsibleUnsafeText object for simplicity
    # Replace with the actual expected behavior of wrap_var
    assert isinstance(wrapped_set, set)
    for item in wrapped_set:
        assert isinstance(item, AnsibleUnsafeText)
