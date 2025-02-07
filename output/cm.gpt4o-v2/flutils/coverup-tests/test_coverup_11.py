# file: flutils/txtutils.py:249-253
# asked: {"lines": [249, 250, 251, 252, 253], "branches": [[252, 0], [252, 253]]}
# gained: {"lines": [249, 250, 251, 252, 253], "branches": [[252, 0], [252, 253]]}

import pytest
from flutils.txtutils import AnsiTextWrapper

def test_placeholder_setter():
    wrapper = AnsiTextWrapper()
    
    # Set placeholder to a new value
    new_placeholder = " [truncated]"
    wrapper.placeholder = new_placeholder
    
    # Assert that the placeholder is set correctly
    assert wrapper.placeholder == new_placeholder
    
    # Set a cached property to ensure it gets deleted
    _ = wrapper.placeholder_len
    assert 'placeholder_len' in wrapper.__dict__
    
    # Change the placeholder again to trigger the deletion of the cached property
    wrapper.placeholder = " [cut]"
    assert wrapper.placeholder == " [cut]"
    assert 'placeholder_len' not in wrapper.__dict__

